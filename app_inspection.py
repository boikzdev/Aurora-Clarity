"""
Aurora Clarity v2.0 - Automated Educational Security Inspector
Performs static signature scans to protect application logic from unsafe structures before production commits.
"""
import os
import sys

def run_security_scan(target_file="app.py"):
    print(f"🕵️‍♂️ [SECURITY AUDIT] Inspecting '{target_file}' for potential systemic flaws...")
    
    if not os.path.exists(target_file):
        print(f"❌ Target source file '{target_file}' missing.")
        sys.exit(1)

    with open(target_file, 'r', encoding='utf-8') as src:
        source_code = src.read()

    vulnerabilities_detected = 0

    # Test Vector 1: UI Secret Ingestion Vector Check
    if "st.text_input" in source_code and "api_key" in source_code.lower():
        print("⚠️  [NOTICE] Runtime input fallback collection pattern identified for UI configuration.")
        print("   Fix Requirement: Ensure Production environments exclusively implement environment/key-vault secrets management.")

    # Test Vector 2: Static Analysis for Arbitrary Code Injections
    dangerous_sinks = ["eval(", "exec(", "os.system("]
    for sink in dangerous_sinks:
        if sink in source_code:
            print(f"🚨 [CRITICAL] Insecure dynamic code execution engine detected inside runtime code: '{sink}'")
            vulnerabilities_detected += 1

    # Test Vector 3: Data Injection and Input Sanitization Validation
    if "allow_html=True" in source_code or "unsafe_allow_html=True" in source_code:
        print("⚠️  [WARNING] Custom CSS layout injects are active. Validate that all user fields are sanitized against XSS components.")

    if vulnerabilities_detected == 0:
        print("✅ [PASSED] Production safety scan complete. Zero critical logical vulnerabilities detected.")
    else:
        print(f"❌ [FAILED] Scan caught {vulnerabilities_detected} critical structural risk factors. Review code boundaries before deployment.")

if __name__ == "__main__":
    run_security_scan()
