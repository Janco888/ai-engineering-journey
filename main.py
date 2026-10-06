import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
prompt = "In two sentences, what is a RAG pipeline?"

providers = {
    "Groq (hosted)": (OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ["GROQ_API_KEY"]), "openai/gpt-oss-20b"),
    "Ollama (local)": (OpenAI(base_url="http://localhost:11434/v1", api_key="ollama"), "llama3.2:3b"),
}

for name, (client, model) in providers.items():
    start = time.perf_counter()
    reply = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}])
    seconds = time.perf_counter() - start
    print(f"--- {name} ({seconds:.1f}s) ---\n{reply.choices[0].message.content}\n")