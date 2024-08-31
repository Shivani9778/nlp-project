# Simple Chatbot using NLTK

This is a basic chatbot built using Python and the Natural Language Toolkit (NLTK) library. The chatbot is capable of responding to simple user inputs based on predefined patterns.

## Features

- Responds to basic greetings, introductions, and questions about AI.
- Simple pattern matching using regular expressions.
- Predefined responses based on user input.
- Designed to showcase a basic implementation of chatbot logic with NLTK.

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

The chatbot uses the NLTK library's `Chat` class, which uses pattern matching with predefined patterns and corresponding responses. It uses regular expressions to match user input with patterns and responds accordingly.

### Code Explanation

- **Import Libraries**: 

  ```python
  import nltk
  from nltk.chat.util import Chat, reflection
   ```
