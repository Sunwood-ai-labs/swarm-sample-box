from configs.tools import *
from data.routines.baggage.policies import *
from data.routines.flight_modification.policies import *
from data.routines.prompts import STARTER_PROMPT

from swarm import Agent

# 各エージェントへの転送関数
def transfer_to_flight_modification():
    return flight_modification

def transfer_to_flight_cancel():
    return flight_cancel

def transfer_to_flight_change():
    return flight_change

def transfer_to_lost_baggage():
    return lost_baggage

def transfer_to_triage():
    """
    ユーザーを別のエージェントや別のポリシーに転送する必要がある場合にこの関数を呼び出します。
    例えば、ユーザーが現在のエージェントでは扱えないトピックについて質問している場合などに使用します。
    """
    return triage_agent

# 振り分けエージェントの指示を生成する関数
def triage_instructions(context_variables):
    customer_context = context_variables.get("customer_context", None)
    flight_context = context_variables.get("flight_context", None)
    return f"""ユーザーのリクエストを振り分け、適切な意図に転送するためのツールを呼び出してください。
    適切な意図に転送する準備ができたら、ツールを呼び出して転送してください。
    詳細を知る必要はありません。リクエストのトピックだけを理解すればよいです。
    エージェントにリクエストを振り分けるためにより多くの情報が必要な場合は、理由を説明せずに直接質問してください。
    思考プロセスをユーザーと共有しないでください！ユーザーに代わって不合理な仮定をしないでください。
    顧客コンテキストはこちらです: {customer_context}、フライトコンテキストはこちらです: {flight_context}"""

# 各エージェントの定義
# 振り分けエージェント：ユーザーのリクエストを適切なエージェントに振り分ける
triage_agent = Agent(
    name="振り分けエージェント",
    instructions=triage_instructions,
    functions=[transfer_to_flight_modification, transfer_to_lost_baggage],
)

# フライト変更エージェント：フライトの変更やキャンセルに関するリクエストを処理
flight_modification = Agent(
    name="フライト変更エージェント",
    instructions="""あなたは航空会社のカスタマーサービスのフライト変更エージェントです。
      ユーザーがどのサブ意図に紹介されるべきかを決定する専門のカスタマーサービスエージェントです。
意図がフライト変更関連の質問であることは既に分かっています。まず、メッセージ履歴を見て、ユーザーがフライトをキャンセルしたいのか変更したいのかを判断できるか確認してください。
ユーザーがキャンセルリクエストなのか変更リクエストなのかが分かるまで、明確化のための質問をしてください。分かったら、適切な転送関数を呼び出してください。毎回、明確化のための質問をするか、関数の1つを呼び出してください。""",
    functions=[transfer_to_flight_cancel, transfer_to_flight_change],
    parallel_tool_calls=False,
)

# フライトキャンセルエージェント：フライトのキャンセルに特化した処理を行う
flight_cancel = Agent(
    name="フライトキャンセル処理",
    instructions=STARTER_PROMPT + FLIGHT_CANCELLATION_POLICY,
    functions=[
        escalate_to_agent,
        initiate_refund,
        initiate_flight_credits,
        transfer_to_triage,
        case_resolved,
    ],
)

# フライト変更エージェント：フライトの変更に特化した処理を行う
flight_change = Agent(
    name="フライト変更処理",
    instructions=STARTER_PROMPT + FLIGHT_CHANGE_POLICY,
    functions=[
        escalate_to_agent,
        change_flight,
        valid_to_change_flight,
        transfer_to_triage,
        case_resolved,
    ],
)

# 手荷物紛失エージェント：手荷物の紛失に関する問い合わせを処理する
lost_baggage = Agent(
    name="手荷物紛失処理",
    instructions=STARTER_PROMPT + LOST_BAGGAGE_POLICY,
    functions=[
        escalate_to_agent,
        initiate_baggage_search,
        transfer_to_triage,
        case_resolved,
    ],
)

# 解説：
# このファイルでは、各種エージェントとそれらの転送関数を定義しています。
# 各エージェントは特定の役割（振り分け、フライト変更、キャンセル、手荷物紛失）を持ち、
# それぞれに適した指示と利用可能な関数が設定されています。
# エージェント間の転送を管理することで、複雑な顧客サービスのフローを実現しています。
