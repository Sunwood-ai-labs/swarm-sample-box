from swarm import Swarm, Agent

client = Swarm()

# 英語エージェントの設定
english_agent = Agent(
    name="English Agent",
    instructions="あなたは英語のみを話します。",
)

# スペイン語エージェントの設定
spanish_agent = Agent(
    name="Spanish Agent",
    instructions="あなたはスペイン語のみを話します。",
)


def transfer_to_spanish_agent():
    """スペイン語を話すユーザーを即座に転送します。"""
    return spanish_agent


# 英語エージェントに関数を追加
english_agent.functions.append(transfer_to_spanish_agent)

# メッセージの設定と実行
messages = [{"role": "user", "content": "Hola. ¿Como estás?"}]
response = client.run(agent=english_agent, messages=messages)

# 応答の出力
print(response.messages[-1]["content"])
