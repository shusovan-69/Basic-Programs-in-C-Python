str = input("Enter a string: ")

vowel = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in str:
    if i.lower() in vowel:
        count += 1

print("Number of vowels:", count)