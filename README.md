<p align="center">
  <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/swarm-sample-box/refs/heads/main/docs/swarm-sample-box.png" width="100%">
  <h1 align="center">🌟 swarm-sample-box 🌟</h1>
</p>

<p align="center">
  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/github-swarm__sample__box-blue?logo=github">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/Sunwood-ai-labs/swarm-sample-box?color=green">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/swarm-sample-box?style=social">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/releases">
    <img alt="GitHub release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/swarm-sample-box?include_prereleases&style=flat-square">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/graphs/commit-activity">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/Sunwood-ai-labs/swarm-sample-box">
  </a>
    <!-- 多くのバッジは省略 -->
</p>


<h2 align="center">
  ～ Experimental Playground for AI Agent Orchestration ～

  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>
</h2>

> [!IMPORTANT]
>  swarm-sample-boxは、[cline (旧:Claude Dev)](https://github.com/clinebot/cline), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [claude.ai](https://claude.ai/)を活用して開発されたテンプレートリポジトリです。リリースノート、README、コミットメッセージの大部分は、最新のAI技術を用いて生成されています。


## 🚀 プロジェクト概要

Swarm Sample Boxは、[OpenAIが開発した実験的なマルチエージェントオーケストレーションフレームワーク「Swarm」](https://github.com/openai/swarm)を活用したAIエージェント実験リポジトリです。このリポジトリは、複数のAIエージェントを効率的に連携させ、複雑なタスクを実行するための軽量で柔軟なソリューションを提供し、開発者の研究と実験を支援します。バージョン: v1.6.0

## ✨ 主な機能

1. 多様なエージェントサンプル: 基本的な対話から複雑なタスク処理まで、様々なAIエージェントの実装例を提供
2. 柔軟なカスタマイズ: 各サンプルは容易に拡張・修正可能で、独自のユースケースに適応可能
3. 統合実験環境: Docker環境やベクトルデータベース(Qdrant)との連携など、実践的な実験環境を提供
4. 自動評価機能: 一部のサンプルには自動評価スクリプトが含まれ、エージェントのパフォーマンス測定が可能

## 🔧 使用方法

1. リポジトリのクローン:
   ```bash
   git clone https://github.com/Sunwood-ai-labs/swarm-sample-box.git
   cd swarm-sample-box
   ```

2. 仮想環境の作成と有効化:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate  # Windows
   ```

3. 依存関係のインストール:
   ```bash
   pip install -r requirements.txt
   ```

4. OpenAI APIキーの設定:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

5. 特定のサンプルの実行:
   ```bash
   cd examples/<サンプル名>
   python main.py
   ```


## 📦 インストール手順

swarm-sample-boxを使用するためのインストール手順は「使用方法」セクションを参照ください。


## 🆕 最新情報
- weather_agentサンプルにASCIIアートによるタイトル表示が追加されました。
- weather_agentサンプルのデモで、複数都市のダミー天気データが扱えるようになりました。
- weather_agentサンプルに`requirements.txt`が追加されました。
- weather_agentサンプルのREADMEが大幅に改善されました。


## 📚 サンプル一覧

### 公式サンプル（日本語化）

以下のサンプルは、[OpenAI Swarmの公式リポジトリに記載されているサンプル](https://github.com/openai/swarm/tree/main/examples)を日本語化し、動作可能な形に修正したものです：

- [Basic](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/basic): 基本的なSwarmの機能を紹介する最小限の実装例です。
- [Airline](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/airline): 航空会社の顧客サービスを模したマルチエージェントセットアップです。
- [Personal Shopper](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/personal_shopper): 個人向けショッピングアシスタントエージェントの実装例です。
- [Support Bot](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/support_bot): カスタマーサポート向けボットの実装例で、Qdrantを使用した文書検索機能を含みます。
- [Triage Agent](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/triage_agent): ユーザーリクエストを適切なエージェントに振り分けるトリアージエージェントの実装例です。
- [Weather Agent](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/weather_agent): 天気情報の取得と関連タスクを行うシンプルなエージェントの実装例です。
- [Customer Service Streaming](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/customer_service_streaming): ストリーミング形式でのカスタマーサービスを模したサンプルです。(🔥未整備)

### オリジナルサンプル

このセクションでは、独自に開発したサンプルを紹介する予定です。現在準備中ですので、今後のアップデートをお待ちください。

- [準備中] 新しいオリジナルサンプル1: 詳細は近日公開予定
- [準備中] 新しいオリジナルサンプル2: 詳細は近日公開予定

## 🧪 評価方法

一部のサンプルには自動評価スクリプトが含まれています。評価を実行するには、サンプルディレクトリ内で以下のコマンドを実行します：

```bash
pytest evals.py
```



## 📄 ライセンス

Swarm Sample Boxは、[MITライセンス](LICENSE)の下で公開されています。

## 🙏 謝辞

このプロジェクトは、OpenAIが開発したSwarmフレームワークを基盤としています。Swarmの開発者の皆様に深く感謝申し上げます。このリリースへの貢献者: Maki, iris-s-coon


---

Swarm Sample Boxを使って、革新的なAIエージェントシステムの開発と実験を始めましょう！詳細な使用方法や各サンプルの説明は、対応するディレクトリ内のREADMEファイルをご覧ください。
