from swarm import Swarm, Agent

client = Swarm()


def get_weather(location) -> str:
    # 天気情報を返す関数（ダミーデータ）
    return "{'temp':67, 'unit':'F'}"


# エージェントの設定
agent = Agent(
    name="Agent",
    instructions="あなたは役立つエージェントです。",
    functions=[get_weather],
)

# メッセージの設定と実行
messages = [{"role": "user", "content": "ニューヨークの天気はどうですか？"}]

response = client.run(agent=agent, messages=messages)
print(response.messages[-1]["content"])
