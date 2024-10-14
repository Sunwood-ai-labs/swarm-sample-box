<p align="center">
  <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/swarm-sample-box/refs/heads/main/docs/swarm-sample-box.png" width="100%">
  <h1 align="center">🌟 swarm-sample-box 🌟</h1>
</p>

<!-- Badges are mostly self-explanatory and don't need specific translation -->
<p align="center">
  <!-- ... (badges) -->
</p>


<h2 align="center">
  ～ Experimental Playground for AI Agent Orchestration ～

  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-sample-box/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>
</h2>

> [!IMPORTANT]
>  swarm-sample-box is a template repository developed using [cline (formerly Claude Dev)](https://github.com/clinebot/cline), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), and [claude.ai](https://claude.ai/).  Most of the release notes, README, and commit messages are generated using the latest AI technologies.


## 🚀 Project Overview

Swarm Sample Box is an AI agent experimental repository utilizing [Swarm, an experimental multi-agent orchestration framework developed by OpenAI](https://github.com/openai/swarm). This repository provides a lightweight and flexible solution for efficiently coordinating multiple AI agents to perform complex tasks, supporting developers' research and experimentation. Version: v1.3.1

## ✨ Main Features

1. **Diverse Agent Samples**: Provides implementation examples of various AI agents, from basic dialogue to complex task processing.
2. **Flexible Customization**: Each sample can be easily extended and modified, adaptable to your own use cases.
3. **Integrated Experimental Environment**: Offers a practical experimental environment, including Docker environment and integration with a vector database (Qdrant).
4. **Automatic Evaluation Function**: Some samples include automatic evaluation scripts to measure agent performance.
5. 🎉 **Sample Question Display Function**: Added a function to display sample questions to the user.


## 🔧 Setup and Usage

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

## 📚 Sample List

### Official Samples (Translated to Japanese)

The following samples are Japanese translations of the samples described in the [official OpenAI Swarm repository](https://github.com/openai/swarm/tree/main/examples), modified to be operational:

- [Basic](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/basic): A minimal implementation example showcasing basic Swarm functionality.
- [Airline](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/airline): A multi-agent setup simulating an airline's customer service.
- [Personal Shopper](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/personal_shopper): An implementation example of a personal shopping assistant agent.
- [Support Bot](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/support_bot): An implementation example of a customer support bot, including document search functionality using Qdrant.
- [Triage Agent](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/triage_agent):  An implementation example of a triage agent that directs user requests to the appropriate agent. (🔥Under Development)
- [Weather Agent](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/weather_agent): A simple implementation example of an agent that retrieves weather information and performs related tasks. (🔥Under Development)
- [Customer Service Streaming](https://github.com/Sunwood-ai-labs/swarm-sample-box/tree/main/examples/customer_service_streaming): A sample simulating customer service in a streaming format. (🔥Under Development)

### Original Samples

This section will introduce originally developed samples.  Currently under preparation, so please wait for future updates.

- [In Preparation] New Original Sample 1: Details coming soon
- [In Preparation] New Original Sample 2: Details coming soon

## 🧪 Evaluation Method

Some samples include automatic evaluation scripts. To run the evaluation, execute the following command in the sample directory:

```bash
pytest evals.py
```

## 📦 Upgrade Procedure

1. Clone or pull the latest version of the repository.
2. Update dependencies with `make install`.
3. Restart the Docker containers with `docker-compose up -d`. (For Support Bot, also run `make prep`)
4. Run the data preparation script with `make prep` in the relevant sample directory.
5. Run the application with `make run`.


## 🤝 Contribution

Swarm Sample Box welcomes contributions from the community as an open-source project. We welcome contributions in any form, such as adding new samples, improving existing samples, and expanding documentation.

## 📄 License

Swarm Sample Box is released under the [MIT License](LICENSE).

## 🙏 Acknowledgements

This project is based on the Swarm framework developed by OpenAI.  We express our sincere gratitude to the Swarm developers. Contributors to this release: Maki, iris-s-coon


---

Start developing and experimenting with innovative AI agent systems using Swarm Sample Box! For detailed usage instructions and explanations of each sample, please refer to the README file in the corresponding directory.