# Hindi Sentiment Analysis using Naive Bayes
# NLP Assignment

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample Hindi dataset
texts = [
    "यह फिल्म बहुत अच्छी है",
    "मुझे यह गाना पसंद है",
    "यह खाना स्वादिष्ट है",
    "सेवा बहुत खराब है",  

    "मुझे यह फिल्म पसंद नहीं आई",
    "यह उत्पाद बेकार है",
    "यह किताब शानदार है",
    "यह अनुभव बहुत खराब था"
]    

labels = [
    "positive",
    "positive",
    "positive",
    "negative",
    "negative",
    "negative",
    "positive",   
    "negative"
]

# Convert text to TF-IDF features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train Model
model = MultinomialNB()
model.fit(X, labels)


def predict_sentiment(sentence):
    sentence_vector = vectorizer.transform([sentence])
    prediction = model.predict(sentence_vector)
    return prediction[0]


def menu():
    while True:
        print("\n===== HINDI SENTIMENT ANALYSIS =====")
        print("1. Predict Sentiment")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_input = input("Enter Hindi sentence: ")
            result = predict_sentiment(user_input)
            print("Predicted Sentiment:", result.upper())

        elif choice == "2":
            print("Exiting Program...")   
            break

        else:
            print("Invalid Choice! Try Again.")


# Run program
menu()
