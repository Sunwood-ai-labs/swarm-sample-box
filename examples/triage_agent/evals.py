from swarm import Swarm
from agents import triage_agent, sales_agent, refunds_agent
from evals_util import evaluate_with_llm_bool, BoolEvalResult
import pytest
import json
from loguru import logger
from art import text2art

# Display ASCII art
print(text2art("Triage Agent"))
print(text2art("Evals"))

# このスクリプトは、エージェントの動作をテストし、会話の成功を評価するための関数とテストケースを定義します。

logger.info("評価システムの初期化を開始します")

client = Swarm()

CONVERSATIONAL_EVAL_SYSTEM_PROMPT = """
ユーザーとエージェントの会話、および会話の主な目標が提供されます。
会話に基づいて、エージェントが主な目標を達成したかどうかを評価することがあなたの目標です。

エージェントが主な目標を達成したかどうかを評価する際には、主な目標に含まれる指示と、ユーザーの反応を考慮してください：
ユーザーにとって回答は満足のいくものですか？主な目標を考慮すると、エージェントはもっと良い対応ができたでしょうか？
ユーザーが回答に満足していなくても、エージェントが主な目標の一部として提供された指示に従っている場合、エージェントは主な目標を達成している可能性があります。
"""

def conversation_was_successful(messages) -> bool:
    logger.info("会話の成功を評価しています")
    conversation = f"CONVERSATION: {json.dumps(messages)}"
    result: BoolEvalResult = evaluate_with_llm_bool(
        CONVERSATIONAL_EVAL_SYSTEM_PROMPT, conversation
    )
    return result.value

def run_and_get_tool_calls(agent, query):
    logger.info(f"エージェント '{agent.name}' に対してクエリを実行しています: {query}")
    message = {"role": "user", "content": query}
    response = client.run(
        agent=agent,
        messages=[message],
        execute_tools=False,
    )
    return response.messages[-1].get("tool_calls")

@pytest.mark.parametrize(
    "query,function_name",
    [
        ("返金したいです！", "transfer_to_refunds"),
        ("販売担当と話したいです。", "transfer_to_sales"),
    ],
)
def test_triage_agent_calls_correct_function(query, function_name):
    logger.info(f"トリアージエージェントのテストを実行しています: {query}")
    tool_calls = run_and_get_tool_calls(triage_agent, query)

    assert len(tool_calls) == 1
    assert tool_calls[0]["function"]["name"] == function_name
    logger.info(f"テスト成功: 正しい関数 '{function_name}' が呼び出されました")

@pytest.mark.parametrize(
    "messages",
    [
        [
            {"role": "user", "content": "U2のリードシンガーは誰ですか"},
            {"role": "assistant", "content": "U2のリードシンガーはボノです。"},
        ],
        [
            {"role": "user", "content": "こんにちは！"},
            {"role": "assistant", "content": "こんにちは！どのようなお手伝いができますか？"},
            {"role": "user", "content": "返金したいです。"},
            {"role": "tool", "tool_name": "transfer_to_refunds"},
            {"role": "user", "content": "ありがとうございます！"},
            {"role": "assistant", "content": "どういたしまして！良い一日をお過ごしください！"},
        ],
    ],
)
def test_conversation_is_successful(messages):
    logger.info("会話の成功テストを実行しています")
    result = conversation_was_successful(messages)
    assert result == True
    logger.info("テスト成功: 会話は成功と評価されました")

logger.info("全てのテストと評価の定義が完了しました")
