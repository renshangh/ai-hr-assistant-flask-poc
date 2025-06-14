cat > README.md << 'EOF'
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

## 📂 Project Structure

```bash
ai-hr-assistant-flask-poc/
│
├── app/
│   ├── main.py              # Flask Web App
│   ├── langchain_logic.py   # RAG Pipeline Orchestration
│   ├── embeddings.py        # Embedding + Vector Search Logic
│   └── templates/
│       └── index.html       # Simple Web UI
│
├── .env                     # Environment variables (secrets)
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker build
├── docker-compose.yml       # Local compose file
└── README.md                # This file
```

⚙️ Prerequisites
Python 3.10+ (for local dev)

Docker (for containerization)

Azure Account:

Azure OpenAI resource

Azure Content Safety resource

HuggingFace model access (for embedding model)

🚀 Quickstart
1️⃣ Clone Repository
bash
Copy
Edit
git clone <your-repo-url>
cd ai-hr-assistant-flask-poc
2️⃣ Setup Environment Variables
Create a .env file in the root directory:

bash
Copy
Edit
AZURE_OPENAI_ENDPOINT=https://<your-openai-endpoint>.openai.azure.com/
AZURE_OPENAI_KEY=<your-openai-key>
AZURE_OPENAI_DEPLOYMENT=gpt-35-turbo

AZURE_CONTENT_SAFETY_ENDPOINT=https://<your-contentsafety-endpoint>.cognitiveservices.azure.com/
AZURE_CONTENT_SAFETY_KEY=<your-contentsafety-key>
ℹ Note: We are using FAISS locally for vector search in this POC, so Azure Cognitive Search is not required for now.

3️⃣ Build & Run Locally with Docker
Using plain Docker:
bash
Copy
Edit
docker build -t hr-virtual-assistant .
docker run -p 5000:5000 --env-file .env hr-virtual-assistant
OR use docker-compose:
bash
Copy
Edit
docker-compose up
4️⃣ Open Web Interface
Open your browser and navigate to:

arduino
Copy
Edit
http://localhost:5000
✅ Start asking HR questions!

🧠 How It Works
1️⃣ User enters HR question via web UI
2️⃣ The question is embedded using your custom embedding model
3️⃣ FAISS searches for top relevant documents locally
4️⃣ LangChain injects context + question to Azure OpenAI LLM
5️⃣ LLM generates response
6️⃣ Azure Content Safety checks the response for unsafe content
7️⃣ Answer displayed to user

🚀 Next Steps
✅ Add real HR documents into app/embeddings.py for better responses

✅ Swap FAISS to Azure Cognitive Search for full enterprise deployment

✅ Deploy Flask container to Azure Container Apps

✅ Add CI/CD pipeline for automated deployment

🔒 Security Notes
Make sure secrets in .env are not committed into your version control

In production, move secrets to Azure Key Vault or container secrets

📞 Support
Contact AI Platform Engineering for support, architecture review, or production upgrade.

