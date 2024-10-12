# Swarm basic

このフォルダには、Swarmの主要な機能を示す基本的な例が含まれています。これらの例は、1つの入力メッセージとそれに対応する出力を持つ、最もシンプルなSwarmの実装を示しています。`simple_loop_no_helpers`には、対話型Swarmセッションを作成する方法を示すためのwhileループがあります。

### 例

1. **agent_handoff.py**

   - 会話を1つのエージェントから別のエージェントに転送する方法を示します。
   - **使用法**: スペイン語を話すユーザーを英語エージェントからスペイン語エージェントに転送します。

2. **bare_minimum.py**

   - エージェントの基本的なセットアップを示す最小限の例です。
   - **使用法**: シンプルなユーザーメッセージに応答するエージェントをセットアップします。

3. **context_variables.py**

   - エージェント内でコンテキスト変数を使用する方法を示します。
   - **使用法**: コンテキスト変数を使用してユーザーを名前で挨拶し、アカウント詳細を表示します。

4. **function_calling.py**

   - エージェントから関数を定義して呼び出す方法を示します。
   - **使用法**: 指定された場所の天気情報を返すことができるエージェントをセットアップします。

5. **simple_loop_no_helpers.py**
   - ヘルパー関数を使用せずに簡単な対話ループの例を示します。
   - **使用法**: ユーザーがエージェントと継続的に対話できるループをセットアップし、会話を表示します。

## 例の実行方法

任意の例を実行するには、以下のコマンドを使用してください：

```shell
python3 <例のファイル名>.py
```


`simple_loop_no_helpers.py`:

```python
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
```
