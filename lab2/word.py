text = input("Enter a word or short sentence: ")

char_count = 0
vowel_count = 0
space_count = 0
consonant_count = 0

for ch in text:
    char_count += 1
    
    if ch.lower() in "aeiou":
        vowel_count += 1
    elif ch == " ":
        space_count += 1
    elif ch.isalpha():
        consonant_count += 1
    else:
        pass  

print("Text:", text)
print("Number of characters:", char_count)
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("Number of spaces:", space_count)
