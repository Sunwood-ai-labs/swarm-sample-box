"""
このスクリプトは、OpenAIのヘルプセンター記事をベクトルデータベース（Qdrant）に準備し格納します。
主な手順:
1. JSONファイルから記事を読み込む
2. 各記事のテキストをOpenAIのEmbedding APIを使用してベクトル化
3. ベクトル化されたデータをQdrantデータベースに格納

進捗状況はtqdmとloguruを使用して表示されます。
"""

import json
import os
from tqdm import tqdm
from loguru import logger
from art import text2art

import pandas as pd
import qdrant_client
from openai import OpenAI
from qdrant_client.http import models as rest

from pyfiglet import Figlet
from colorama import init, Fore, Style

# coloramaの初期化
init(autoreset=True)

def generate_ascii_art(text, font="standard", color=Fore.WHITE):
    """
    指定されたテキスト、フォント、色でASCIIアートを生成します。
    
    :param text: 変換するテキスト
    :param font: 使用するフォント (デフォルト: "standard")
    :param color: テキストの色 (デフォルト: 白)
    :return: 色付きのASCIIアート文字列
    """
    f = Figlet(font=font)
    ascii_art = f.renderText(text)
    
    # 各行に色を適用
    colored_ascii_art = "\n".join([f"{color}{line}{Style.RESET_ALL}" for line in ascii_art.split("\n")])
    
    return colored_ascii_art

# 使用例
print(generate_ascii_art("Swarm Sample", font="slant", color=Fore.CYAN))
print(generate_ascii_art(">> Customer service streaming", font="slant", color=Fore.YELLOW))

# ロギングの設定
logger.add("prep_data.log", rotation="500 MB")

client = OpenAI()
EMBEDDING_MODEL = "text-embedding-3-large"

# データディレクトリから記事リストを取得
# article_list = os.listdir("data_mini")
article_list = os.listdir("data")

articles = []

# 記事の読み込み
logger.info("記事の読み込みを開始します")
for x in tqdm(article_list, desc="記事の読み込み"):
    # article_path = "data_mini/" + x
    article_path = "data/" + x

    # JSONファイルを開く
    with open(article_path, 'r') as f:
        # JSONオブジェクトを辞書として読み込む
        data = json.load(f)
        articles.append(data)

logger.info(f"{len(articles)}件の記事を読み込みました")

# 各記事のembeddingを作成
logger.info("記事のembedding作成を開始します")
for i, x in tqdm(enumerate(articles), desc="Embedding作成", total=len(articles)):
    try:
        embedding = client.embeddings.create(model=EMBEDDING_MODEL, input=x["text"])
        articles[i].update({"embedding": embedding.data[0].embedding})
    except Exception as e:
        logger.error(f"記事 '{x['title']}' のembedding作成中にエラーが発生しました: {e}")

# Qdrantクライアントの初期化
qdrant = qdrant_client.QdrantClient(host="localhost", port=6333)
logger.info("Qdrantに接続しました")

collection_name = "help_center"

# 最初の記事のembeddingサイズを取得
vector_size = len(articles[0]["embedding"])

# 記事をDataFrameに変換
article_df = pd.DataFrame(articles)

# 既存のコレクションがあれば削除（記事に変更があった場合に再作成するため）
try:
    if qdrant.get_collection(collection_name=collection_name):
        logger.info(f"既存の '{collection_name}' コレクションを削除します")
        qdrant.delete_collection(collection_name=collection_name)
except Exception as e:
    logger.info(f"'{collection_name}' コレクションが存在しません。新規作成します。")

# ベクターDBコレクションの作成
logger.info(f"'{collection_name}' コレクションを作成します")
qdrant.create_collection(
    collection_name=collection_name,
    vectors_config={
        "article": rest.VectorParams(
            distance=rest.Distance.COSINE,
            size=vector_size,
        )
    },
)

# コレクションにベクターを格納
logger.info("ベクターをコレクションに格納します")
qdrant.upsert(
    collection_name=collection_name,
    points=[
        rest.PointStruct(
            id=k,
            vector={
                "article": v["embedding"],
            },
            payload=v.to_dict(),
        )
        for k, v in tqdm(article_df.iterrows(), desc="ベクター格納", total=len(article_df))
    ],
)

logger.info("データの準備が完了しました")
