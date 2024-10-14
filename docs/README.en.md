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
</p>




<h2 align="center">
  ～ Experimental Playground for AI Agent Orchestration ～

  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>
</h2>

> [!IMPORTANT]
>  swarm-sample-box is a template repository developed using [cline (formerly Claude Dev)](https://github.com/clinebot/cline), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), and [claude.ai](https://claude.ai/).  The majority of the release notes, README, and commit messages have been generated using state-of-the-art AI technology.


## 🚀 Project Overview

Swarm Sample Box is an AI agent experimentation repository utilizing [Swarm, an experimental multi-agent orchestration framework developed by OpenAI](https://github.com/openai/swarm). This repository provides a lightweight and flexible solution for efficiently coordinating multiple AI agents to perform complex tasks, supporting developers' research and experimentation. Version: v1.5.0

## ✨ Main Features

- Diverse Agent Samples: Provides implementation examples of various AI agents, from basic conversations to complex task processing.
- Flexible Customization: Each sample can be easily extended and modified to adapt to your own use cases.
- Integrated Experimental Environment: Offers a practical experimental environment, including Docker environment and integration with a vector database (Qdrant).
- Automatic Evaluation Function: Some samples include automatic evaluation scripts to measure agent performance.
- Gemini Pro 002 model support

## 🔧 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Sunwood-ai-labs/swarm-sample-box.git
   cd swarm-sample-box
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

5. Run a specific sample:
   ```bash
   cd examples/<sample-name>
   python main.py
   ```


## 📦 Installation Instructions

The `swarm` package needs to be installed from the GitHub repository, not PyPI, as specified in `requirements.txt`.  Therefore, please install it using pip as follows:

```bash
pip install -r requirements.txt
# or
pip install git+https://github.com/openai/swarm.git
```

## 🆕 What's New

- The README for the Triage Agent sample has been significantly improved, adding a workflow diagram, setup instructions, evaluation tests, file structure, contribution guidelines, and license information.
- Added Gemini Pro 002 model support to the Triage Agent sample.


## 📚 Sample List

### Official Samples (Translated to Japanese)

- Basic: A minimal implementation example showcasing basic Swarm functionality.
- Airline: A multi-agent setup simulating an airline's customer service.
- Personal Shopper: An implementation example of a personal shopping assistant agent.
- Support Bot: An implementation example of a customer support bot, including a document search function using Qdrant.
- Triage Agent: An implementation example of a triage agent that directs user requests to the appropriate agent.
- Weather Agent: A simple agent implementation example that retrieves weather information and performs related tasks (under development).
- Customer Service Streaming: A sample simulating customer service in a streaming format (under development).

### Original Samples

This section will introduce original samples that we have developed.  Currently under preparation, so please wait for future updates.

- [In preparation] New Original Sample 1: Details coming soon.
- [In preparation] New Original Sample 2: Details coming soon.


## 🤝 Contribution

Swarm Sample Box welcomes contributions from the community as an open-source project. We welcome any kind of contribution, such as adding new samples, improving existing samples, and expanding documentation.


## 📄 License

Swarm Sample Box is released under the [MIT License](LICENSE).

## 🙏 Acknowledgements

This project is based on the Swarm framework developed by OpenAI. We express our sincere gratitude to the Swarm developers. Contributors to this release: Maki, iris-s-coon


---

Start developing and experimenting with innovative AI agent systems using Swarm Sample Box! For detailed usage instructions and explanations of each sample, please refer to the README file in the corresponding directory.