import argparse

def parse_args():
    # コマンドライン引数のパーサーを作成
    parser = argparse.ArgumentParser()

    # エンジンの選択（ローカルまたはアシスタント）
    parser.add_argument("--engine", choices=["local", "assistants"], default="local", 
                        help="使用するエンジンを選択します。")

    # テストの実行
    parser.add_argument("--test", nargs='*', help="テストを実行します。")

    # 新しいタスクの作成
    parser.add_argument("--create-task", type=str, 
                        help="指定された説明で新しいタスクを作成します。")

    # タスクの説明（位置引数）
    parser.add_argument("task_description", type=str, nargs="?", default="", 
                        help="作成するタスクの説明。")

    # タスクに使用するアシスタントの指定
    parser.add_argument("--assistant", type=str, 
                        help="新しいタスクに使用するアシスタントを指定します。")

    # タスクの評価フラグ
    parser.add_argument("--evaluate", action="store_true", 
                        help="新しいタスクの評価フラグを設定します。")

    # タスクの反復フラグ
    parser.add_argument("--iterate", action="store_true", 
                        help="新しいタスクの反復フラグを設定します。")

    # CLIモードの有効化
    parser.add_argument("--input", action="store_true", 
                        help="対話型のCLIモードを有効にします。")

    # パースされた引数を返す
    return parser.parse_args()
