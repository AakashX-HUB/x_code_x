#try and except
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input! Please enter a valid number.")

except Exception as e:
    print("An unexpected error occurred:", e)
#try, except, and finally
try:
    num = int(input("Enter a number: "))

    result = 10 / num

    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("Program finished.")
#assert
try:
    age = int(input("Enter your age: "))

    assert age >= 18, "You must be 18 or older."

    print("Access granted.")

except ValueError:
    print("Please enter a valid number.")

except AssertionError as e:
    print(e)
#raise
try:
    num = int(input("Enter a positive number: "))

    if num < 0:
        raise ValueError("Negative numbers are not allowed.")

    print("You entered:", num)

except ValueError as e:
    print(e)
#Combined Example
try:
    age = int(input("Enter your age: "))

    assert age > 0, "Age must be positive."

    if age < 18:
        raise Exception("You are not eligible.")

    print("Eligible")

except ValueError:
    print("Please enter a valid number.")

except AssertionError as e:
    print(e)

except Exception as e:
    print(e)

finally:
    print("Thank you!")

print("math module")

import math

print(math.sqrt(16))
print(math.cbrt(27))

degrees = 180

print(math.tan(degrees))
print(math.sin(90))

print(math.ceil(90.90))
print(math.floor(90.90))

print(math.factorial(5))
