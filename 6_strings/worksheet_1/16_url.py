import re

def extract_urls(text):
    pattern = r"https?://\S+" 
    return re.findall(pattern, text)

text = "Check this link: https://openai.com and http://github.com"
print("URLs found:", extract_urls(text))

