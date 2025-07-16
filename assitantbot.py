# Text-Based Assistant Bot
"""
Understand how simple AI chatbots work using Python, and build a mini assistant that can:

1. Greet users
2. Respond to simple commands (like time, date, etc.)
3. Say goodbye
4. (Optional) Be expanded later with voice or OpenAI API
"""
def greet():
    print("Hey! I am PyBot 🤖. How I can help you?")

def handle_command(command):
    if "time" in command:
        from datetime import datetime
        print("Current Time:", datetime.now().strftime("%H:%M:%S"))
    elif "date" in command:
        from datetime import datetime
        print("Today's Date:", datetime.now().strftime("%d-%m-%y"))
    elif "hello" in command or "hi" in command:
        print("Hey there! 👋")
    elif "how are you" in command:
        print("I am doing great! Thanks. How about you?")
    elif "calculate" in command:
        try:
            expression = command.replace("calculate", "").strip()
            result = eval(expression)
            print("The answer is", result)
        except:
            print("Sorry. I couldn't understand or evaluate your expression!")
    elif "exit" in command or "bye" in command:
        print("Goodbye! Have a great Day!")
        return False
    else:
        print("Sorry. I didn't understand that.")
    return True


def run_bot():
    greet()
    running = True
    while running:
        user_input = input("You: ").lower()
        running = handle_command(user_input)

run_bot()