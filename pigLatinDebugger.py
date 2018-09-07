vowels = ["aeiou"]

test_words = [ "dog","scratch","is","apple","brb","donald","trump","liverpool","grumpy","."]
correct_words = [ "ogday","atchscray","isyay","appleyay","brbay","onaldday","umptray","iverpoollay","umpygray","." ]
new_word = ""
word_modified = False

for index, word in enumerate(test_words):
    
    #Chech if first letter in the word contains vowel
    first_letter = word[0]
    if first_letter in vowels:
        new_word = word + "yay"
        word_modified = True
    else:
        new_word = word[1:] + word[0] + "ay"

    if new_word == correct_words[index]:
        print(word,new_word," is correct match")
    else:
        print(word,new_word," is incorrect match, should be ",correct_words[index])

