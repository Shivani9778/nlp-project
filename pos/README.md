# NLTK Text Processing Example

This project demonstrates basic text processing techniques using the Natural Language Toolkit (NLTK) in Python. The script performs sentence tokenization, word tokenization, stop word removal, and Part-of-Speech (POS) tagging on a given text.

## Prerequisites

Ensure you have Python installed on your system. You will also need the NLTK library, which can be installed via pip if you haven't done so already:

```bash
pip install nltk
Setup
Before running the code, ensure that the required NLTK data files are downloaded, including the Punkt tokenizer models and the stopwords list. You can download them by running the following Python code:

python
Copy code
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
Script Overview
The script processes a dummy text by performing the following steps:

Sentence Tokenization: Splits the text into individual sentences.
Word Tokenization: Further splits each sentence into words and punctuation marks.
Stop Words Removal: Filters out common English stop words such as 'is', 'and', 'the', etc.
POS Tagging: Tags each word with its part of speech, such as nouns, verbs, adjectives, etc.
Code
Here is the code that is used in this project:

python
Copy code
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Set of stopwords in English
stop_words = set(stopwords.words('english'))

# Sample text
txt = ("Sukanya, Rajib and Naba are my good friends. "
       "Sukanya is getting married next year. "
       "Marriage is a big step in one’s life. "
       "It is both exciting and frightening. "
       "But friendship is a sacred bond between people. "
       "It is a special kind of love between us. "
       "Many of you must have tried searching for a friend "
       "but never found the right one.")

# Sentence tokenization
tokenized = sent_tokenize(txt)
for i in tokenized:
    # Word tokenization
    wordsList = nltk.word_tokenize(i)
    
    # Removing stop words from word list
    wordsList = [w for w in wordsList if not w in stop_words] 
    
    # POS tagging
    tagged = nltk.pos_tag(wordsList)
    
    print(tagged)
How to Run
Copy the above code into a Python file (e.g., nltk_example.py).

Make sure you have downloaded the necessary NLTK data files (as mentioned in the Setup section).

Run the script using the command:

bash
Copy code
python nltk_example.py
Expected Output
The script will output a list of tuples for each sentence, where each tuple contains a word and its corresponding POS tag. For example:

css
Copy code
[('Sukanya', 'NNP'), (',', ','), ('Rajib', 'NNP'), ('Naba', 'NNP'), ('good', 'JJ'), ('friends', 'NNS'), ('.', '.')]
[('Sukanya', 'NNP'), ('getting', 'VBG'), ('married', 'VBN'), ('next', 'JJ'), ('year', 'NN'), ('.', '.')]
...


This project is licensed under the MIT License. See the LICENSE file for details.

vbnet
Copy code

This `README.md` provides clear instructions on what the code does, how to set it up, and what the user can exp
