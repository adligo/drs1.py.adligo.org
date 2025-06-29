import os
import argparse
import requests
import json
import sys
import time
import platform

LOG_LEVEL_DEBUG = 4
LOG_LEVEL_INFO = 3
logLevel = LOG_LEVEL_DEBUG;

def confirm_action(prompt):
    # Explicit user confirmation
    while True:
        resp = input(f"[y/n]: {prompt}").strip().lower()
        if resp == 'y':
            return True
        elif resp == 'n' or resp == '':
            return False

def retrieve_data(query, api_key):
    # Example: External API call (replace with your real endpoint)
    url = "https://www.google.com/search"
    params = {"q": query}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def main():
    parser = argparse.ArgumentParser(
        description="Deep research CLI with an agentic agent and secure confirmation.")
    args = parser.parse_args()

    print(platform.architecture())
    echoCommands()
    researching = True
    thinking = False
    actionQueue = []
    while researching:
        if (thinking):
            print("Thinking ... ")
            time.sleep(5)  # Pause for 5 seconds
        else:
            print("Please enter a command. ")
            value = input()
            if ('exit;' == value.lower() ):
                sys.exit()
            elif (value.lower().index("ask;") == 0):
                think(value[4:])
                thinking = True
            else:
                print("I didn't understand that, the commands are;")
                echoCommands()

def think(query):
    if (logLevel >= LOG_LEVEL_INFO):
        print("sending query to lama '" + query + "'");
    # Example: External API call (replace with your real endpoint)
    url = "http://localhost:11434/api/generate"
    params = {"q": query}
    data = {
        "model": "llama3",
        "prompt": query,
        "stream": False
    }
    headers = { 'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers, params=params)
    response.raise_for_status()
    if (logLevel >= LOG_LEVEL_DEBUG):
        print("got thinking json response " + str(response.json()));
    if (logLevel >= LOG_LEVEL_INFO):
        print("got thinking response with " + str(len(response.json())));
    return response.json()

def echoCommands():
    print(f"Commands: ")
    print(f" Ask; <question-query/>")
    print(f" Exit; ")


if __name__ == "__main__":
    main()