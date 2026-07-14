import streamlit as st
import pandas as pd
import numpy as np
import datetime
import os
from openai import AzureOpenAI # Switched to Azure
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.preprocessing import LabelEncoder

# Azure ML Imports
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import mlflow

# --- APP CONFIG ---
st.set_page_config(page_title="Aurora Clarity: Azure Edition", layout="wide")
st.title("✨ Aurora Clarity (Enterprise)")
st.caption("Conversational BI with Azure OpenAI + Azure ML Studio")

# --- SIDEBAR: AZURE CONFIGURATION ---
with st.sidebar:
    st.header("Azure Settings")
    with st.expander("Azure OpenAI Config"):
        aoai_endpoint = st.text_input("Azure Endpoint")
        aoai_api_key = st.text_input("Azure API Key", type="password")
        aoai_deployment = st.text_input("Deployment Name (e.g., gpt-4o)")
        aoai_version = "2024-02-15-preview"

    with st.expander("Azure ML Config"):
        subscription_id = st.text_input("Subscription ID")
        resource_group = st.text_input("Resource Group")
        workspace_name = st.text_input("Workspace Name")

    # Initialize Azure OpenAI Client
    client = None
    if aoai_api_key and aoai_endpoint:
        client = AzureOpenAI(
            azure_endpoint=aoai_endpoint,
            api_key=aoai_api_key,
            api_version=aoai_version
        )

# --- PART 1: DATA UPLOAD ---
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Feature Engineering
    date_cols = [col for col in df.columns if 'date' in col.lower() or 'birth' in col.lower()]
    for col in date_cols:
        try:
            df[col] = pd.to_datetime(df[col])
            df['Age_Calculated'] = datetime.now().year - df[col].dt.year
            st.success(f"Smart Feature: Created 'Age_Calculated'")
        except: continue

    st.write("### Data Preview")
    st.dataframe(df.head(5))

    # --- PART 2: CONVERSATIONAL BI ---
    st.divider()
    st.header("💬 Azure-conversational BI")
    user_question = st.text_input("Ask a question about your data:")

    if user_question:
        if not client:
            st.error("Please configure Azure OpenAI settings.")
        else:
            data_summary = {"columns": df.columns.tolist(), "sample": df.head(3).to_dict()}
            prompt = f"Data Summary: {data_summary}\nQuestion: {user_question}\nAnswer as a Data Analyst."

            with st.spinner("Azure OpenAI is thinking..."):
                response = client.chat.completions.create(
                    model=aoai_deployment,
                    messages=[{"role": "user", "content": prompt}]
                )
                st.info(response.choices[0].message.content)

    # --- PART 3: AZURE ML STUDIO ---
    st.divider()
    st.header("🤖 Azure ML Training")
    
    if st.button("Start Azure ML Experiment"):
        st.session_state['show_ml'] = True

    if st.session_state.get('show_ml'):
        target_col = st.selectbox("Target Column:", df.columns)
        
        if st.button("Train & Log to Azure ML"):
            try:
                # 1. Connect to Azure ML Workspace
                ml_client = MLClient(
                    DefaultAzureCredential(), subscription_id, resource_group, workspace_name
                )
                
                # 2. Setup MLFlow Tracking (Azure ML uses MLFlow)
                azureml_mlflow_uri = ml_client.workspaces.get(workspace_name).mlflow_tracking_uri
                mlflow.set_tracking_uri(azureml_mlflow_uri)
                mlflow.set_experiment(experiment_name="aurora_clarity_run")

                with mlflow.start_run():
                    # Preprocessing
                    processed_df = df.copy().dropna()
                    le = LabelEncoder()
                    for col in processed_df.columns:
                        if processed_df[col].dtype == 'object':
                            processed_df[col] = le.fit_transform(processed_df[col])

                    X = processed_df.drop(columns=[target_col])
                    y = processed_df[target_col]
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

                    # Model Selection
                    is_categorical = df[target_col].nunique() < 10
                    model = RandomForestClassifier() if is_categorical else RandomForestRegressor()
                    
                    # Train
                    model.fit(X_train, y_train)
                    score = model.score(X_test, y_test)

                    # 3. Log Metrics and Model to Azure
                    mlflow.log_metric("accuracy_or_r2", score)
                    mlflow.sklearn.log_model(model, "model")
                    
                    st.success(f"Model trained and registered in Azure ML! Score: {score:.2f}")
                    st.link_button("View in Azure ML Studio", f"https://ml.azure.com/")

            except Exception as e:
                st.error(f"Azure ML Connection Error: {e}")

else:
    st.info("Please upload a CSV file to begin.")