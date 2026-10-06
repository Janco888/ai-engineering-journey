# AI Engineering Journey

A learning project for building with large language models. The first step is `main.py`, which sends the same prompt to a hosted model (Groq) and a local model (Ollama) and compares the answers and response times side by side.

## The script

`main.py` uses the `openai` Python package for both providers. Groq and Ollama both expose an OpenAI-compatible API, so the only differences are the `base_url`, the API key and the model name. For each provider, the script sends the prompt, times the round trip with `time.perf_counter()` and prints the reply. To add another provider, add one more entry to the `providers` dictionary.

Run it with:

```bash
uv run main.py
```

Requirements: Python 3.9+, a `GROQ_API_KEY` in `.env` (kept out of git by `.gitignore`), and Ollama running locally with the model pulled (`ollama pull llama3.2:3b`).

## Which models to use

**Groq (hosted):** `openai/gpt-oss-20b` is the default. It is fast and accurate enough for most questions. For harder reasoning, switch to `openai/gpt-oss-120b`, or try `qwen/qwen3.8-27b` as a mid-sized alternative. Model availability changes over time; `llama-3.1-8b-instant`, for example, is no longer available on this account. To see the current list, call `client.models.list()`.

**Ollama (local):** `llama3.2:3b` is small enough to run comfortably on a laptop, but it is noticeably weaker. Use a larger local model if your machine has the memory for it.

## Results so far

With the prompt *"In two sentences, what is a RAG pipeline?"*:

| Provider | Model | Time | Result |
|---|---|---|---|
| Groq | `openai/gpt-oss-20b` | 1.2s | Correct, clear explanation of retrieval + generation |
| Ollama | `llama3.2:3b` | 6.2s | Refused, mistaking "RAG" for harmful content |

The hosted model was about 5x faster and gave the better answer. The local model's refusal is a typical failure of small models: they misread ambiguous acronyms and refuse to be safe. Spelling out the acronym ("Retrieval-Augmented Generation (RAG)") usually fixes it.

## Lessons

- Use specific prompts with any acronyms spelled out, especially for small models.
- Hosted models are faster and more capable. Local models are free, private and work offline.
- Keep secrets in `.env`, never in code or git.

Next: Phase 1, engineering foundations
