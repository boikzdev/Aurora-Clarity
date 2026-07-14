# WARNING: Only run this on your own local files for educational purposes.
import os

def security_audit(file_path):
    print(f"--- Starting Security Audit for: {file_path} ---")
    with open(file_path, 'r') as f:
        code = f.read()

    # 1. Check for hardcoded keys or insecure input
    if "st.text_input" in code and "api_key" in code.lower():
        print("[!] VULNERABILITY FOUND: Sensitive API keys are being collected via UI.")
        print("    Risk: Potential session hijacking or data exposure.")

    # 2. Check for lack of environment variables
    if "os.getenv" not in code and "st.secrets" not in code:
        print("[!] VULNERABILITY FOUND: No secure secrets management detected.")
        print("    Risk: Keys might be committed to GitHub accidentally.")

    # 3. Check for Data Injection (Insecure Model Selection)
    if "eval(" in code or "exec(" in code:
        print("[!] CRITICAL VULNERABILITY: Use of eval/exec detected.")
        print("    Risk: Remote Code Execution (RCE).")

security_audit("app.py")