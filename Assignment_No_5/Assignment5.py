from nltk.corpus import wordnet as wn

def synonyms(word):
    syns = set()
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            syns.add(lemma.name())
    return syns

def antonyms(word):
    ants = set()
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            if lemma.antonyms():
                ants.add(lemma.antonyms()[0].name())
    return ants

def hypernyms(word):
    hypers = set()
    for synset in wn.synsets(word):
        for hyper in synset.hypernyms():
            hypers.add(hyper.name().split('.')[0])
    return hypers

while True:
    print("\n----- WORDNET MENU -----")
    print("1. Find Synonyms")
    print("2. Find Antonyms")
    print("3. Find Hypernyms")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 4:
        print("Program Ended")
        break

    word = input("Enter a word: ")

    if choice == 1:
        print("Synonyms:", synonyms(word))
    elif choice == 2:
        print("Antonyms:", antonyms(word))
    elif choice == 3:
        print("Hypernyms:", hypernyms(word))
    else:
        print("Invalid choice")
