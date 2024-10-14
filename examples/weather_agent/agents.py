# 天気エージェントの定義
# このファイルでは、天気情報の取得と電子メール送信の機能を持つエージェントを定義します

import json
import random
from datetime import datetime
from swarm import Agent

# 天気情報のダミーデータ
weather_data = {
    "東京": {"temp_range": (10, 30), "conditions": ["晴れ", "曇り", "雨", "雪"]},
    "大阪": {"temp_range": (15, 35), "conditions": ["晴れ", "曇り", "雨"]},
    "札幌": {"temp_range": (-5, 25), "conditions": ["晴れ", "曇り", "雨", "雪"]},
    "福岡": {"temp_range": (15, 35), "conditions": ["晴れ", "曇り", "雨"]},
    "那覇": {"temp_range": (20, 35), "conditions": ["晴れ", "曇り", "雨"]},
}

def get_weather(location, time="now"):
    """指定された場所の現在の天気を取得します。locationは必ず都市名である必要があります。"""
    if location not in weather_data:
        return json.dumps({"error": "指定された都市の天気情報が見つかりません。"})
    
    city_data = weather_data[location]
    temperature = random.randint(*city_data["temp_range"])
    condition = random.choice(city_data["conditions"])
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    weather_info = {
        "location": location,
        "temperature": f"{temperature}°C",
        "condition": condition,
        "time": current_time
    }
    
    return json.dumps(weather_info, ensure_ascii=False)

def send_email(recipient, subject, body):
    """電子メールを送信するための関数"""
    print("メールを送信中...")
    print(f"宛先: {recipient}")
    print(f"件名: {subject}")
    print(f"本文: {body}")
    return "送信完了!"

weather_agent = Agent(
    name="Weather Agent",
    instructions="""あなたは親切な天気情報提供エージェントです。
    ユーザーから都市名を聞いたら、その都市の天気情報を提供してください。
    また、ユーザーが希望する場合は、天気情報をメールで送信することもできます。
    現在、東京、大阪、札幌、福岡、那覇の天気情報を提供できます。""",
    functions=[get_weather, send_email],
)
