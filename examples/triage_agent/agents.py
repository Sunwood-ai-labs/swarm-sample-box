from swarm import Agent
from loguru import logger
from art import text2art

# Display ASCII art
print(text2art("Triage Agent"))
print(text2art("Agents"))

# このスクリプトは、トリアージ、販売、返金の各エージェントとその機能を定義します。
# エージェント間の移動を可能にする転送機能も含まれています。

logger.info("エージェントと機能の定義を開始します")

def process_refund(item_id, reason="NOT SPECIFIED"):
    """アイテムの返金を処理します。item_idは'item_...'の形式である必要があります。返金処理前にユーザーの確認を取ってください。"""
    logger.info(f"アイテム {item_id} の返金処理を開始します。理由: {reason}")
    print(f"[mock] アイテム {item_id} を返金しています。理由: {reason}...")
    return "成功!"

def apply_discount():
    """ユーザーのカートに割引を適用します。"""
    logger.info("割引の適用を開始します")
    print("[mock] 割引を適用しています...")
    return "11%の割引を適用しました"

logger.info("トリアージエージェントを定義しています")
triage_agent = Agent(
    name="トリアージエージェント",
    instructions="ユーザーの要求を最適に処理できるエージェントを判断し、その会話をそのエージェントに転送します。",
)

logger.info("販売エージェントを定義しています")
sales_agent = Agent(
    name="販売エージェント",
    instructions="蜂の販売に非常に熱心になってください。",
)

logger.info("返金エージェントを定義しています")
refunds_agent = Agent(
    name="返金エージェント",
    instructions="ユーザーの返金要求を処理します。理由が高額すぎる場合は、返金コードを提供してください。ユーザーが主張する場合は、返金を処理します。",
    functions=[process_refund, apply_discount],
)

def transfer_back_to_triage():
    """現在のエージェントが処理できないトピックについてユーザーが質問している場合、この関数を呼び出します。"""
    logger.info("トリアージエージェントに転送します")
    return triage_agent

def transfer_to_sales():
    logger.info("販売エージェントに転送します")
    return sales_agent

def transfer_to_refunds():
    logger.info("返金エージェントに転送します")
    return refunds_agent

# エージェントに転送機能を追加
triage_agent.functions = [transfer_to_sales, transfer_to_refunds]
sales_agent.functions.append(transfer_back_to_triage)
refunds_agent.functions.append(transfer_back_to_triage)

logger.info("エージェントと機能の定義が完了しました")
