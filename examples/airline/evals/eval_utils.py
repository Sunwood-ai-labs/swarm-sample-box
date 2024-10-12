import datetime
import json
import uuid

from swarm import Swarm

def run_function_evals(agent, test_cases, n=1, eval_path=None):
    # 正しく処理されたケースの数をカウント
    correct_function = 0
    # 全テストケースの結果を格納するリスト
    results = []
    # 評価の一意のIDと実行時刻を生成
    eval_id = str(uuid.uuid4())
    eval_timestamp = datetime.datetime.now().isoformat()
    # Swarmクライアントのインスタンスを作成
    client = Swarm()

    for test_case in test_cases:
        # 各テストケースで正しく処理された回数をカウント
        case_correct = 0
        # テストケースの結果を格納する辞書
        case_results = {
            "messages": test_case["conversation"],
            "expected_function": test_case["function"],
            "actual_function": [],
            "actual_message": [],
        }
        print(50 * "--")
        print(f"\033[94m会話: \033[0m{test_case['conversation']}\n")
        
        # 各テストケースをn回実行
        for i in range(n):
            print(f"\033[90m反復: {i + 1}/{n}\033[0m")
            # エージェントを実行し、応答を取得
            response = client.run(
                agent=agent, messages=test_case["conversation"], max_turns=1
            )
            output = extract_response_info(response)
            actual_function = output.get("tool_calls", "None")
            actual_message = output.get("message", "None")

            # 実際の関数呼び出しとメッセージを結果に追加
            case_results["actual_function"].append(actual_function)
            case_results["actual_message"].append(actual_message)

            # ツール呼び出しがあった場合の処理
            if "tool_calls" in output:
                print(
                    f'\033[95m期待される関数: \033[0m {test_case["function"]}, \033[95m実際: \033[0m{output["tool_calls"]}\n'
                )
                if output["tool_calls"] == test_case["function"]:
                    case_correct += 1
                    correct_function += 1
            # メッセージのみの場合の処理
            elif "message" in output:
                print(
                    f'\033[95m期待される関数: \033[0m {test_case["function"]}, \033[95m実際: \033[0mNone'
                )
                print(f'\033[90mメッセージ: {output["message"]}\033[0m\n')
                if test_case["function"] == "None":
                    case_correct += 1
                    correct_function += 1

        # テストケースの精度を計算
        case_accuracy = (case_correct / n) * 100
        case_results["case_accuracy"] = f"{case_accuracy:.2f}%"
        results.append(case_results)

        print(
            f"\033[92mこのケースでの正解数: {case_correct} / {n}\033[0m"
        )
        print(f"\033[93mこのケースの精度: {case_accuracy:.2f}%\033[0m")
    
    # 全体の精度を計算
    overall_accuracy = (correct_function / (len(test_cases) * n)) * 100
    print(50 * "**")
    print(
        f"\n\033[92m全体: 正しく選択された関数: {correct_function} / {len(test_cases) * n}\033[0m"
    )
    print(f"\033[93m全体の精度: {overall_accuracy:.2f}%\033[0m")

    # 最終結果をまとめる
    final_result = {
        "id": eval_id,
        "timestamp": eval_timestamp,
        "results": results,
        "correct_evals": correct_function,
        "total_evals": len(test_cases) * n,
        "overall_accuracy_percent": f"{overall_accuracy:.2f}%",
    }

    # 評価結果をファイルに保存（オプション）
    if eval_path:
        try:
            with open(eval_path, "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        if not isinstance(existing_data, list):
            existing_data = [existing_data]

        existing_data.append(final_result)

        with open(eval_path, "w") as file:
            json.dump(existing_data, file, indent=4)

    return overall_accuracy

def extract_response_info(response):
    # レスポンスから関連情報を抽出
    results = {}
    for message in response.messages:
        if message["role"] == "tool":
            results["tool_calls"] = message["tool_name"]
            break
        elif not message["tool_calls"]:
            results["message"] = message["content"]
    return results

# 解説：
# このスクリプトは、エージェントの機能評価を実行するためのものです。
# 主な機能は以下の通りです：
# 1. 指定されたエージェントに対して、一連のテストケースを実行します。
# 2. 各テストケースは指定回数（n回）実行され、期待される関数呼び出しと実際の結果を比較します。
# 3. テストケースごとの精度と全体の精度を計算し、表示します。
# 4. 評価結果を詳細にまとめ、オプションでファイルに保存します。
# 5. 色付きの出力を使用して、結果を見やすく表示します。

# このスクリプトは、エージェントの性能を定量的に評価し、その結果を分析するのに役立ちます。
# 特に、多数のテストケースや繰り返し実行が必要な場合に有用です。
