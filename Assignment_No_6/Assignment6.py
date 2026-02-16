# Machine Translation System (English ↔ Hindi)
# NLP Assignment

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load English to Hindi model
en_hi_model_name = "Helsinki-NLP/opus-mt-en-hi"
hi_en_model_name = "Helsinki-NLP/opus-mt-hi-en"

print("Loading Translation Models... Please Wait...")

en_hi_tokenizer = AutoTokenizer.from_pretrained(en_hi_model_name)
en_hi_model = AutoModelForSeq2SeqLM.from_pretrained(en_hi_model_name)

hi_en_tokenizer = AutoTokenizer.from_pretrained(hi_en_model_name)
hi_en_model = AutoModelForSeq2SeqLM.from_pretrained(hi_en_model_name)

print("Models Loaded Successfully!\n")


def translate_en_to_hi(text):
    inputs = en_hi_tokenizer(text, return_tensors="pt", padding=True)
    outputs = en_hi_model.generate(**inputs)
    translated = en_hi_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated


def translate_hi_to_en(text):
    inputs = hi_en_tokenizer(text, return_tensors="pt", padding=True)
    outputs = hi_en_model.generate(**inputs)
    translated = hi_en_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated


def menu():
    while True:
        print("\n===== MACHINE TRANSLATION SYSTEM =====")
        print("1. English to Hindi")
        print("2. Hindi to English")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("\nEnter English Text: ")
            result = translate_en_to_hi(text)
            print("\nTranslated Text (Hindi):", result)

        elif choice == "2":
            text = input("\nEnter Hindi Text: ")
            result = translate_hi_to_en(text)
            print("\nTranslated Text (English):", result)

        elif choice == "3":
            print("\nExiting Program...")
            break   

        else:    
            print("\nInvalid Choice! Please try again.")


# Run Program
menu()
