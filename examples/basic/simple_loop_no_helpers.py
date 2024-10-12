from swarm import Swarm, Agent

client = Swarm()

# エージェントの設定
my_agent = Agent(
    name="Agent",
    instructions="あなたは役立つエージェントです。",
)

def pretty_print_messages(messages):
    # メッセージを整形して表示
    for message in messages:
        if message["content"] is None:
            continue
        print(f"{message['sender']}: {message['content']}")

messages = []
agent = my_agent
while True:
    # ユーザー入力を受け取る
    user_input = input("> ")
    messages.append({"role": "user", "content": user_input})

    # エージェントの応答を取得
    response = client.run(agent=agent, messages=messages)
    messages = response.messages
    agent = response.agent
    pretty_print_messages(messages)
