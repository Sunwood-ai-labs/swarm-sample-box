import json

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('.')

from configs.agents import *
from evals.eval_utils import run_function_evals

# 評価用のテストケースファイルのパス
triage_test_cases = "eval_cases/triage_cases_JP.json"
flight_modification_cases = "eval_cases/flight_modification_cases_JP.json"

# 各テストケースの実行回数
n = 5

if __name__ == "__main__":
    # 振り分けエージェント（triage_agent）の評価を実行
    with open(triage_test_cases, "r") as file:
        triage_test_cases = json.load(file)
    run_function_evals(
        triage_agent,
        triage_test_cases,
        n,
        eval_path="eval_results/triage_evals_JP.json",
    )

    # フライト変更エージェント（flight_modification）の評価を実行
    with open(flight_modification_cases, "r") as file:
        flight_modification_cases = json.load(file)
    run_function_evals(
        flight_modification,
        flight_modification_cases,
        n,
        eval_path="eval_results/flight_modification_evals_JP.json",
    )

# 解説：
# このスクリプトは、航空会社のカスタマーサービスシステムにおける
# 2つの主要なエージェント（振り分けエージェントとフライト変更エージェント）の
# 機能評価を自動的に実行するためのものです。

# 主な機能：
# 1. 振り分けエージェント（triage_agent）の評価：
#    - triage_cases.jsonファイルからテストケースを読み込みます。
#    - run_function_evalsを使用して評価を実行します。
#    - 結果はtriage_evals.jsonファイルに保存されます。

# 2. フライト変更エージェント（flight_modification）の評価：
#    - flight_modification_cases.jsonファイルからテストケースを読み込みます。
#    - 同じくrun_function_evalsを使用して評価を実行します。
#    - 結果はflight_modification_evals.jsonファイルに保存されます。

# 各評価は5回（n=5）繰り返され、これにより結果の信頼性が向上します。

# このスクリプトを実行することで、両エージェントの性能を
# 一度に評価し、結果を別々のJSONファイルに保存できます。
# これは、エージェントの改善や性能の継続的なモニタリングに役立ちます。
