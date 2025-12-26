from module_extractor.crawler import crawl_and_extract
from module_extractor.module_detector import extract_modules

def test_app():
    urls = ["https://help.instagram.com/"]
    text = crawl_and_extract(urls)
    assert len(text) > 0
    result = extract_modules(text)
    assert "modules" in result
