# Simple Chatbot using NLTK

This is a basic chatbot built using Python and the Natural Language Toolkit (NLTK) library. The chatbot is designed to respond to user inputs based on predefined patterns using regular expressions.

## Features

- Responds to basic greetings, introductions, and simple questions.
- Uses pattern matching with regular expressions to generate responses.
- Can be extended with more patterns and responses to enhance interactivity.

## Requirements

- Python 3.x
- NLTK library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. Install the required dependencies:

    ```bash
    pip install nltk
    ```

3. Run the chatbot:

    ```bash
    python chatbot.py
    ```

## How it Works

### Define Patterns and Responses

Define a list of `pairs` where each pair consists of a regular expression pattern and a list of possible responses.

```python
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    # Add more patterns and responses
]

