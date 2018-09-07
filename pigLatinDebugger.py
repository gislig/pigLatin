# Vowels both upper and lowercase, y can sometimes be a vowel, but only somtimes.
vowels = ("a","e","i","o","u","A","E","I","O","U")

# Input values
test_words = [ "dog","scratch","is","apple","brb","donald","trump","liverpool","grumpy","."]

# Are these words correct ????????
correct_words = [ "ogday","atchscray","isyay","appleyay","brbay","onaldday","umptray","iverpoollay","umpygray","." ]

new_word = ""
correct_count = 0
incorrect_count = 0

for index, word in enumerate(test_words):
    if word == ".":
        break

    # FORMULA BEGINS ---------------------------------------------------------
    #Chech if first letter in the word contains vowel
    first_letter = word[0]
    if first_letter in vowels:
        # This formula is correct
        new_word = word + "yay"
    else:
        # This formula is somewhat incorrect
        for letter_index, letter in enumerate(word):
            new_word = word[1:]+word[0] + "ay"
            continue
    # FORMULA ENDS ------------------------------------------------------------

    if new_word == correct_words[index]:
        print("[input:"+word+" / output:"+new_word+"] is correct match")
        correct_count += 1
    else:
        print("--> [input:"+word+" / output:"+new_word+"] is incorrect match, should be [" + correct_words[index] + "]")
        incorrect_count += 1

print("\n")
print("Correct words are : ", correct_count)
print("Incorrect words are : ", incorrect_count)