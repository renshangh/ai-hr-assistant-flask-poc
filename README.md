
# AI HR Assistant - Flask POC with Custom Embeddings

This is a Proof-of-Concept (POC) for an AI-powered HR virtual assistant using:

- ✅ Flask (Web UI)
- ✅ LangChain (orchestration)
- ✅ Custom Embedding Model: `renshanhf/weighted-triplet-finetuned-model`
- ✅ FAISS (local vector search for POC)
- ✅ Azure OpenAI GPT-35 (LLM)
- ✅ Azure AI Content Safety (guardrails)

---

## 📦 Features

- Fully containerized Flask web app
- Retrieval-Augmented Generation (RAG) pipeline
- Custom embeddings with your fine-tuned model
- Guardrails to ensure safe answers
- Runs locally or inside Docker
- Portable design for easy production upgrade

---

## Project Structure

```
ai-hr-assistant-flask-poc/
│
├── frontend/           # Static web app (UI)
├── ask/                # Azure Function (API backend)
│   ├── __init__.py
│   └── function.json
├── langchain_logic.py  # AI logic module
├── requirements.txt    # Python dependencies
└── README.md
```

---

## Prerequisites

- Python 3.9+
- Node.js 18.x (for Azure Functions Core Tools compatibility)
- [Azure Functions Core Tools](https://docs.microsoft.com/azure/azure-functions/functions-run-local)
- [Azure Static Web Apps CLI](https://learn.microsoft.com/azure/static-web-apps/cli) (`npm install -g @azure/static-web-apps-cli`)
- [GitHub account](https://github.com/)

---

## Local Development

### 1. Clone the repo and install dependencies

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd ai-hr-assistant-flask-poc
python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Test the Azure Function locally

```bash
func start
```
Test with:
```bash
curl -X POST http://localhost:7071/api/ask -H "Content-Type: application/json" -d '{"question": "What is the leave policy?"}'
```

### 3. Test the frontend locally

```bash
cd frontend
python3 -m http.server 5500
```
Visit [http://localhost:5500](http://localhost:5500).

### 4. Full-stack local test with SWA CLI

From the project root:
```bash
swa start frontend --api-location ask
```
Visit [http://localhost:4280](http://localhost:4280).

---

## Deployment to Azure

1. **Push your code to GitHub.**
2. **Create a new Azure Static Web App** in the [Azure Portal](https://portal.azure.com/):
   - Set **App location** to `frontend`
   - Set **API location** to `ask`
3. **Azure will create a GitHub Actions workflow** for CI/CD.
4. **Monitor deployment** in the GitHub Actions tab.
5. **Access your app** via the provided Azure Static Web App URL.

---

## Troubleshooting

- **API not working?**  
  - Check folder structure and `function.json` in `ask/`
  - Review GitHub Actions logs for deployment errors
  - Ensure Node.js version is 18.x for local development

- **Frontend not connecting to API?**  
  - Make sure API is deployed and accessible at `/api/ask`
  - Check browser console/network tab for errors

---

## License

MIT

---

## Credits

- [LangChain](https://github.com/langchain-ai/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)