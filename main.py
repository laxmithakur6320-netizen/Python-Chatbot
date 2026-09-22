Add Python chatbot source code
print("Namaste! welcome to your  chatbot")
print("you can ask me basic question, type 'bye' to exit the bot")

#Chatbot memory creation [ dictionary of responses ]

responses = {
   "hello": "Hi! How can I help you today?",
"hi": "Hello!",
"hey": "Hey there!",
"good morning": "Good morning! Have a nice day.",
"good afternoon": "Good afternoon!",
"good evening": "Good evening!",
"good night": "Good night! Sweet dreams.",

"how are you": "I'm doing great. Thanks for asking!",
"what is your name": "My name is PyBot.",
"who are you": "I'm a chatbot built with Python.",
"who made you": "I was created by a Laxmi Thakur.",
"what can you do": "I can answer questions and help you with basic tasks.",
"help": "Sure! Ask me anything.",

"thank you": "You're welcome!",
"thanks": "Happy to help!",
"bye": "Goodbye! Have a great day.",
"see you": "See you soon!",
"take care": "Take care and stay safe.",

"tell me a joke": "Why do programmers hate bugs? Because they take too long to debug!",
"tell me a fact": "Python is one of the most popular programming languages.",
"motivate me": "Keep learning. Every small step brings you closer to success.",

"what is python": "Python is a high-level programming language.",
"what is html": "HTML is used to create web pages.",
"what is css": "CSS is used to style web pages.",
"what is javascript": "JavaScript makes websites interactive.",
"what is ai": "AI stands for Artificial Intelligence.",
"what is cybersecurity": "Cybersecurity protects systems and data from cyber threats.",

"who invented python": "Python was created by Guido van Rossum.",
"what is the capital of india": "The capital of India is New Delhi.",
"who is the prime minister of india": "The Prime Minister of India is Narendra Modi.",
"i am sad": "I'm here for you. I hope things get better soon.",
"i am happy": "That's wonderful to hear!",  
}


#METHOD/FUNCTION TO GET RESPONSE FROM THE BOT

def getResponseBot(userInput):
    userinput = userInput.lower()

    for eachkey in responses:
        if eachkey in userinput:
            return responses[eachkey]

    return "Sorry, I don't understand that. Can you please rephrase your question?"
# Take user input and respond accordingly

while True:
    userInput = input("Please enter your question: ")
    reply = getResponseBot(userInput)
    print("Bot:", reply)

    if "bye" in userInput.lower():
        break
