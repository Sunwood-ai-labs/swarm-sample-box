# Swarm Basic: 多機能エージェントシステムの基礎

![](https://raw.githubusercontent.com/Sunwood-ai-labs/swarm-sample-box/refs/heads/main/docs/Sample01.png)

このフォルダには、Swarmの主要な機能を示す基本的な例が含まれています。これらの例を通じて、Swarmの核心的な機能と、それらを組み合わせて複雑なAIシステムを構築する方法を学ぶことができます。

## セットアップと実行方法

Swarmを使用するには、以下の手順でセットアップを行います：

```powershell
# 仮想環境の作成と有効化
uv venv
.venv\Scripts\activate

# Swarmのインストール
uv pip install git+https://github.com/openai/swarm.git

# OpenAI APIキーの設定
$env:OPENAI_API_KEY = "your-api-key"

# 例の実行
python <例のファイル名>.py
```

## 例の概要と使用法

1. **agent_handoff.py**: エージェント間の引き継ぎ
   - **機能**: 異なる言語を話すエージェント間でのスムーズな引き継ぎを示します。
   - **使用法**: スペイン語を話すユーザーを英語エージェントからスペイン語エージェントに転送します。
   - **応用**: 多言語カスタマーサポート、言語学習アプリケーション

2. **bare_minimum.py**: 最小限の設定
   - **機能**: Swarmの最も基本的な設定を示します。
   - **使用法**: シンプルなユーザーメッセージに応答するエージェントをセットアップします。
   - **応用**: 迅速なプロトタイピング、シンプルなチャットボットの作成

3. **context_variables.py**: コンテキスト変数の活用
   - **機能**: エージェントの動作をカスタマイズするためのコンテキスト変数の使用方法を示します。
   - **使用法**: コンテキスト変数を使用してユーザーを名前で挨拶し、アカウント詳細を表示します。
   - **応用**: パーソナライズされたユーザー体験、動的なシステム設定管理

4. **function_calling.py**: 関数呼び出し
   - **機能**: エージェントから特定の関数を呼び出す方法を示します。
   - **使用法**: 指定された場所の天気情報を返すことができるエージェントをセットアップします。
   - **応用**: リアルタイムデータ統合、APIとの連携、複雑なタスクの自動化

5. **simple_loop_no_helpers.py**: シンプルな対話ループ
   - **機能**: ヘルパー関数を使用せずに基本的な対話ループを実装する方法を示します。
   - **使用法**: ユーザーがエージェントと継続的に対話できるループをセットアップし、会話を表示します。
   - **応用**: カスタム対話システムの開発、長期的な対話セッションの管理

## コード例: simple_loop_no_helpers.py

以下は、`simple_loop_no_helpers.py`の完全なコード例です：

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

このコードは、ユーザーとエージェントの間で継続的な対話を可能にする基本的なループを実装しています。

## まとめ

これらの例を通じて、Swarmの基本的な機能と、それらを組み合わせて複雑なAIシステムを構築する方法を学ぶことができます。各例は、実際のアプリケーション開発にすぐに応用できる実用的なパターンを提供しており、開発者が自身のプロジェクトに合わせてカスタマイズし、拡張することができます。

Swarmを活用することで、複数のAIエージェントが協調して動作する次世代のインテリジェントシステムの開発が可能になり、ユーザーエクスペリエンスの向上や業務プロセスの最適化など、様々な分野でイノベーションを促進することができるでしょう。
