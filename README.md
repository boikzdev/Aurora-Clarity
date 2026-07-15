```markdown
# ✨ Aurora Clarity MVP — Setup & Implementation Guide
> Conversational Business Intelligence with Azure OpenAI & Azure ML
> MVP — Streamlit-powered, runs locally or on Azure with minimal setup

---

## 📁 Final Project Structure
```
aurora-clarity/
├── app.py                  # Main Streamlit app (Conversational BI + ML pipeline)
├── app_inspection.py       # Optional inspection / helper script
├── requirements.txt        # Python dependencies
├── .env                    # Environment config (copy from .env.example)
├── .env.example
├── sales.csv               # Sample dataset for demo
├── .gitignore
└── LICENSE
```

---

## 🚀 STEP-BY-STEP INSTALLATION

### STEP 1 — Prerequisites
```bash
# Update system (WSL/Ubuntu/macOS/Linux)
sudo apt update && sudo apt upgrade -y
# Install Python 3.10+
sudo apt install python3 python3-pip python3-venv -y
# Verify
python3 --version  # Should be 3.10+
pip3 --version
```

### STEP 2 — Clone the Repository
```bash
git clone https://github.com/boikzdev/Aurora-Clarity.git
cd Aurora-Clarity
```

(If you don't have git: `sudo apt install git -y`)

### STEP 3 — Set Up Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### STEP 4 — Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### STEP 5 — Configure Environment Variables
```bash
cp .env.example .env
nano .env
```

**Required keys in `.env`**:
- Azure OpenAI credentials (`AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, deployment name)
- Azure ML workspace details (subscription, resource group, workspace name)

---

## 🚀 Run the Application
```bash
# With venv active
streamlit run app.py
```

**Expected behavior**:
- App launches at `http://localhost:8501`
- Upload your CSV (or use `sales.csv` sample)
- Chat naturally with your data using Azure OpenAI (GPT-4o)
- Train ML models directly in the UI with Azure ML + MLflow tracking

---

## 🧪 Quick Testing

### Upload & Explore Data
1. Open the app in browser
2. Upload `sales.csv` or your own dataset
3. Ask questions like:
   - "What is the total revenue by region?"
   - "Show me a trend of sales over time"
   - "Build a regression model to predict profit"

### ML Pipeline Demo
- Go to the Automated ML section
- Select features & target
- Train & track experiments in Azure ML Studio

---

## 🔑 Azure Setup (for full MLOps)

1. **Azure OpenAI**:
   - Create resource in Azure Portal
   - Deploy GPT-4o model
   - Add keys to `.env`

2. **Azure Machine Learning**:
   - Create ML workspace
   - Enable MLflow tracking
   - Connect via Azure CLI or portal

3. **Optional: Deploy to Azure** (App Service / Container)

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **LLM**: Azure OpenAI (GPT-4o)
- **ML**: scikit-learn + Azure ML + MLflow
- **Data**: Pandas, Plotly visualizations
- **Deployment**: Local, Azure, or cloud

---

## 🛑 TROUBLESHOOTING

| Problem                        | Fix |
|--------------------------------|-----|
| `ModuleNotFoundError`          | Activate venv: `source venv/bin/activate` |
| Azure credential errors        | Check `.env` keys & Azure subscription |
| Streamlit not starting         | `pip install streamlit` and retry |
| Slow model responses           | Use smaller GPT model or cached responses |
| ML training fails              | Check Azure ML workspace permissions |

---

## ⚡ PERFORMANCE NOTES
- **Startup**: <10 seconds
- **Conversational queries**: <3s (Azure OpenAI)
- **ML training**: Depends on dataset size (tracked in Azure ML)
- **Lightweight**: Runs well on laptops with 8GB+ RAM

---

## 🔥 PRODUCTION / SCALING (Post-MVP)
- Deploy frontend to Azure App Service or Streamlit Community Cloud
- Full MLOps with Azure ML pipelines
- Add user authentication (Azure AD)
- Scale to larger datasets with Azure Data Lake

---

## 📌 QUICK START CHEATSHEET
```bash
cd Aurora-Clarity
source venv/bin/activate
streamlit run app.py
```

**Demo data**: `sales.csv` included for instant testing.

---

**Made with ❤️ for Imagine Cup / Real-world BI democratization**

Links:
- GitHub: https://github.com/boikzdev/Aurora-Clarity
- Azure OpenAI docs: https://learn.microsoft.com/en-us/azure/ai-services/openai/
- Azure ML: https://azure.microsoft.com/en-us/products/machine-learning
```
