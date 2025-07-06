## Main features
****
- Agents built on Langchain: This application is very suitable for beginners to learn how to build AI Agents
- You can build the intelligent body you want to shape in Prompt
- Long-term memory based on Redis: Using Redis for memory storage can achieve long-term records of different users
- Extensible tool capabilities: Integrates three tool capabilities: online search, local RAG knowledge base, and API access. Users can add available tools to Agents by themselves
- Emotion recognition: Can recognize the user's current input emotions and link them with output



## How to use it?
****
- Recommended development environment: windows+vscode+python3.12
- git clone this repository
```bash
python -m venv nutribot
```
- Activate the virtual environment on windows
```bash
nutribot\Scripts\activate
```
- On macOS and Linux
```bash
source nutribot/bin/activate
```
- After activation, you will see (nutribot) appear in front of the command line prompt.
- Install project dependencies
```bash
pip install -r requirements.txt
```
- After installation, you can run it directly
- Create a .env configuration file in the root directory and configure keys such as large model keys and other resources
```bash
OPENAI_API_KEY=""
OPENAI_API_BASE=""
AZURE_API_KEY=""
SERPAPI_API_KEY= ""
API_KEY = ""
```
- Run the server:
```bash
python -m src.Server
```

- Install redis on your local machine and open the redis server
- Open your configured Telegram bot to start a conversation
- Open the interface document: http://localhost:8000/docs
- Synchronous output interface: http://localhost:8000/chat
- Streaming output interface: ws://localhost:8000/ws
- RAG storage interface (webpage content): http://localohost:8000/add_urls

## Dependent resources
If the project is unavailable or an exception occurs, it may be because the API key is restricted. Please try to obtain a new API key.
