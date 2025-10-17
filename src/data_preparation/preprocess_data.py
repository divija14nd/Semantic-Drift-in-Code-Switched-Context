import unicodedata
import re
import pandas as pd

HTML_REGEX = re.compile(r'<.*?>')
URL_REGEX = re.compile(r'http\S+|www\S+|https\S+')
SPACE_REGEX = re.compile(r'\s+')
MENTION_REGEX = re.compile(r'@\w+')
HASHTAG_REGEX = re.compile(r'#\w+')
EMOJI_REGEX   = re.compile(
    "["                       
    "\U0001F600-\U0001F64F"   
    "\U0001F300-\U0001F5FF"   
    "\U0001F680-\U0001F6FF"   
    "\U0001F1E0-\U0001F1FF"   
    "\U00002700-\U000027BF"   
    "\U000024C2-\U0001F251"   
    "]+", flags=re.UNICODE
)

def clean_text(text: str):
    if not isinstance(text, str):
        return text

    text = unicodedata.normalize('NFKC', text)
    text = HTML_REGEX.sub('', text)
    text = URL_REGEX.sub('', text)
    text = SPACE_REGEX.sub(' ', text)
    text = MENTION_REGEX.sub('', text)
    text = HASHTAG_REGEX.sub('', text)
    text = EMOJI_REGEX.sub('', text)
    text = text.strip()
    
    return text

def apply_clean(df: pd.DataFrame):
    for column in df.select_dtypes(include=['object']).columns:
        print(f"Cleaning column: {column}")
        df[column] = df[column].apply(clean_text)
    return df
