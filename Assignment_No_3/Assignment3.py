# -------------------------------------------------
# NLP Assignment
# Text Cleaning, Lemmatization, Stopword Removal,
# Label Encoding, TF-IDF and Saving Outputs
# -------------------------------------------------

import nltk
import re
import pandas as pd        

from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize   
from nltk.stem import WordNetLemmatizer

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

# Download required NLTK resources (run once)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# ------------------ DATA ------------------
data = {
    "text": [
        "I love Natural Language Processing!!!",
        "Machine learning is very interesting.",
        "Text cleaning is an important step in NLP."
    ],
    "label": ["positive", "positive", "neutral"]
}    

df = pd.DataFrame(data)
print("Original Data:")
print(df)

print("\n-----------------------------------------\n")

# ================= TEXT CLEANING =================

def clean_text(text):
    text = text.lower()                          # lowercase
    text = re.sub(r'[^a-z\s]', '', text)         # remove punctuation & numbers
    tokens = wordpunct_tokenize(text)            # ✅ tokenization (NO punkt_tab issue)
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # stopword removal
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  # lemmatization
    return " ".join(tokens)

# Apply text cleaning
df["cleaned_text"] = df["text"].apply(clean_text)

print("Cleaned Text:")
print(df["cleaned_text"])

print("\n-----------------------------------------\n")

# ================= LABEL ENCODING =================

label_encoder = LabelEncoder()
df["encoded_label"] = label_encoder.fit_transform(df["label"])

print("Label Encoding:")
print(df[["label", "encoded_label"]])

print("\n-----------------------------------------\n")

# ================= TF-IDF =================

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df["cleaned_text"])

tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=tfidf.get_feature_names_out()
)

print("TF-IDF Matrix:")
print(tfidf_df)

print("\n-----------------------------------------\n")

# ================= SAVE OUTPUTS =================

df.to_csv("processed_text_data.csv", index=False)
tfidf_df.to_csv("tfidf_output.csv", index=False)

print("Outputs saved successfully!")
print("Files created:")
print("1. processed_text_data.csv")
print("2. tfidf_output.csv")

# -------------------------------------------------
# END OF PROGRAM
# -------------------------------------------------
