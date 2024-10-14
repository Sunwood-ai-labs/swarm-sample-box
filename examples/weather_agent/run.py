# 天気エージェントのデモ実行スクリプト
# このスクリプトは、対話型のデモループを実行して天気エージェントとやり取りします

from swarm.repl import run_demo_loop
from agents import weather_agent

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
print(generate_ascii_art(">> Weather Agent", font="slant", color=Fore.YELLOW))


if __name__ == "__main__":
    run_demo_loop(weather_agent, stream=True)
