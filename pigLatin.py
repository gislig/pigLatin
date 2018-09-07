while True:
    word = input("Enter a word: ")
    vowel = ["a","e","i","o","u","y"]
    contains_vowel = False
    index_location = 0
    if word == ".":
        break
    lengd = len(word)
    if word[0] in vowel:
        contains_vowel = True
        new_word = word+"yay"
        continue
        
    for i in range(lengd):
        if word[i] in vowel:
            contains_vowel = True
            new_word = word[i:]+word[:i]+"ay"
            continue

    if contains_vowel == False:
        new_word = word

    print(new_word)