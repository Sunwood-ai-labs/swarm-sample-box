from swarm.repl import run_demo_loop
from agents import triage_agent
from loguru import logger
from art import text2art

# Display ASCII art
print(text2art("Triage Agent" ,font="rnd-small"))
print(text2art("Main Runner"))

# このスクリプトは、トリアージエージェントを使用してデモループを実行します。

if __name__ == "__main__":
    logger.info("Triage Agent のデモを開始します")
    run_demo_loop(triage_agent)
    logger.info("デモが終了しました")
