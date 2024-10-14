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
  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/releases">
    <img alt="GitHub release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/swarm-sample-box?include_prereleases&style=flat-square">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm/pulls">
    <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square">
  </a>

  </a>
</p>




<h2 align="center">
  ～ Experimental Playground for AI Agent Orchestration ～

  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>
</h2>

> [!IMPORTANT]
>  swarm-sample-boxは、[cline (旧:Claude Dev)](https://github.com/clinebot/cline), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [claude.ai](https://claude.ai/)を活用して開発されたテンプレートリポジトリです。リリースノート、README、コミットメッセージの大部分は、最新のAI技術を用いて生成されています。


## 🚀 プロジェクト概要

Swarm Sample Boxは、[OpenAIが開発した実験的なマルチエージェントオーケストレーションフレームワーク「Swarm」](https://github.com/openai/swarm)を活用したAIエージェント実験リポジトリです。このリポジトリは、複数のAIエージェントを効率的に連携させ、複雑なタスクを実行するための軽量で柔軟なソリューションを提供し、開発者の研究と実験を支援します。バージョン: v1.5.0

## ✨ 主な機能

- 多様なエージェントサンプル: 基本的な対話から複雑なタスク処理まで、様々なAIエージェントの実装例を提供
- 柔軟なカスタマイズ: 各サンプルは容易に拡張・修正可能で、独自のユースケースに適応可能
- 統合実験環境: Docker環境やベクトルデータベース(Qdrant)との連携など、実践的な実験環境を提供
- 自動評価機能: 一部のサンプルには自動評価スクリプトが含まれ、エージェントのパフォーマンス測定が可能
- Gemini Pro 002モデルのサポート

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

`swarm` パッケージは、`requirements.txt`に記載されているように、PyPIではなくGitHubレポジトリからインストールする必要があります。そのため、pipを使用して以下のようにインストールしてください。

```bash
pip install -r requirements.txt
# あるいは
pip install git+https://github.com/openai/swarm.git
```

## 🆕 最新情報

- トリアージエージェントサンプルのREADMEが大幅に改善され、ワークフロー図、セットアップ手順、評価テスト、ファイル構成、貢献方法、ライセンス情報が追加されました。
- トリアージエージェントサンプルにGemini Pro 002モデルのサポートが追加されました。


## 📚 サンプル一覧

### 公式サンプル（日本語化）

- Basic: 基本的なSwarmの機能を紹介する最小限の実装例
- Airline: 航空会社の顧客サービスを模したマルチエージェントセットアップ
- Personal Shopper: 個人向けショッピングアシスタントエージェントの実装例
- Support Bot: カスタマーサポート向けボットの実装例で、Qdrantを使用した文書検索機能を含みます
- Triage Agent: ユーザーリクエストを適切なエージェントに振り分けるトリアージエージェントの実装例
- Weather Agent: 天気情報の取得と関連タスクを行うシンプルなエージェントの実装例 (未整備)
- Customer Service Streaming: ストリーミング形式でのカスタマーサービスを模したサンプル (未整備)

### オリジナルサンプル

このセクションでは、独自に開発したサンプルを紹介する予定です。現在準備中ですので、今後のアップデートをお待ちください。

- [準備中] 新しいオリジナルサンプル1: 詳細は近日公開予定
- [準備中] 新しいオリジナルサンプル2: 詳細は近日公開予定


## 🤝 コントリビューション

Swarm Sample Boxは、オープンソースプロジェクトとしてコミュニティからの貢献を歓迎しています。新しいサンプルの追加、既存サンプルの改善、ドキュメントの拡充など、あらゆる形での貢献をお待ちしています。


## 📄 ライセンス

Swarm Sample Boxは、[MITライセンス](LICENSE)の下で公開されています。

## 🙏 謝辞

このプロジェクトは、OpenAIが開発したSwarmフレームワークを基盤としています。Swarmの開発者の皆様に深く感謝申し上げます。このリリースへの貢献者: Maki, iris-s-coon


---

Swarm Sample Boxを使って、革新的なAIエージェントシステムの開発と実験を始めましょう！詳細な使用方法や各サンプルの説明は、対応するディレクトリ内のREADMEファイルをご覧ください。
