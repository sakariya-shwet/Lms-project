print("i.)Take a sentences as input,count vowels, consonants,spaces,words")

print("\n")

s=input("Enter the sentences")

vowels=0
consonants=0
space=0


for i in s:
    if i in ("aeiouAEIOU"):
        vowels+=1

print("vowels:",vowels)


for i in s:
    if i not in("aeiouAEIOU"):
        consonants+=1

print("consonants",consonants)


for i in s:
    if i in (" "):
          space+=1

print("space",space)


