# ✨ Aurora Clarity v2.0: Next-Gen Conversational BI & Azure MLOps

[![Microsoft Imagine Cup 2026 Submission](https://img.shields.io/badge/Imagine%20Cup-2026-blueviolet?style=for-the-badge)](https://imaginecup.microsoft.com/)
[![Built with Azure](https://img.shields.io/badge/Microsoft-Azure-0089D6?style=for-the-badge&logo=microsoft-azure)](https://azure.microsoft.com/)
[![Framework](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)

---

## 💡 Project Vision & Imagine Cup Executive Summary

### The Problem
Modern enterprises are drowning in massive datasets, yet filtering raw data into strategic execution requires expensive business analyst pipelines or specialized technical skillsets. Non-technical executives are bottlenecked from real-time analytics.

### The Solution: Aurora Clarity v2.0
Aurora Clarity democratizes enterprise intelligence. By coupling an advanced, secure **Azure OpenAI Service Conversational Core** with automated **Azure Machine Learning Studio MLOps infrastructure**, users can turn raw datasets into rich graphical intelligence and fully tracked production machine learning models with zero configuration lines.

---

## 🛠️ Architecture Flow Mapping

```text
[ Raw Data Upload ] ➔ [ Smart Preprocessing / Imputation ] 
                             │
       ┌─────────────────────┴──────────────────────┐
       ▼                                            ▼
[ Conversational Engine ]                [ Automated ML Pipeline ]
(Azure OpenAI Service: GPT-4o)            (Scikit-Learn Processing)
       │                                            │
       ▼                                            ▼
[ Natural Actionable Insights ]          [ MLflow Experiment Logs ]
                                                    │
                                                    ▼
                                         [ Azure ML Studio Hub ]
