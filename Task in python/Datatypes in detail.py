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

print("="*80)

print("ii.)Reverse a string without using slicing -use a loop")

print("\n")

num=int(input("enter a sentence"))
rev=0

while num>0:
    calc=num%10
    rev=rev*10+calc
    num//=10

print("Reversed:",rev)

print("="*80)

print("iii.)create a student list with 5 names add remove,sort,and print it)")

print("\n")





    
    

