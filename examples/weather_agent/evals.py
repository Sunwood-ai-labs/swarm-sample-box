# -*- coding: utf-8 -*-
# 天気エージェントの評価テスト
# このファイルでは、天気エージェントの機能をテストするための評価関数を定義します

from swarm import Swarm
from agents import weather_agent
import pytest

client = Swarm()


def run_and_get_tool_calls(agent, query):
    """エージェントにクエリを実行させ、ツール呼び出しを取得する関数"""
    message = {"role": "user", "content": query}
    response = client.run(
        agent=agent,
        messages=[message],
        execute_tools=False,
    )
    return response.messages[-1].get("tool_calls")


@pytest.mark.parametrize(
    "query",
    [
        "東京の天気は？",
        "那覇の天気を教えて。",
        "今日、傘が必要？札幌にいます。",
    ],
)
def test_calls_weather_when_asked(query):
    """天気について尋ねられた時に正しく天気関数を呼び出すかテストする"""
    tool_calls = run_and_get_tool_calls(weather_agent, query)

    assert len(tool_calls) == 1
    assert tool_calls[0]["function"]["name"] == "get_weather"


@pytest.mark.parametrize(
    "query",
    [
        "アメリカ合衆国の大統領は誰？",
        "今何時？",
        "こんにちは！",
    ],
)
def test_does_not_call_weather_when_not_asked(query):
    """天気と関係ない質問をされた時に天気関数を呼び出さないことをテストする"""
    tool_calls = run_and_get_tool_calls(weather_agent, query)

    assert not tool_calls
