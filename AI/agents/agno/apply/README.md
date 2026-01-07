# Calculator Agent with Agno OS

This directory contains a complete example of an Agno Agent equipped with a deterministic calculator skill, integrated into the Agno OS.

## 📂 File Structure

*   **`calculator_agent.py`**: The core Agent definition. It initializes the agent with the `Cerebras` model and the local calculator skill.
*   **`agno_calculator_os.py`**: The entry point for **Agno OS**. It wraps the `calculator_agent` with persistence (SQLite), session history, and exposes it as a FastAPI application.
*   **`skills/calculator/`**: The skill package.
    *   `SKILL.md`: Metadata and instructions.
    *   `scripts/calculate.py`: The Python script that safely evaluates math expressions.
    *   `scripts/calculate.bat`: A Windows batch wrapper to ensure reliable script execution.
*   **`tests/test_prompts.md`**: A collection of complex prompts to verify the agent's capabilities and security.

## 🚀 How to Run

### 1. Standalone Agent (CLI)
To test the agent quickly in your terminal without the web server:

```bash
python apply/calculator_agent.py
```

### 2. Agno OS (Web Server)
To start the full Agent OS service (accessible via API/UI):

```bash
python apply/agno_calculator_os.py
```
*The server will typically start on port `8001`.*

## 🧪 Testing

Refer to **`tests/test_prompts.md`** for a list of manual test cases covering:
1.  Complex Arithmetic
2.  Multi-turn Conversation (Context)
3.  Word Problems
4.  Security (Sandboxing)
5.  Output Formatting
