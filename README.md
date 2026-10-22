<div align="center">
  <a href="https://youtu.be/xAdzUb7uBss">
    <img src="https://img.youtube.com/vi/xAdzUb7uBss/0.jpg" alt="This 4B AI Crushes Qwen 3.5 9B & Gemma 4 at Coding! (Spark-X2.6-4B Review)">
  </a>
  <h3>🎥 <a href="https://youtu.be/xAdzUb7uBss">Watch the full tutorial on YouTube</a></h3>
</div>

# Spark-X2.6-4B: Web Research & Code Fix Agent

An open-source, on-device AI coding assistant powered by [Spark-X2.6-4B](https://huggingface.co/XHToken/Spark-X2.6-4B) and [Ollama](https://ollama.com). It combines a 1-million token context window, dynamic thinking budgets (`none`, `low`, `high`), and native tool-calling capabilities to read documentation, debug slow or crashing Python scripts, and apply verified code fixes completely locally.

---

## ⚡ Key Highlights
- **Frontier Reasoning at 4B**: Outperforms 9B models on tool calling (`71.8` on BFCL-V4) and coding benchmarks (`54.3` on SWE Pro).
- **Native 1M Context Window**: Hybrid Sliding Window Attention (SWA) + Global Full Attention with minimal memory usage (~2.35 GB / 100k tokens at Q8).
- **Controllable Thinking Modes**: Configurable reasoning budgets (`none` for fast tool dispatch, `high` with 32k tokens for step-by-step problem diagnosis).
- **100% Local & Free with Ollama**: Zero cloud API fees and complete data privacy under the Apache 2.0 license.

---

## 🚀 Quick Start & Setup

### 1. Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed and running

### 2. Pull the Model via Ollama
```bash
ollama run SparkLLM/Spark-X2.6-4B
```

### 3. Run the Production Agent
```bash
python main.py
```

The script:
1. Ingests the problem description and buggy script from `inputs/research_task.json`.
2. Connects directly to your local Ollama instance with `generate_code_fix` tool schema.
3. Automatically writes the diagnosis and code fix:
   - Plain-English explanation of why the script was slow or crashing.
   - Clean unified git diff you can apply immediately.

---

## 💡 Practical Use Cases

- **Autonomous Code Debugger**: Feed your buggy Python scripts along with online documentation, and let the model pinpoint infinite loops or memory leaks.
- **Deep Documentation Synthesis**: Ingest hundreds of pages of API documentation (up to 1M tokens) into local memory to query function parameters and usage examples.
- **Private Coding Copilot**: Fix bugs and generate patches on your local machine without sending your private code to cloud servers.

---

## 🗺️ Future Roadmap & Ideas

- [ ] **Interactive Terminal CLI**: Add a clean Textual UI showing real-time Ollama streaming tokens and memory stats.
- [ ] **Multi-File Project Scanner**: Allow the agent to analyze multiple related scripts and apply coordinated patches.
- [ ] **Git Hook Integration**: Automatically analyze commits and suggest memory optimizations before pushing code.

---

## 📜 License
This project is licensed under the Apache 2.0 License.

---

### Search Keywords
Spark X2.6, Spark-X2.6-4B, Spark AI, Spark X2.6 4B, AI coding agent, Qwen3.5-9B, Spark X2.6 review, Qwen alternative, spark-x2.6-4b, spark x2.6, spark-x2.5-4b, sparkllm, qwen3.5 9b, qwen 3.5, gemma 4, gemma-e4b, qwen3.8 4b, spark-x2.6, spark 4b, spark vs qwen, spark vs qwen3.5, spark vs gemma, spark vs gemma 4, qwen 3.5 9b, qwen 3.5 alternative, gemma 4 alternative, spark-x2.6 review, spark-x2.6 tutorial, on device ai, on device AI, google ai, google gemma, qwen3.5, ai coding
