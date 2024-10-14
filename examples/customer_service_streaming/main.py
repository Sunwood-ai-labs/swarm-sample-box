"""
このスクリプトは、Swarmフレームワークを使用してカスタマーサービスタスクを実行します。
主な機能:
1. コマンドライン引数の解析
2. ツールとアシスタントの検証
3. テストモードまたは対話モードでのタスク実行
4. 事前定義されたタスクの実行

進捗状況はloguruを使用して表示されます。
"""

import shlex
import argparse
from loguru import logger
from art import text2art

from src.swarm.swarm import Swarm
from src.tasks.task import Task
from configs.general import test_root, test_file, engine_name, persist
from src.validator import validate_all_tools, validate_all_assistants
from src.arg_parser import parse_args


from pyfiglet import Figlet
from colorama import init, Fore, Style

# coloramaの初期化
init(autoreset=True)

def generate_ascii_art(text, font="standard", color=Fore.WHITE):
    """
    指定されたテキスト、フォント、色でASCIIアートを生成します。
    
    :param text: 変換するテキスト
    :param font: 使用するフォント (デフォルト: "standard")
    :param color: テキストの色 (デフォルト: 白)
    :return: 色付きのASCIIアート文字列
    """
    f = Figlet(font=font)
    ascii_art = f.renderText(text)
    
    # 各行に色を適用
    colored_ascii_art = "\n".join([f"{color}{line}{Style.RESET_ALL}" for line in ascii_art.split("\n")])
    
    return colored_ascii_art

# 使用例
print(generate_ascii_art("Swarm Sample", font="slant", color=Fore.CYAN))
print(generate_ascii_art(">> Customer service streaming", font="slant", color=Fore.YELLOW))

def main():
    logger.info("Swarmの実行を開始します")

    args = parse_args()
    logger.info(f"解析されたコマンドライン引数: {args}")

    try:
        logger.info("ツールとアシスタントの検証を開始します")
        validate_all_tools(engine_name)
        validate_all_assistants()
        logger.success("ツールとアシスタントの検証が成功しました")
    except Exception as e:
        logger.error(f"検証に失敗しました: {e}")
        raise Exception("検証に失敗しました")

    swarm = Swarm(engine_name=engine_name, persist=persist)
    logger.info(f"Swarmを初期化しました (engine: {engine_name}, persist: {persist})")

    if args.test is not None:
        logger.info("テストモードで実行します")
        test_files = args.test
        if len(test_files) == 0:
            test_file_paths = [f"{test_root}/{test_file}"]
        else:
            test_file_paths = [f"{test_root}/{file}" for file in test_files]
        swarm = Swarm(engine_name='local')
        swarm.deploy(test_mode=True, test_file_paths=test_file_paths)

    elif args.input:
        logger.info("対話モードで実行します")
        # 対話モードでタスクを追加
        while True:
            print("タスクを入力してください（終了する場合は 'exit' と入力）:")
            task_input = input()

            # 終了コマンドのチェック
            if task_input.lower() == 'exit':
                logger.info("対話モードを終了します")
                break

            # shlexを使用してタスクの説明と引数を解析
            task_args = shlex.split(task_input)
            task_parser = argparse.ArgumentParser()
            task_parser.add_argument("description", type=str, nargs='?', default="")
            task_parser.add_argument("--iterate", action="store_true", help="新しいタスクの反復フラグを設定します。")
            task_parser.add_argument("--evaluate", action="store_true", help="新しいタスクの評価フラグを設定します。")
            task_parser.add_argument("--assistant", type=str, default="user_interface", help="タスクのアシスタントを指定します。")

            # タスク引数の解析
            task_parsed_args = task_parser.parse_args(task_args)

            # 新しいタスクの作成と追加
            new_task = Task(description=task_parsed_args.description,
                            iterate=task_parsed_args.iterate,
                            evaluate=task_parsed_args.evaluate,
                            assistant=task_parsed_args.assistant)
            swarm.add_task(new_task)
            logger.info(f"新しいタスクを追加しました: {new_task.description}")

            # 新しいタスクでSwarmをデプロイ
            swarm.deploy()
            swarm.tasks.clear()

    else:
        logger.info("事前定義されたタスクを読み込みます")
        # 事前定義されたタスクがあれば読み込む
        # 事前定義されたタスクでSwarmをデプロイ
        swarm.load_tasks()
        swarm.deploy()

    logger.success("Swarmの操作が完了しました")
    print("\n\n🍯🐝🍯 Swarm operations complete 🍯🐝🍯\n\n")


if __name__ == "__main__":
    main()
