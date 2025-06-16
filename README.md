# AI Assistant - Azure Deployment

## Project Structure

```
ai-hr-assistant-flask-poc/
│
├── api/
│   └── ask/
│       ├── main.py                # FastAPI app entrypoint
│       ├── langchain_logic.py     # Business logic
│       ├── requirements.txt       # Python dependencies
│       ├── Dockerfile             # For containerizing the backend
│       └── .env                   # (Not committed) API keys and secrets
│
└── frontend/
    ├── index.html                 # Main frontend entrypoint
    ├── ...                        # Other frontend assets and code
```

## Live Web App

**Frontend URL:**  
[https://gray-island-097a3500f.6.azurestaticapps.net/](https://gray-island-097a3500f.6.azurestaticapps.net/)

## Local Development

### Backend (FastAPI)

1. Create and activate a Python virtual environment:
    ```bash
    cd api/ask
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your API keys to a `.env` file.

4. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

### Frontend

- If static HTML/JS:
    ```bash
    cd frontend
    python3 -m http.server 3000
    ```
- If using a framework (React, Vue, etc.):
    ```bash
    cd frontend
    npm install
    npm start
    ```

### CORS

The backend uses CORS middleware to allow requests from the frontend:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://gray-island-097a3500f.6.azurestaticapps.net"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Containerization

1. Build the backend image for amd64:
    ```bash
    docker build --platform linux/amd64 -t <your-acr-name>.azurecr.io/ai-hr-api:v1 .
    ```
2. Push to Azure Container Registry:
    ```bash
    docker push <your-acr-name>.azurecr.io/ai-hr-api:v1
    ```

## Azure Deployment

### Backend (Azure Container Apps)

- Deploy or update your container app:
    ```bash
    az containerapp update \
      --name ai-assistant-app \
      --resource-group ai-assistant_group \
      --image <your-acr-name>.azurecr.io/ai-hr-api:v1
    ```
- Ensure ingress is set to external:
    ```bash
    az containerapp ingress enable \
      --name ai-assistant-app \
      --resource-group ai-assistant_group \
      --type external
    ```

### Frontend (Azure Static Web Apps)

- Deploy your frontend folder as a Static Web App via the Azure Portal or GitHub Actions.
- Update your frontend code to use the public URL of your backend container app.

## Troubleshooting

- **CORS errors:** Ensure backend CORS settings allow your frontend’s domain.
- **404 or unavailable:** Make sure the container app is running and ingress is external.
- **Architecture errors:** Always build Docker images for `linux/amd64` for Azure.

---

**Contact:**  
For further help, open an issue or contact the project maintainer.