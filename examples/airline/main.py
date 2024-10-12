from configs.agents import *
from swarm.repl import run_demo_loop

# コンテキスト変数の設定
# これらの変数は顧客情報とフライト情報を含み、エージェントの対話に使用されます
context_variables = {
    "customer_context": """ここに顧客の詳細情報があります:
1. CUSTOMER_ID: customer_12345
2. NAME: John Doe
3. PHONE_NUMBER: (123) 456-7890
4. EMAIL: johndoe@example.com
5. STATUS: Premium
6. ACCOUNT_STATUS: Active
7. BALANCE: $0.00
8. LOCATION: 1234 Main St, San Francisco, CA 94123, USA
""",
    "flight_context": """顧客は、ニューヨークのLGA（ラガーディア）からロサンゼルスのLAXへの次の便を予約しています。
フライト番号は1919です。出発日時は2024年5月21日午後3時（東部時間）です。""",
}

if __name__ == "__main__":
    # デモループの実行
    # triage_agentを初期エージェントとして使用し、コンテキスト変数を渡してデバッグモードで実行
    run_demo_loop(triage_agent, context_variables=context_variables, debug=True)

# 解説：
# このスクリプトは、Swarmフレームワークを使用して対話式のカスタマーサービスデモを実行します。
# context_variablesには顧客とフライトの情報が含まれており、これらはエージェントが対話中に参照できます。
# run_demo_loopは、ユーザーとエージェント間の対話を管理し、triage_agentから始まる対話フローを実行します。
