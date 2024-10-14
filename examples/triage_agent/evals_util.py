from openai import OpenAI
import instructor
from pydantic import BaseModel
from typing import Optional
from loguru import logger
from art import text2art

# Display ASCII art
print(text2art("Triage Agent"))
print(text2art("Evals Util"))

# このスクリプトは、LLMを使用して会話を評価するためのユーティリティ関数を提供します。

logger.info("評価ユーティリティの初期化を開始します")

__client = instructor.from_openai(OpenAI())

class BoolEvalResult(BaseModel):
    value: bool
    reason: Optional[str]

def evaluate_with_llm_bool(instruction, data) -> BoolEvalResult:
    logger.info("LLMを使用してブール評価を実行しています")
    eval_result, _ = __client.chat.completions.create_with_completion(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": data},
        ],
        response_model=BoolEvalResult,
    )
    logger.info(f"評価結果: {eval_result.value}, 理由: {eval_result.reason}")
    return eval_result

logger.info("評価ユーティリティの初期化が完了しました")
