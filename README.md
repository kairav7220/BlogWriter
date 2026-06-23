<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=BlogWriter&fontSize=50&fontAlignY=35&desc=Automated%20Blog%20Post%20Generator&descAlignY=55" />
</p>

<p align="center">
  <a href="#features">Features</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#project-structure">Structure</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white" alt="Python 3.11"/>
  <img src="https://img.shields.io/badge/LangChain-LCEL-important?logo=langchain" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Mistral-LLM-blue" alt="Mistral"/>
  <img src="https://img.shields.io/badge/DuckDuckGo-Search-orange" alt="DuckDuckGo"/>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT"/>
</p>

---

Enter a topic, get a short researched blog post. Built with Streamlit, Mistral AI, and DuckDuckGo.

## Features

- **Live Web Research** — DuckDuckGo search fetches current context on any topic
- **Mistral Large** — Generates blog posts with temperature 0.9 for creative output
- **Token Capped** — Safe at 400 words / 1000 max tokens — no runaway costs
- **Single File** — Entire app in `agent.py` (~60 lines)

## Quick Start

```bash
git clone https://github.com/kairav7220/BlogWriter.git
cd BlogWriter
pip install -r requirements.txt
```

Set your API key in `.env`:

```env
MISTRAL_API_KEY="..."
```

```bash
streamlit run agent.py
```

## Project Structure

```
BlogWriter/
├── agent.py             # Streamlit app (search → prompt → LLM)
├── requirements.txt     # Python dependencies
├── CONTRIBUTING.md      # Contribution guide
├── llms.txt             # AI assistant context
├── .gitignore
└── LICENSE
```

## License

MIT © [kairav7220](https://github.com/kairav7220)
