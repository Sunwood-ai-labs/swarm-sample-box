from swarm import Swarm, Agent

client = Swarm()

# 基本的なエージェントの設定
agent = Agent(
    name="Agent",
    instructions="あなたは役立つエージェントです。",
)

# メッセージの設定と実行
messages = [{"role": "user", "content": "こんにちは！"}]
response = client.run(agent=agent, messages=messages)

# 応答の出力
print(response.messages[-1]["content"])
