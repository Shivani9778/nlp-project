Simple NLTK Chatbot
This is a simple chatbot built using Python and the Natural Language Toolkit (NLTK) library. The chatbot can respond to basic greetings, questions about itself, and some specific queries related to artificial intelligence and weather.

Features
Responds to common greetings.
Can introduce itself and ask for your name.
Basic interaction about the weather and artificial intelligence.
Simple predefined responses based on pattern matching.
How It Works
The chatbot uses the nltk.chat.util module from NLTK, which allows us to define pairs of patterns and corresponding responses. The chatbot matches user inputs against these patterns and provides predefined responses.

Code Explanation
Here's a brief breakdown of the code:

Importing Libraries: The chatbot uses the nltk library, specifically the Chat and reflections classes from nltk.chat.util.

python
Copy code
import nltk
from nltk.chat.util import Chat, reflections
Defining Pairs: Pairs of patterns and responses are defined in a list. Each pair consists of a regex pattern and a list of possible responses.

python
Copy code
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"what is your name?", ["I am a chatbot created with NLTK. What's your name?"]],
    [r"my name is (.*)", ["Hello %1, nice to meet you!"]],
    [r"how are you?", ["I'm just a bot, but I'm doing great! How about you?"]],
    [r"i am (.*)", ["awesome"]],
    [r"What is artificial intelligence", ["Artificial Intelligence is a branch of computer science..."]],
    [r"what is your age?", ["I am a computer program, so I don't have an age!"]],
    [r"how is the weather today?", ["The weather is rainy."]],
    [r"what's today's weather?", ["Let me check, it looks rainy today."]],
    [r"quit", ["Goodbye! Have a nice day."]],
]
Creating the Chatbot Instance: A Chat instance is created using the defined pairs and reflections.

python
Copy code
chatbot = Chat(pairs, reflections)
Starting the Chat: The converse() method is called to start the conversation, and the user can type their responses in the console.

python
Copy code
print("Hi, I am your simple chatbot. Type 'quit' to exit.")
chatbot.converse()
How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/simple-nltk-chatbot.git
cd simple-nltk-chatbot
Install the required libraries:

bash
Copy code
pip install nltk
Run the chatbot:

bash
Copy code
python chatbot.py
Type your inputs and chat with the bot! To exit, type quit.
