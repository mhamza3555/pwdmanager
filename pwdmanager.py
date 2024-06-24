starting_program = input("Enter 'hello' to start the program: ").lower()
if starting_program != "hello":
    print("Program not started. Exiting...")
    exit()

def view():
    try:
        with open('password.txt', 'r') as p:
            for line in p.readlines():
                data = line.strip()
                if "and" in data:
                    username, passw = data.split("and")
                    username = username.replace("name: ", "").strip()
                    passw = passw.replace("password: ", "").strip()
                    print(f"Name: {username} and Password: {passw}\n")
                else:
                    print("Incorrect format in the file.")
    except FileNotFoundError:
        print("The file does not exist. Please add a password first.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    with open('password.txt', 'a') as p:
        p.write(f"name: {name} and password: {password}\n")

while True:
    user_input = input('Enter "view" to see the details, "add" to add the details, and "q" to close the program: ').lower()

    if user_input == "q":
        break

    elif user_input == "view":
        view()

    elif user_input == "add":
        add()

    else:
        print("Invalid input. Please try again.")
