def get_odd_number_from_user():
    while True:
        try:
            user_input = input("Enter an odd number: ")
            number = int(user_input)

            if number % 2 == 1:
                return number
            else:
                raise ValueError("Please enter only odd numbers.")

        except ValueError as ve:
            print(f"Error: {ve}")
            print("Try again.")

if __name__ == "__main__":
    try:
        odd_number = get_odd_number_from_user()
        print(f"You entered an odd number: {odd_number}")

    except KeyboardInterrupt:
        print("\nUser interrupted the program.")

    except Exception as e:
        print(f"An error occurred: {e}")
