from swarm import Swarm, Agent

client = Swarm()


def instructions(context_variables):
    # コンテキスト変数から名前を取得し、指示を生成
    name = context_variables.get("name", "ユーザー")
    return f"あなたは役立つエージェントです。ユーザーを名前（{name}）で挨拶してください。"


def print_account_details(context_variables: dict):
    # アカウント詳細の出力
    user_id = context_variables.get("user_id", None)
    name = context_variables.get("name", None)
    print(f"アカウント詳細: {name} {user_id}")
    return "成功"


# エージェントの設定
agent = Agent(
    name="Agent",
    instructions=instructions,
    functions=[print_account_details],
)

# コンテキスト変数の設定
context_variables = {"name": "ジェームズ", "user_id": 123}

# 最初の応答を実行
response = client.run(
    messages=[{"role": "user", "content": "こんにちは！"}],
    agent=agent,
    context_variables=context_variables,
)
print(response.messages[-1]["content"])

# アカウント詳細の出力を実行
response = client.run(
    messages=[{"role": "user", "content": "アカウント詳細を表示してください！"}],
    agent=agent,
    context_variables=context_variables,
)
print(response.messages[-1]["content"])
