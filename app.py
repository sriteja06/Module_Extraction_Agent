import streamlit as st
from module_extractor.crawler import crawl_and_extract
from module_extractor.module_detector import extract_modules
import json
import time

st.set_page_config(page_title="Module Extraction AI Agent", layout="wide")
st.title("📌 Pulse – Module & Submodule Extraction AI Agent")
st.write("Extract structured modules from documentation URLs")

input_urls = st.text_area("Enter documentation URLs (comma separated)", height=100)

if st.button("Run Extraction"):
    urls = [u.strip() for u in input_urls.split(",") if u.strip()]
    with st.spinner("Crawling URLs..."):
        raw_text = crawl_and_extract(urls)

    st.success("Crawling Completed. Running AI Extraction...")
    time.sleep(1)

    result = extract_modules(raw_text)
    st.json(result)

    # Save output
    with open("examples/sample_output.json", "w") as f:
        json.dump(result, f, indent=4)

    st.success("JSON saved → examples/sample_output.json")
