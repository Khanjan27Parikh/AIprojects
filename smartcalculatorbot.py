#  AI Tool builder - Smart Calcultor bot

# eg: Add 3 and 5, Subtract 2 from 10, Multipy 4 and 6, Divide 10 by 2

# Building basic operations as functions
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Cannot divide by 0"
    else:
        return a / b
    

# Command handler that understands Natural Text
def handle_smart_command(command):
    command = command.lower()

    if "add" in command:
        parts = command.replace("add", "").strip().split("and")   
        # .replace() will replace the "add" with empty string, 
        # .strip() will remove the spaces, 
        # .split() will split on basis of "and" and return a list of 2 numbers
        a,b = int(parts[0]), int(parts[1])
        print("Answer:", add(a,b))

    elif "subtract" in command:
        parts = command.replace("subtract", "").strip().split("from")
        b,a = int(parts[0]), int(parts[1])
        print("Answer:", subtract(a,b))

    elif "multiply" in command:
        parts = command.replace("multiply", "").strip().split("and")
        a,b = int(parts[0]), int(parts[1])
        print("Answer:", multiply(a,b))

    elif "divide" in command:
        parts = command.replace("divide", "").strip().split("by")
        a,b = int(parts[0]), int(parts[1])
        print("Answer:", divide(a,b))
    
    else:
        print("Sorry. I didn't understand your question.")



# Adding to assistant loop
def run_smart_bot():
    print("Hi, I can do math! Say something like: "
          "\n-> Add 5 and 8\n-> Subtract 5 from 6\n-> Multipy 4 and 6\n-> Divide 10 by 2")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        handle_smart_command(user_input)


run_smart_bot()