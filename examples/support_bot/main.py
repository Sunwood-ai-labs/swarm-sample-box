"""
このスクリプトは、Support Botのメイン実行ファイルです。
ユーザーインターフェースエージェントとヘルプセンターエージェントを設定し、
対話ループを開始します。
"""

from art import text2art
import re

import qdrant_client
from openai import OpenAI

from swarm import Agent
from swarm.repl import run_demo_loop

# ASCII artで"Support Bot Main"を表示
print(text2art("Support Bot"))
print(text2art("Main"))

# 接続の初期化
client = OpenAI()
qdrant = qdrant_client.QdrantClient(host="localhost", port=6333)

# 埋め込みモデルの設定
EMBEDDING_MODEL = "text-embedding-3-large"

# Qdrantコレクションの設定
collection_name = "help_center"


def query_qdrant(query, collection_name, vector_name="article", top_k=5):
    """ユーザークエリの埋め込みベクトルを作成し、Qdrantで検索を実行"""
    embedded_query = (
        client.embeddings.create(
            input=query,
            model=EMBEDDING_MODEL,
        )
        .data[0]
        .embedding
    )

    query_results = qdrant.search(
        collection_name=collection_name,
        query_vector=(vector_name, embedded_query),
        limit=top_k,
    )

    return query_results


def query_docs(query):
    """関連記事のナレッジベースを検索"""
    print(f"ナレッジベースを検索中: {query}")
    query_results = query_qdrant(query, collection_name=collection_name)
    output = []

    for i, article in enumerate(query_results):
        title = article.payload["title"]
        text = article.payload["text"]
        url = article.payload["url"]

        output.append((title, text, url))

    if output:
        title, content, _ = output[0]
        response = f"タイトル: {title}\n内容: {content}"
        truncated_content = re.sub(
            r"\s+", " ", content[:50] + "..." if len(content) > 50 else content
        )
        print("最も関連性の高い記事のタイトル:", truncated_content)
        return {"response": response}
    else:
        print("結果なし")
        return {"response": "該当する記事が見つかりませんでした。"}


def send_email(email_address, message):
    """ユーザーにメールを送信"""
    response = f"メール送信先: {email_address}, メッセージ: {message}"
    return {"response": response}


def submit_ticket(description):
    """ユーザーのチケットを提出"""
    return {"response": f"チケットが作成されました: {description}"}


def transfer_to_help_center():
    """ユーザーをヘルプセンターエージェントに転送"""
    return help_center_agent


user_interface_agent = Agent(
    name="ユーザーインターフェースエージェント",
    instructions="あなたはユーザーとのすべてのやり取りを処理するユーザーインターフェースエージェントです。一般的な質問や、他のエージェントが適切でない場合にこのエージェントを呼び出してください。",
    functions=[transfer_to_help_center],
)

help_center_agent = Agent(
    name="ヘルプセンターエージェント",
    instructions="あなたはOpenAIのヘルプセンターエージェントで、GPTモデル、DALL-E、Whisperなど、OpenAI製品に関する質問を扱います。",
    functions=[query_docs, submit_ticket, send_email],
)

# 新しい関数: サンプル質問を表示
def display_sample_questions():
    sample_questions = [
        "OpenAI APIの認証エラーが発生しています。どう対処すればいいですか？",
        "Whisperで対応している言語は何ですか？",
        "サブスクリプションプランの変更方法を教えてください。",
        "最近リリースされたOpenAI製品の新機能について教えてください。",
        "GPT-3.5のファインチューニングに関するガイドはどこにありますか？",
        "APIの使用中に特殊なエラーが発生しました。開発者チームに確認してもらえますか？",
        "GPT-4の出力品質について感想を伝えたいのですが。",
        "テキスト生成以外のAI機能を探しています。OpenAIで何か適切なものはありますか？"
    ]
    
    print("\nサンプル質問:")
    for i, question in enumerate(sample_questions, 1):
        print(f"{i}. {question}")
    print("\n以上のような質問に対応できます。実際の質問をどうぞ。\n")

# メイン実行部分
if __name__ == "__main__":
    display_sample_questions()
    run_demo_loop(user_interface_agent)
