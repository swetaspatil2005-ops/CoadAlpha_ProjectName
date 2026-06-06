# Smart Chatbot

# Function to generate chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi! How can I help you?"

    elif user_input == "hi":
        return "Hello! Nice to meet you."

    elif user_input == "good morning":
        return "Good Morning! Have a nice day."

    elif user_input == "good evening":
        return "Good Evening!"

    elif user_input == "how are you":
        return "I am fine, thanks!"

    elif user_input == "what is your name":
        return "My name is Smart Chatbot."

    elif user_input == "who are you":
        return "I am a simple rule-based chatbot."

    elif user_input == "who created you":
        return "I was created using Python."

    elif user_input == "what is python":
        return "Python is a popular programming language."

    elif user_input == "what is ai":
        return "AI stands for Artificial Intelligence."

    elif user_input == "what is machine learning":
        return "Machine Learning is a branch of AI."

    elif user_input == "what is chatbot":
        return "A chatbot is a program that can communicate with users."

    elif user_input == "what is programming":
        return "Programming is the process of writing instructions for computers."

    elif user_input == "what is data science":
        return "Data Science is the study of data to gain useful insights."

    elif user_input == "what is cloud computing":
        return "Cloud Computing provides services over the internet."

    elif user_input == "what is cyber security":
        return "Cyber Security protects systems and networks from cyber threats."

    elif user_input == "what is html":
        return "HTML is used to create web pages."

    elif user_input == "what is css":
        return "CSS is used to style web pages."

    elif user_input == "what is java":
        return "Java is an object-oriented programming language."

    elif user_input == "what is c language":
        return "C is a powerful procedural programming language."

    elif user_input == "what is c++":
        return "C++ is an extension of the C programming language."

    elif user_input == "what is javascript":
        return "JavaScript is used to make web pages interactive."

    elif user_input == "what is sql":
        return "SQL is used to manage databases."

    elif user_input == "what is computer":
        return "A computer is an electronic device that processes data."

    elif user_input == "what is internet":
        return "The Internet is a global network connecting millions of devices."

    elif user_input == "what is operating system":
        return "An Operating System manages computer hardware and software."

    elif user_input == "what is database":
        return "A database is a collection of organized data."

    elif user_input == "what is linux":
        return "Linux is an open-source operating system."

    elif user_input == "what is kali linux":
        return "Kali Linux is a Linux distribution used for cybersecurity testing."

    elif user_input == "what is networking":
        return "Networking connects computers to share data and resources."

    elif user_input == "what is software":
        return "Software is a set of instructions that tells a computer what to do."

    elif user_input == "what is hardware":
        return "Hardware refers to the physical parts of a computer."

    elif user_input == "tell me a joke":
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    elif user_input == "what is the capital of india":
        return "New Delhi is the capital of India."

    elif user_input == "help":
        return "Ask me questions about programming, AI, computers, and technology."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a great day."

    # Default response for unknown questions
    else:
        return "Sorry, I don't understand that question."


# Chatbot title
print("================================")
print("        SMART CHATBOT")
print("================================")

# Main chatbot loop
while True:
    user = input("You: ")

    response = chatbot_response(user)
    print("Bot:", response)

    # Exit chatbot when user types bye
    if user.lower() == "bye":
        break