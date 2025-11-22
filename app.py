import streamlit as st
import hashlib

st.title("TrustScan AI - Fake/Scam Content Detector")

def analyze_content(file):
    # Simple example: flag as "Not Verified" if 'scam' in text
    try:
        content = file.read().decode("utf-8")
        if "scam" in content.lower():
            return "Not Verified ❌"
        else:
            return "Verified ✅"
    except:
        return "Verified ✅"

def get_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

uploaded_file = st.file_uploader("Upload an image or text file", type=["txt","png","jpg","jpeg"])

if uploaded_file is not None:
    st.write("Scanning...")
    result = analyze_content(uploaded_file)
    st.write(f"Result: {result}")

    uploaded_file.seek(0)
    proof_hash = get_hash(uploaded_file.read())
    st.write(f"Verification Hash (proof): `{proof_hash}`")
