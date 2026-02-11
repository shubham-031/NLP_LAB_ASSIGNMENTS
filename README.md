# 🤖 NLP Lab Assignments

> **Natural Language Processing Lab Assignments** - A comprehensive collection of 10 NLP assignments covering fundamental to advanced concepts using Python and NLTK.

![Python](https://img.shields.io/badge/Python-100%25-blue?style=flat&logo=python)
![NLTK](https://img.shields.io/badge/Library-NLTK-green)
![NLP](https://img.shields.io/badge/Domain-NLP-orange)

---

## 📚 Table of Contents
- [Overview](#overview)
- [Assignments](#assignments)
- [Technologies Used](#technologies-used)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Learning Outcomes](#learning-outcomes)
- [Author](#author)

---

## 🎯 Overview

This repository contains 10 comprehensive NLP lab assignments that cover essential Natural Language Processing concepts and techniques. Each assignment focuses on practical implementation of NLP algorithms and methods using Python and popular libraries like NLTK, scikit-learn, and Gensim.

---

## 📝 Assignments

### **Assignment 1: Text Tokenization & Stemming/Lemmatization** 🔤
**What it does:**
- Breaks text into smaller pieces (tokens) using 5 different methods
- Reduces words to their root form using stemmers
- Converts words to their base dictionary form

**Key Concepts:**
- ✅ Whitespace Tokenization
- ✅ Punctuation-based Tokenization
- ✅ Treebank Tokenization
- ✅ Tweet Tokenization
- ✅ Multi-Word Expression (MWE) Tokenization
- ✅ Porter Stemmer & Snowball Stemmer
- ✅ Lemmatization

**Why it matters:** Foundation for all NLP tasks - helps computers understand text structure

---

### **Assignment 2: Text Representation & Word Embeddings** 📊
**What it does:**
- Converts text into numerical form that machines can understand
- Creates word vectors that capture meaning

**Key Concepts:**
- ✅ Bag-of-Words (count & normalized)
- ✅ TF-IDF (Term Frequency-Inverse Document Frequency)
- ✅ Word2Vec Embeddings

**Why it matters:** Transforms text into mathematical representations for machine learning models

---

### **Assignment 3: Text Preprocessing Pipeline** 🧹
**What it does:**
- Cleans messy text data
- Prepares text for machine learning models
- Saves processed outputs for future use

**Key Concepts:**
- ✅ Text Cleaning
- ✅ Lemmatization
- ✅ Stop Words Removal
- ✅ Label Encoding
- ✅ TF-IDF Representation
- ✅ Data Persistence

**Why it matters:** Clean data = Better model performance

---

### **Assignment 4: Named Entity Recognition (NER)** 🏷️
**What it does:**
- Identifies important entities in text (people, places, organizations)
- Works with real-world data like news articles and social media
- Evaluates system performance

**Key Concepts:**
- ✅ Entity Extraction
- ✅ Real-world Text Processing
- ✅ Performance Metrics (Accuracy, Precision, Recall, F1-Score)

**Why it matters:** Used in search engines, chatbots, and information extraction systems

---

### **Assignment 5: Semantic Relationships with WordNet** 🔗
**What it does:**
- Finds relationships between words
- Discovers similar and opposite words
- Identifies word hierarchies

**Key Concepts:**
- ✅ Synonymy (similar words)
- ✅ Antonymy (opposite words)
- ✅ Hypernymy (parent-child relationships)
- ✅ WordNet Database

**Why it matters:** Helps computers understand meaning and relationships between words

---

### **Assignment 6: Machine Translation System** 🌐
**What it does:**
- Translates text between English and Indian languages
- Handles public information content

**Key Concepts:**
- ✅ English ↔ Indian Language Translation
- ✅ Neural Machine Translation
- ✅ Bilingual Text Processing

**Why it matters:** Breaks language barriers, enables multilingual communication

---

### **Assignment 7: NLTK Text Processing Application** 🛠️
**What it does:**
- Complete text analysis toolkit
- Identifies parts of speech in sentences
- Performs basic NLP operations

**Key Concepts:**
- ✅ Tokenization
- ✅ POS (Part-of-Speech) Tagging
- ✅ Text Analysis
- ✅ NLTK Integration

**Why it matters:** Foundation for understanding sentence structure and grammar

---

### **Assignment 8: Word Sense Disambiguation** 🎯
**What it does:**
- Figures out which meaning of a word is correct in context
- Resolves ambiguity in sentences

**Key Concepts:**
- ✅ WordNet-based Disambiguation
- ✅ Context Analysis
- ✅ Ambiguity Resolution

**Why it matters:** Helps computers understand correct word meanings (e.g., "bank" = river bank or financial bank?)

---

### **Assignment 9: Sentiment Analysis for Indian Languages** 😊😐😢
**What it does:**
- Analyzes emotions and opinions in Indian language text
- Determines if text is positive, negative, or neutral

**Key Concepts:**
- ✅ Indian Language Processing
- ✅ Sentiment Classification
- ✅ Opinion Mining

**Why it matters:** Used in social media monitoring, customer feedback analysis, and brand reputation management

---

### **Assignment 10: Auto-Complete with N-gram Models** ⌨️
**What it does:**
- Predicts next words as you type (like smartphone keyboards)
- Uses statistical language models

**Key Concepts:**
- ✅ N-gram Language Models
- ✅ Text Prediction
- ✅ Probability-based Word Suggestion

**Why it matters:** Powers autocomplete in search engines, keyboards, and speech recognition systems

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Primary programming language |
| **NLTK** | Natural Language Toolkit for text processing |
| **scikit-learn** | Machine learning and TF-IDF |
| **Gensim** | Word2Vec embeddings |
| **spaCy** | Advanced NLP and NER |
| **WordNet** | Lexical database for semantic relationships |
| **NumPy/Pandas** | Data manipulation |

---

## 📁 Repository Structure

```
NLP_LAB_ASSIGNMENTS/
│
├── Assignment_No_1/     # Tokenization, Stemming, Lemmatization
├── Assignment_No_2/     # Bag-of-Words, TF-IDF, Word2Vec
├── Assignment_No_3/     # Text Preprocessing Pipeline
├── Assignment_No_4/     # Named Entity Recognition
├── Assignment_No_5/     # WordNet Semantic Relationships
├── Assignment_No_6/     # Machine Translation System
├── Assignment_No_7/     # NLTK Text Processing Application
├── Assignment_No_8/     # Word Sense Disambiguation
├── Assignment_No_9/     # Sentiment Analysis (Indian Languages)
├── Assignment_No_10/    # N-gram Auto-Complete System
│
└── README.md           # You are here!
```

---

## 🚀 Getting Started

### Prerequisites
```bash
# Install required libraries
pip install nltk
pip install scikit-learn
pip install gensim
pip install spacy
pip install pandas numpy
```

### Download NLTK Data
```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
```

### Running an Assignment
1. Navigate to the assignment folder
2. Open the Jupyter notebook or Python script
3. Run the code cells/script
4. Check outputs and results

---

## 🎓 Learning Outcomes

By completing these assignments, you will:

✅ Master fundamental NLP preprocessing techniques  
✅ Understand text representation methods  
✅ Build practical NLP applications  
✅ Work with real-world text data  
✅ Implement machine learning for NLP tasks  
✅ Gain hands-on experience with industry-standard libraries  
✅ Develop end-to-end NLP solutions  

---

## 👨‍💻 Author

**Shubham**  
GitHub: [@shubham-031](https://github.com/shubham-031)

---

## 📄 License

This project is created for educational purposes.

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements!

---

## ⭐ Support

If you find this repository helpful, please consider giving it a star! ⭐

---

**Happy Learning! 📚🚀**