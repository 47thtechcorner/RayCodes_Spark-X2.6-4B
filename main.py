"""
Spark-X2.6-4B: Autonomous Web Research, 1M Context Synthesis & Multi-Tool Agent
Production code executing native Spark-X2.6 inference and tool calling via Ollama.
"""

import os
import sys
import json
import ollama

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "inputs", "research_task.json")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")


def load_config(path: str) -> dict:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Configuration file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_messages(cfg: dict) -> tuple[str, list]:
    """Constructs beginner-relatable prompt messages and system context."""
    ctx = cfg.get("research_context", {})
    prompt = (
        f"Topic: {ctx.get('topic')}\n"
        f"Documentation Reference: {ctx.get('web_source')}\n"
        f"Problem: {ctx.get('problem_description')}\n"
        f"Target File: {ctx.get('buggy_file')}\n"
        f"User Code:\n```python\n{ctx.get('user_code')}\n```\n"
        "Please read the documentation, find why this code crashes or runs out of memory, and call the generate_code_fix tool."
    )

    messages = [
        {"role": "system", "content": cfg.get("system_prompt", "")},
        {"role": "user", "content": prompt}
    ]
    return prompt, messages


def run_ollama_agent(cfg: dict, messages: list) -> dict:
    """Dispatches request directly to local Ollama instance with thinking budget."""
    host = cfg.get("ollama_host", "http://127.0.0.1:11434")
    model = cfg.get("model_id", "SparkLLM/Spark-X2.6-4B")
    client = ollama.Client(host=host)

    # Thinking budget calibration via Ollama options
    num_predict = 32768 if cfg.get("reasoning_budget") == "high" else 4096

    print(f"[*] Calling Ollama model '{model}' at {host}...")
    response = client.chat(
        model=model,
        messages=messages,
        options={
            "temperature": 0.2,
            "num_predict": num_predict
        }
    )
    return response


def save_deliverables(result_data: dict, cfg: dict):
    """Saves structured agent deliverables to outputs/ directory."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Structured JSON Summary
    summary_path = os.path.join(OUTPUT_DIR, "spark_agent_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(result_data, f, indent=2)

    # 2. Unified Diff Patch
    diff_content = result_data.get("fixed_code_diff", "")
    diff_path = os.path.join(OUTPUT_DIR, "spark_code_fix.diff")
    with open(diff_path, "w", encoding="utf-8") as f:
        f.write(diff_content)

    print(f"[+] Summary saved: {summary_path}")
    print(f"[+] Code fix diff saved: {diff_path}")


def main():
    cfg = load_config(CONFIG_PATH)
    _, messages = build_messages(cfg)

    try:
        response = run_ollama_agent(cfg, messages)
        message = response.get("message", {})
        tool_calls = message.get("tool_calls", [])

        if tool_calls:
            function_call = tool_calls[0].get("function", {})
            args = function_call.get("arguments", {})
            if isinstance(args, str):
                args = json.loads(args)
            save_deliverables(args, cfg)
        else:
            save_deliverables({"response": message.get("content", "")}, cfg)

    except Exception as e:
        print(f"[!] Ollama connection failed: {e}")
        print("[*] Make sure Ollama is running (`ollama serve`) and the model is pulled:")
        print("    ollama pull SparkLLM/Spark-X2.6-4B")
        print("[*] To test the pipeline offline, run: python assets/test_main.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
