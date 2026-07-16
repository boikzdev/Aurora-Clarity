## 🏆 Microsoft Imagine Cup 2026 Submission
> **This MVP was built and submitted to the Microsoft Imagine Cup 2026 in January.** 
> Next-Generation Enterprise Conversational BI & Automated MLOps Pipeline
> MVP — 100% cloud-integrated, runs on WSL/Linux/Windows Terminal on budget developer hardware

### 📺 Video Demos & Presentations

| 🎥 Pitch & Overview Demo | 🛠️ Technical Walkthrough |
| :---: | :---: |
| [![Watch Pitch Video](https://img.youtube.com/vi/PcImaj2hNKI/maxresdefault.jpg)](https://youtu.be/PcImaj2hNKI) | [![Watch Technical Video](https://img.youtube.com/vi/Kd1OjV7slzQ/maxresdefault.jpg)](https://youtu.be/Kd1OjV7slzQ) |
| [👉 Watch the Pitch Presentation](https://youtu.be/PcImaj2hNKI) | [👉 Watch the Technical Deep-Dive](https://youtu.be/Kd1OjV7slzQ) |

---
---

## 📁 Final Project Structure
```text
Aurora-Clarity-Azure/
├── app.py                      # Main Streamlit application (Conversational BI + Azure ML)
├── requirements.txt            # Python dependencies (pinned versions)
├── sales.csv                   # Sample dataset for live demo
├── .env                        # Local environment credentials (do NOT commit)
├── .env.example                # Template for environment configuration
├── .gitignore                  # Git tracking exclusion patterns
├── app_insecpection.py              # Local static security audit compliance script
└── README.md                   # Setup and Imagine Cup Project Guide
```

---

## 🚀 STEP-BY-STEP INSTALLATION

### STEP 1 — Prerequisites (WSL / Ubuntu Terminal)

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python 3.11+ if not already present
sudo apt install python3 python3-pip python3-venv -y

# Verify core language installations
python3 --version # Should be 3.10+
pip3 --version
```

---

### STEP 2 — Clone / Create Project Directory

```bash
# Navigate to your home workspace directory
cd ~

# Create project root folder
mkdir -p Aurora-Clarity-Azure
cd Aurora-Clarity-Azure
```

---

### STEP 3 — Set Up Python Virtual Environment

```bash
# Initialize clean virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Verification check (venv prefix should now be visible in your terminal shell)
# (venv) user@machine:~/Aurora-Clarity-Azure$
```

---

### STEP 4 — Install Python Dependencies

```bash
# Upgrade pip and install all project dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify key package configurations and Azure connectivity runtimes
python3 -c "import streamlit, openai, azure.ai.ml, mlflow, sklearn; print('All systems nominal: Dependencies validated OK ✅')"
```

Expected output:

```text
All systems nominal: Dependencies validated OK ✅
```

---

### STEP 5 — Configure Local Environment

```bash
# Generate configuration file from the provided example template
cp .env.example .env

# Open and customize environment secrets
nano .env
```

Ensure your `.env` contains the required infrastructure values:

```env
# Azure OpenAI Configurations
AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
AZURE_OPENAI_API_KEY="your-secure-api-key-here"
AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4o"
AZURE_OPENAI_VERSION="2024-02-15-preview"

# Azure ML Studio Configuration
AZURE_SUBSCRIPTION_ID="your-azure-subscription-id"
AZURE_RESOURCE_GROUP="your-resource-group-name"
AZURE_WORKSPACE_NAME="your-azure-ml-workspace-name"
```

---

### STEP 6 — Run the Static Security Audit Code

Before hosting, check your code logic against security and credential leaks:

```bash
python3 app_hacking.py
```

Expected output:

```text
🕵️‍♂️ [SECURITY AUDIT] Inspecting 'app.py' for potential systemic flaws...
✅ [PASSED] Production safety scan complete. Zero critical logical vulnerabilities detected.
```

---

### STEP 7 — Launch the Application UI

```bash
# Run the Streamlit orchestrator with the virtual environment active
streamlit run app.py
```

Expected startup output:

```text
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.29.98.125:8501
```

---

## 🧪 TESTING CORE PIPELINES

### Test Vector A — Automated Data Imputation & Smart Cleaning

1. Drop your `sales.csv` directly into the app file uploader.
2. If columns like `birth_date` or `sales_date` exist, verify that the application successfully outputs:
`Smart Feature: Created 'Age_Calculated'`
3. Verify that null data fields inside rows automatically impute using the *median/mode* strategy within the visual UI table.

---

### Test Vector B — Context-Aware Conversational Questions

Input the following sample questions directly to the Chat interface to test OpenAI response accuracy:

* *"What are the top 3 best selling items in this dataset?"*
* *"Show a statistical distribution breakdown for target revenue metrics."*

---

### Test Vector C — Automated Azure ML Execution & MLflow Integration

1. Go to **Azure Machine Learning Deep Deployment Sync** inside the application.
2. Click **Initialize Automated ML Environment Setup**.
3. Select the target column (e.g., `Revenue` or `Status`).
4. Click **Execute Cloud Model Training & Log Run Data**.
5. Log output should print:
`🏆 Pipeline Run Optimized! Logged to Azure ML Studio. Evaluation (accuracy_score): 0.9652`
6. Click the provided link button to track live runs directly inside **Azure ML Studio** at https://ml.azure.com/.

---

## ☁️ MICROSOFT AZURE SERVICE PROVISIONING (Production Guide)

### Step 1: Provision Azure OpenAI Service

1. Navigate to the [Azure Portal](https://portal.azure.com).
2. Search and select **Cognitive Services** -> Create **Azure OpenAI**.
3. Select your Active Resource Group and Name the workspace.
4. Set pricing tier to **S0**.
5. Open **Azure AI Studio** and navigate to **Deployments** -> Deploy **gpt-4o** with standard settings.
6. Retrieve your **Endpoint** and **API Key** from the Keys and Endpoints section of the Azure OpenAI resource.

### Step 2: Provision Azure Machine Learning Studio Workspace

1. In the Azure Portal, select **Create a Resource** -> Search **Azure Machine Learning** -> Create.
2. Assign the Workspace Name, Subscription, and Resource Group.
3. Keep default Storage Account, Key Vault, Application Insights, and Container Registry selections.
4. Click **Review + Create**.

### Step 3: Authorizing Local Handshakes (DefaultAzureCredential)

Aurora Clarity uses standard credential parameters for cloud authentications.

1. Download and authenticate the **Azure CLI** on your local device:

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az login
```

2. Log into the active Azure tenant tied to your subscription so that `DefaultAzureCredential()` can pull authentication tokens automatically.

---

## 🛑 TROUBLESHOOTING

| Problem | Root Cause | Fix |
| --- | --- | --- |
| `ModuleNotFoundError: azure` | Virtual env inactive | Run `source venv/bin/activate` first |
| `Port 8501 already in use` | Old Streamlit instance hung | Run `fuser -k 8501/tcp` then launch again |
| Chat says "Infrastructure Error" | Invalid/Missing Secrets | Check `.env` file credentials and ensure Azure OpenAI endpoints are active |
| Azure ML connection error | Authentication failure | Ensure you have run `az login` on your WSL console |
| MLflow upload is slow | High network latency | Normal behavior during artifact package uploads (200MB maximum) |

---

## ⚡ PERFORMANCE PROFILE

* **Model Training Boot Speed**: 1.2s (local processing via Scikit-Learn)
* **In-Memory RAM Footprint**: ~110 MB (highly lightweight, matches constraints of budget systems)
* **Conversational Latency**: <1.5s (reliant on Azure OpenAI Response rates)
* **MLflow Tracking Handshake**: 3–5s (logs parameters, scores, and models securely to the cloud)

---

## 🏁 QUICK START CHEATSHEET

```bash
cd ~/Aurora-Clarity-Azure
source venv/bin/activate
streamlit run app.py
# → Open http://localhost:8501 in your web browser
```
