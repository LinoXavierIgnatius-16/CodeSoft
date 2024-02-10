import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive length.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        generated_password = generate_password(length)
        print("Generated Password:", generated_password)

        ask_to_generate_another = input("Do you want to generate another password? (yes/no): ").lower()
        if ask_to_generate_another != 'yes':
            print("Exiting the Password Generator.")
            break

if __name__ == "__main__":
    main()
