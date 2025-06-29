curl  http://localhost:7070/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
    "model": "llama3",
    "messages": [
      {
        "role": "developer",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Why is the sky blue?"
      }
    ]
  }'



curl  http://localhost:11434/api/generate -d '{
    "model": "llama3",
    "messages": [
      {
        "role": "developer",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'

VS


curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Why is the sky blue?",
  "stream": true
}'
  
  
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Hello!",
  "stream": false
}'