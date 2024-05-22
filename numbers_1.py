"""
Of course! Here's another task to help you practice your Python skills:

### Task: Simple Grade Calculator

Write a Python program that:
1. Prompts the user to enter a list of grades (as integers) separated by spaces.
2. Calculates the average grade.
3. Determines the corresponding letter grade based on the average:
   - `A` for average 90-100
   - `B` for average 80-89
   - `C` for average 70-79
   - `D` for average 60-69
   - `F` for average below 60
4. Prints the average grade and the corresponding letter grade.

### Example interaction with the program:
```
Enter grades separated by spaces: 85 90 78 92
The average grade is: 86.25
The letter grade is: B
```

### Steps:
1. Use `input()` to get the list of grades.
2. Split the input string to get individual grade values.
3. Convert the grade values to integers.
4. Calculate the average of the grades.
5. Determine the letter grade based on the average.
6. Print the average grade and the letter grade.

Once you've written your code, paste it here, and I'll check it for you!"""

def main():
    numbers = input("Enter grades separated by spaces: ")
    #print(numbers)
    #print(numbers.split())
    numbers_list = int(numbers.split())
    print(sum(numbers_list)/len(numbers_list))

main()