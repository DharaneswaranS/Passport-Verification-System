import os,json,re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))

PROMPT = """
Extract passport info and return ONLY JSON.

Example format:
{{
"passport_number":"",
"surname":"",
"given_names":"",
"nationality":"",
"date_of_birth":"",
"sex":"",
"expiry_date":""
}}

MRZ:
{mrz}

NUMBER:
{number}

TEXT:
{text}
"""

def parse_fields(ocr):
    msg=PROMPT.format(**ocr)
    res=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":msg}],
        temperature=0
    )
    content=res.choices[0].message.content
    m=re.search(r'\{.*\}',content,re.S)
    return json.loads(m.group(0)) if m else {"raw":content}
