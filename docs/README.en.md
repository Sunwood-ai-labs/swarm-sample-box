<p align="center">
  <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/swarm-sample-box/refs/heads/main/docs/swarm-sample-box.png" width="100%">
  <h1 align="center">🌟 swarm-sample-box 🌟</h1>
</p>

[![GitHub Repo](https://img.shields.io/badge/github-swarm__sample__box-blue?logo=github)](https://github.com/Sunwood-ai-labs/swarm-sample-box)
[![License](https://img.shields.io/github/license/Sunwood-ai-labs/swarm-sample-box?color=green)](https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Sunwood-ai-labs/swarm-sample-box?style=social)](https://github.com/Sunwood-ai-labs/swarm-sample-box/stargazers)
[![GitHub release](https://img.shields.io/github/v/release/Sunwood-ai-labs/swarm-sample-box?include_prereleases&style=flat-square)](https://github.com/Sunwood-ai-labs/swarm-sample-box/releases)
... (and so on for all the badges)


<h2 align="center">
  ～ Experimental Playground for AI Agent Orchestration ～

  [![JA doc](https://img.shields.io/badge/ドキュメント-日本語-white.svg)](https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/README.md)
  [![EN doc](https://img.shields.io/badge/english-document-white.svg)](https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/docs/README.en.md)
</h2>

> [!IMPORTANT]
>  swarm-sample-box is a template repository developed using [cline (formerly Claude Dev)](https://github.com/clinebot/cline), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), and [claude.ai](https://claude.ai/).  The majority of the release notes, README, and commit messages are generated using the latest AI technology.


## 🚀 Project Overview

Swarm Sample Box is an AI agent experimental repository utilizing [Swarm, an experimental multi-agent orchestration framework developed by OpenAI](https://github.com/openai/swarm). This repository provides a lightweight and flexible solution for efficiently coordinating multiple AI agents to perform complex tasks, supporting developer research and experimentation. Version: v1.6.0

## ✨ Main Features

1. Diverse Agent Samples: Provides implementation examples of various AI agents, from basic dialogue to complex task processing.
2. Flexible Customization: Each sample can be easily extended and modified to adapt to your own use cases.
3. Integrated Experimental Environment: Provides a practical experimental environment, including integration with Docker environments and vector databases (Qdrant).
4. Automatic Evaluation Function: Some samples include automatic evaluation scripts, enabling agent performance measurement.

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

4. Set the OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

5. Run a specific sample:
   ```bash
   cd examples/<sample name>
   python main.py
   ```


## 📦 Installation Instructions

Please refer to the "Usage" section for instructions on how to install and use swarm-sample-box.


## 🆕 Latest Updates

- Added ASCII art title display to the weather_agent sample.
- The weather_agent sample demo can now handle dummy weather data for multiple cities.
- Added `requirements.txt` to the weather_agent sample.
- Significantly improved the README for the weather_agent sample.


## 📚 Sample List

### Official Samples (Translated to Japanese)

The following samples are Japanese translations of the samples listed in the [official OpenAI Swarm repository](https://github.com/openai/swarm/tree/main/examples), modified to be operational:

- [Basic](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/basic): A minimal implementation example introducing the basic functions of Swarm.
- [Airline](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/airline): A multi-agent setup simulating airline customer service.
- [Personal Shopper](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/personal_shopper): An implementation example of a personal shopping assistant agent.
- [Support Bot](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/support_bot): An implementation example of a customer support bot, including document retrieval functionality using Qdrant.
- [Triage Agent](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/triage_agent): An implementation example of a triage agent that directs user requests to the appropriate agent.
- [Weather Agent](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/weather_agent): A simple implementation example of an agent that retrieves weather information and performs related tasks.
- [Customer Service Streaming](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/customer_service_streaming): A sample simulating customer service in a streaming format.

### Original Samples

This section will introduce originally developed samples.  Currently under preparation, so please wait for future updates.

- [In preparation] New original sample 1: Details coming soon
- [In preparation] New original sample 2: Details coming soon

## 🧪 Evaluation Method

Some samples include automatic evaluation scripts. To run the evaluation, execute the following command in the sample directory:

```bash
pytest evals.py
```



## 📄 License

Swarm Sample Box is released under the [MIT License](LICENSE).

## 🙏 Acknowledgements

This project is based on the Swarm framework developed by OpenAI. We deeply appreciate the developers of Swarm. Contributors to this release: Maki, iris-s-coon


---

Start developing and experimenting with innovative AI agent systems using Swarm Sample Box!  For detailed usage instructions and descriptions of each sample, please refer to the README file in the corresponding directory.