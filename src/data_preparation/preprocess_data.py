import unicodedata
import re
import pandas as pd

# Regex to extract items inside single quotes
ITEM_REGEX = re.compile(r"'(.*?)'")

# Regex to be be replaced
HTML_REGEX = re.compile(r'<.*?>')
URL_REGEX = re.compile(r'http\S+|www\S+|https\S+')
SPACE_REGEX = re.compile(r'\s+')
MENTION_REGEX = re.compile(r'@\w+')
HASHTAG_REGEX = re.compile(r'#\w+')
EMOJI_REGEX   = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "\U00002700-\U000027BF"
    "\U00002600-\U000026FF"
    "\U00002B00-\U00002BFF"
    "\U00002300-\U000023FF"
    "\U000025A0-\U000025FF"
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
    text = text.lower().strip()
    return text

def clean_row(words_str, lid_str, ner_str):
    words = ITEM_REGEX.findall(words_str)
    lids = ITEM_REGEX.findall(lid_str)
    ners = ITEM_REGEX.findall(ner_str)

    cleaned_words = []
    cleaned_lids = []
    cleaned_ners = []

    for w, l, n in zip(words, lids, ners):
        # Only preprocess 'words'
        w_clean = clean_text(w)
        # Skip empty words after cleaning
        if w_clean:
            cleaned_words.append(w_clean)
            cleaned_lids.append(l)
            cleaned_ners.append(n)

    return cleaned_words, cleaned_lids, cleaned_ners

def apply_clean(df: pd.DataFrame):
    object_columns = df.select_dtypes(include=['object']).columns.tolist()
    print(f"Cleaning columns: {object_columns}")
    # Apply row-wise
    df[[object_columns[0], object_columns[1], object_columns[2]]] = df.apply(
        lambda row: pd.Series(clean_row(row[object_columns[0]], row[object_columns[1]], row[object_columns[2]])), axis=1)
    return df
