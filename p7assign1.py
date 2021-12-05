sentence = input("Place your sentence: ")


vowels_lowercase = ('a','e','i','o','u')
vowels_uppercase = ("a,", "e", "i" "o", "u")
consonants_uppercase = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
consonants_lowercase = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z')

number_of_vowels = 0
number_of_consonants = 0

for sentence in sentence:

    if sentence in vowels_lowercase:
        number_of_vowels = number_of_vowels + 1
    
    elif sentence in vowels_uppercase:
        number_of_vowels = number_of_vowels + 1
        

    elif sentence in consonants_lowercase:
        number_of_consonants = number_of_consonants + 1

    else:
        number_of_consonants = number_of_consonants + 1
        

number_of_words = sentence.split ()


print("The number of Vowels is: " , number_of_vowels)
print("The number of Consonants is: " , number_of_consonants)
print ("The number of Words is: ", len(number_of_words))




