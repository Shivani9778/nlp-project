mport nltk
from nltk.chat.util import Chat, reflections
# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you ?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created with NLTK. What's your name?"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!"]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing great! How about you?"]
    ],
    [
        r"i am (.*)",
        ["awesome"]
    ],
    [
        r"What is artificial intelligence",
        ["Artificial Intelligence is a branch of computer science by which we can create a Intelligence machine to think like human ,behave like human and act like like human."]
    ],
    [
        r"what is your age?",
        ["i am a computer program dude seriously you are asking me this"]
    ],
    [
        r"how is the weather today?",
        ["the whether is rainy."]
    ],
    [
        r"what's today's weather?",
        ["Let me check, it looks rainy today."]
    ],
    [
        r"quit",
        ["Goodbye! Have a nice day."]
    ],
]

# Create a Chat instance with the pairs and reflections
chatbot = Chat(pairs, reflections)

# Start a conversation with the user
print("Hi, I am your simple chatbot. Type 'quit' to exit.")
chatbot.converse()
