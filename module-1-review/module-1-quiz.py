"""
MODULE 1 QUIZ
=============

This quiz tests understanding of Module 1 concepts: Variables, Arithmetic Operations, and String Concatenation.
Students should answer all questions and submit their responses.

Instructions:
- Answer multiple choice questions by writing the letter (A, B, C, or D)
- For coding questions, write the Python code
- For short answer questions, write 1-2 sentences

"""

print("=" * 40)
print("MODULE 1 QUIZ")
print("Name: ___________________")
print("Date: ___________________")
print("=" * 40)

# =============================================================================
# MULTIPLE CHOICE QUESTIONS 
# =============================================================================

print("\nMULTIPLE CHOICE: Choose the best answer")
print("-" * 40)

print("\n1. Which of the following is the correct way to assign the value 10 to a variable named 'count'?")
print("   B) count = 10")

print("\n2. What is the output of: print(15 % 4)")
print("   B) 3")

print("\n3. Which operator is used for string concatenation in Python?")
print("   C) +")

print("\n4. What does the following code output?")
print("   B) 11")

print("\n5. To include a number in a string concatenation, you must:")
print("   B) Use the str() function")

# =============================================================================
# SHORT ANSWER QUESTIONS 
# =============================================================================

print("\n\nSHORT ANSWER: Answer in 1-2 complete sentences")
print("-" * 50)

print("\n6. Explain the difference between the = operator and the == operator in Python.")
print("   Answer: = is used to assign a value to a variable and == is used to check if two values are equal in conditionals")

print("\n7. What is the modulus operator (%) used for? Give an example.")
print("   Answer: this operator is used to get the remainder of two divided numbers. So 15 % 4 would return 3.")

print("\n8. Why do we need to use str() when concatenating numbers with strings?")
print("   Answer: numbers have a different data type (either float or int), and will return a type error if a concatenation is attempted.")

# =============================================================================
# CODING QUESTIONS 
# =============================================================================

print("\n\nCODING QUESTIONS: Write Python code for each problem")
print("-" * 50)

print("\n9. Write code to calculate the area of a circle with radius 7.")
print("   Use the formula: area = 3.14159 * radius * radius")
print("   Store the result in a variable called 'area' and print it.")
print()
print("   Code:")
print("   radius=7 ")
print("   area = 3.14159 * (radius**2)")
print("   print(area)")

print("\n10. Create variables for your favorite movie title and the year it was released.")
print("    Then create a message that says: 'My favorite movie is [title] from [year].'")
print("    Print the message.")
print()
print("    Code:")
print("    movie_title = 'whiplash' ")
print("    year = 2014")
print("    message = f'My favorite movie is { movie_title } from { year  }'")
print("    print(message)")

print("\n11. Write code that calculates how many weeks and days are in 100 days.")
print("    Print the result in the format: '100 days = X weeks and Y days'")
print("    (Hint: Use integer division // and modulus %)")
print()
print("    Code:")
print("    weeks = 100 // 7")
print("    days = 100 % 7")
print("    print(f'100 days = { weeks } weeks and { days } days)' ")

# =============================================================================
# BONUS QUESTION 
# =============================================================================


print("-" * 45)

print("\n12. Create a program that calculates the total cost of buying textbooks.")
print("    - Math book: $89.99")
print("    - Science book: $76.50")
print("    - History book: $65.25")
print("    - Student discount: 15% off the total")
print("    Calculate and print the original total, discount amount, and final total.")
print()
print("    Code:")
print("    total_cost = 89.99 + 76.50 + 65.25")
print("    discount_amount = total_cost * .15")
print("    final_total = total_cost - discount_amount")
print("    print(f'the total cost of books is { total_cost } but after the discount is applied {discount_amount} is taken off leaving the final price as { final_total })")

print("\n" + "=" * 40)
print("END OF QUIZ")


print("=" * 40)
