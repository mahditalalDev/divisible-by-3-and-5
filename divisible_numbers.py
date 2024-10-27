# Prompt the user to enter an upper limit number
user_number = int(input("Please enter a number: "))

# Check if the input is less than 15
if user_number < 15:
    print("There is no number divisible by both 3 and 5 in this range")

# Loop through numbers from 15 up to the user's number
for i in range(15, user_number):
    # Check if the number is divisible by both 3 and 5
    if i % 15 == 0:
        print(i)  # Print the number if it meets the condition
