import csv

FILE_NAME = "expenses.csv"

# Create file with header if it doesn't exist
def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])
    except FileExistsError:
        pass


# Add Expense
def add_expense():
    try:
        date = input("Enter Date (DD-MM-YYYY): ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount])

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount! Please enter a numeric value.")

    except Exception as e:
        print("Error:", e)


# View Expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n--- All Expenses ---")
            for row in reader:
                print("{:<15} {:<15} {:<10}".format(*row))

    except FileNotFoundError:
        print("Expense file not found!")

    except Exception as e:
        print("Error:", e)


# Calculate Total Expenses
def total_expenses():
    try:
        total = 0

        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            for row in reader:
                total += float(row[2])

        print(f"\nTotal Expenses: ₹{total:.2f}")

    except FileNotFoundError:
        print("Expense file not found!")

    except Exception as e:
        print("Error:", e)


# Search by Category
def search_category():
    try:
        search = input("Enter Category to Search: ").lower()

        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            found = False

            print("\nMatching Expenses:")
            for row in reader:
                if row[1].lower() == search:
                    print(row)
                    found = True

            if not found:
                print("No expenses found in this category.")

    except FileNotFoundError:
        print("Expense file not found!")

    except Exception as e:
        print("Error:", e)


# Main Menu
def main():
    initialize_file()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Search by Category")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_expense()

            elif choice == 2:
                view_expenses()

            elif choice == 3:
                total_expenses()

            elif choice == 4:
                search_category()

            elif choice == 5:
                print("Thank you!")
                break

            else:
                print("Please enter a valid choice (1-5).")

        except ValueError:
            print("Invalid input! Enter a number.")

        except Exception as e:
            print("Error:", e)


main()

# Function to add student record
def add_student():
    try:
        name = input("Enter Student Name: ")
        marks = input("Enter Student Marks: ")

        with open("students.txt", "a") as file:
            file.write(f"Name: {name}, Marks: {marks}\n")

        print("Student record saved successfully!")

    except Exception as e:
        print("Error while writing to file:", e)


# Function to display all records
def display_students():
    try:
        with open("students.txt", "r") as file:
            records = file.read()

            if records:
                print("\n--- Student Records ---")
                print(records)
            else:
                print("No records found.")

    except FileNotFoundError:
        print("File not found! No student records available.")

    except Exception as e:
        print("Error while reading file:", e)


# Main Program
add_student()
display_students()
