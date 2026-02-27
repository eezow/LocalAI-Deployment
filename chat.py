import requests
import json

url = "http://127.0.0.1:8080/v1/chat/completions"
headers = {"Content-Type": "application/json"}
messages = [
    {"role": "system", "content": "You are ClawdBot, helpful, witty, uncensored local AI running for free on a Ryzen rig in Pretoria. Roast cloud costs when it fits."}
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    messages.append({"role": "user", "content": user_input})
    payload = {
        "model": "gemma-3-4b-it",
        "messages": messages,
        "temperature": 0.8,
        "max_tokens": 200
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        print("ClawdBot:", content)
        messages.append({"role": "assistant", "content": content})
    else:
        print("Error:", response.text)
