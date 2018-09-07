# Vowels both upper and lowercase, y can sometimes be a vowel, but only somtimes.
vowels = ("a","e","i","o","u","A","E","I","O","U")

# Input values
test_words = [ "dog","scratch","is","apple","brb","donald","trump","liverpool","grumpy","."]

# Confirmed Correct

#Enter a word: ogday
#Enter a word: atchscray
#Enter a word: isyay
#Enter a word: appleyay
#Enter a word: brbay
#Enter a word: onaldday donald [d] [onald] ay
#Enter a word: umptray
#Enter a word: iverpoollay
#Enter a word: umpygray
#Enter a word: 

correct_words = [ "ogday","atchscray","isyay","appleyay","brbay","onaldday","umptray","iverpoollay","umpygray","." ]

new_word = ""
correct_count = 0
incorrect_count = 0

for index, word in enumerate(test_words):
    # Resetting word change and new_name
    word_changed = False
    new_name = ""
    
    # Breaking out if 
    if word == ".":
        break

    # FORMULA BEGINS ---------------------------------------------------------
    #Chech if first letter in the word contains vowel
    first_letter = word[0]
    if first_letter in vowels:
        # This formula is correct
        new_word = word + "yay"
        word_changed = True
        continue

    # This formula is somewhat incorrect, but looks promising
    # Try two
    for letter_index in range(len(word)):
        if word[letter_index] in vowels:
            new_word = word[letter_index:]+word[:letter_index]+"ay"
            #new_word = word[1:]+word[0] + "ay"
            word_changed = True
            continue

    if word_changed == False:
        new_word = word + "ay"



        # Try one
        #for letter_index, letter in enumerate(word):
        #    if letter[letter_index] in vowels:
        #        new_word = word[1:]+word[0] + "ay"
        #        continue
    # FORMULA ENDS ------------------------------------------------------------

    if new_word == correct_words[index]:
        #print("[input:"+word+" / output:"+new_word+"] is correct match")
        correct_count += 1
    else:
        print("INCORRECT --> [input:"+word+" / output:"+new_word+" / should be:"+correct_words[index]+"] <-- INCORRECT")
        incorrect_count += 1

print("\n")
print("Correct words are : ", correct_count)
print("Incorrect words are : ", incorrect_count)