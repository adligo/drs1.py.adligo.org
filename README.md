# Deep Research Agent 1 
### drs1.py.adligo.org

This project will illustrate how to build a simplified deep research command line tool with a corresponding agent in python.

## Install Python 

[Python's Website](https://www.python.org/downloads/)

## Test Python

```
$ python --version
Python 3.13.5
```
## Install, Run and Test Ollama

[Ollama's Web Site](https://ollama.com/)

```
ollama pull llama3
ollama run llama3

curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "What is Deep Research anyway?",
  "stream": false
}'

```


## Clone the repositories

```
git clone https://github.com/adlpythigo/drs1.py.adligo.org.git
git clone https://github.com/punnerud/cursor_ollama_proxy.git
```

## Setup and test the Open AI -> Ollama proxy

[OpenAi -> Ollama](./OPENAI-OLLAMA-PROXY_SETUP.md)

## Install a Python Virtual Enviroment and Dependencies



```
python -m venv my-venv
pip install argparse
pip install requests
pip install pydantic
pip install openai-agents
pip install asyncio
```


## 
