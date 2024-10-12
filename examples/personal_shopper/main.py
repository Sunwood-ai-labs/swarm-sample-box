import datetime
import random

import database
from swarm import Agent
# from swarm.agents import create_triage_agent
from swarm.repl import run_demo_loop


def refund_item(user_id, item_id):
    """
    ユーザーIDとアイテムIDに基づいて払い戻しを開始する関数
    入力引数のフォーマット: '{"user_id":"1","item_id":"3"}'
    """
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT amount FROM PurchaseHistory
        WHERE user_id = ? AND item_id = ?
    """,
        (user_id, item_id),
    )
    result = cursor.fetchone()
    if result:
        amount = result[0]
        print(f"ユーザーID {user_id} のアイテムID {item_id} に対して ${amount} を払い戻します。")
    else:
        print(f"ユーザーID {user_id} とアイテムID {item_id} に対する購入履歴が見つかりません。")
    print("払い戻しが開始されました")


def notify_customer(user_id, method):
    """
    顧客を電話またはメールで通知する関数
    入力引数のフォーマット: '{"user_id":"1","method":"email"}'
    """
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT email, phone FROM Users
        WHERE user_id = ?
    """,
        (user_id,),
    )
    user = cursor.fetchone()
    if user:
        email, phone = user
        if method == "email" and email:
            print(f"顧客 {email} に通知メールを送信しました。")
        elif method == "phone" and phone:
            print(f"顧客 {phone} に通知SMSを送信しました。")
        else:
            print(f"ユーザーID {user_id} の {method} 連絡先が利用できません。")
    else:
        print(f"ユーザーID {user_id} が見つかりません。")


def order_item(user_id, product_id):
    """
    ユーザーIDと製品IDに基づいて製品を注文する関数
    入力引数のフォーマット: '{"user_id":"1","product_id":"2"}'
    """
    date_of_purchase = datetime.datetime.now()
    item_id = random.randint(1, 300)

    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT product_id, product_name, price FROM Products
        WHERE product_id = ?
    """,
        (product_id,),
    )
    result = cursor.fetchone()
    if result:
        product_id, product_name, price = result
        print(
            f"ユーザーID {user_id} の製品 {product_name} を注文しています。価格は {price} です。"
        )
        # 購入をデータベースに追加
        database.add_purchase(user_id, date_of_purchase, item_id, price)
    else:
        print(f"製品ID {product_id} が見つかりません。")


# データベースの初期化
database.initialize_database()

# テーブルのプレビュー
database.preview_table("Users")
database.preview_table("PurchaseHistory")
database.preview_table("Products")


# エージェント間転送関数
def transfer_to_sales_agent():
    return sales_agent

def transfer_to_refunds_agent():
    return refunds_agent

# エージェントの定義
refunds_agent = Agent(
    name="払い戻しエージェント",
    description="""返品処理後の払い戻しに関するすべてのアクションを処理するエージェントです。
    払い戻しを開始するには、ユーザーIDとアイテムIDの両方が必要です。両方を1つのメッセージで尋ねてください。
    ユーザーが通知を希望する場合は、通知方法を尋ねる必要があります。通知の場合、
    ユーザーIDと通知方法を1つのメッセージで尋ねてください。""",
    functions=[refund_item, notify_customer],
)

sales_agent = Agent(
    name="販売エージェント",
    description="""商品の注文に関するすべてのアクションを処理する販売エージェントです。
    ユーザーが購入したい商品に関わらず、注文を行うにはユーザーIDと製品IDの両方が必要です。
    これらの2つの情報なしでは注文を行うことができません。ユーザーIDと製品IDの両方を1つのメッセージで尋ねてください。
    ユーザーが通知を希望する場合は、通知方法を尋ねる必要があります。通知の場合、
    ユーザーIDと通知方法を1つのメッセージで尋ねてください。
    """,
    functions=[order_item, notify_customer],
)

triage_agent = Agent(
    name="トリアージエージェント",
    instructions="""ユーザーのリクエストを分類し、適切なインテントに転送するツールを呼び出します。
    適切なインテントに転送する準備ができたら、ツールを呼び出してください。
    詳細を知る必要はなく、リクエストのトピックだけを理解すれば十分です。
    ユーザーのリクエストが注文や商品の購入に関するものであれば、販売エージェントに転送します。
    ユーザーのリクエストが商品の払い戻しや返品に関するものであれば、払い戻しエージェントに転送します。
    リクエストをエージェントに振り分けるために更に情報が必要な場合は、理由を説明せずに直接質問してください。
    ユーザーに思考プロセスを共有しないでください！ユーザーに代わって不合理な仮定をしないでください。""",
    functions=[transfer_to_sales_agent, transfer_to_refunds_agent],
)

print("-------------------------------------")
for f in triage_agent.functions:
    print(f.__name__)
print("-------------------------------------")

if __name__ == "__main__":
    # デモループの実行
    run_demo_loop(triage_agent, debug=False)
