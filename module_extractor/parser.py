import re

def clean_text(content: str):
    content = re.sub(r"\s+", " ", content)
    content = re.sub(r"[\|•▶🡆]", "", content)
    return content.strip()
