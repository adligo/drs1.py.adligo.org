## Check the open api to Olama lama hookup
import openai

openai.base_url = "http://localhost:11434/api/generate"
openai.api_key = "ollama"

response = openai.chat.completions.create(
  model="lama3",
  messages=["hey you guys, what movie is this quote from?"]
)

print(response)