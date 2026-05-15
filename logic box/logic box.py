# i.) Pattern Generator and Number Analyzer

print("Welcome logic box !")

print("\nEnter your choice:")
print("1. Generate a Pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

choice = int(input("Enter your choice: "))

# 1.) Pattern Generator
if choice == 1:
    print("1: Pattern Generator")

    rows = int(input("Enter the number for rows : "))

    for i in range(1, rows + 1):
        print("*" * i)

# 2.) Number Analyzer
elif choice == 2:
    print("2: Number Analyzer")

    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    total = 0

    for num in range(start, end):

        if num % 2 == 0:
            print("Number is Even", num)
        else:
            print("Number is Odd", num)

        total += num   
    
    print(f"\nSum of all numbers from {start} to {end} : {total}")

# 3.) Exit
elif choice == 3:
    print("Exiting the program. Goodbye!")

# Invalid choice
else:
    print("Invalid Choice")
