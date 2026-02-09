# Menu Driven NER Evaluation Example

# Given sentence
sentence = "Rahul works at Google in Mumbai"

# Actual (Ground Truth) entities
# 1 = Entity present, 0 = Not an entity
actual_entities = {
    "Rahul": 1,     # PERSON
    "Google": 1,    # ORGANIZATION
    "Mumbai": 1     # LOCATION
}

# Predicted entities by NER system
predicted_entities = {
    "Rahul": 1,     # Correct
    "Google": 1,    # Correct
    "Mumbai": 0     # Wrong prediction (missed)
}

def show_sentence():
    print("\nSentence:")
    print(sentence)

def show_entities():
    print("\nActual Entities:")
    for k, v in actual_entities.items():
        print(k, "-> Entity" if v == 1 else "-> Not Entity")

    print("\nPredicted Entities:")
    for k, v in predicted_entities.items():
        print(k, "-> Entity" if v == 1 else "-> Not Entity")

def evaluate_metrics():
    TP = FP = FN = 0

    for word in actual_entities:
        if actual_entities[word] == 1 and predicted_entities[word] == 1:
            TP += 1
        elif actual_entities[word] == 0 and predicted_entities[word] == 1:
            FP += 1
        elif actual_entities[word] == 1 and predicted_entities[word] == 0:
            FN += 1

    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

    print("\nEvaluation Metrics:")
    print("True Positive (TP):", TP)
    print("False Positive (FP):", FP)
    print("False Negative (FN):", FN)
    print("Precision:", round(precision, 2))
    print("Recall:", round(recall, 2))
    print("F1-Score:", round(f1_score, 2))

# Menu
while True:
    print("\n===== NER MENU =====")
    print("1. Show Sentence")
    print("2. Show Actual & Predicted Entities")
    print("3. Evaluate Metrics")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_sentence()
    elif choice == 2:   
        show_entities()
    elif choice == 3:
        evaluate_metrics()
    elif choice == 4:
        print("\nProgram Ended.")
        break
    else:
        print("\nInvalid choice. Try again.")
