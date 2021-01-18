# This program takes text from an online article and converts it to speech

from newspaper import Article
import nltk
from gtts import gTTS
import os

# Get the article
article = Article("https://www.mindtools.com/page6.html")

article.download()
article.parse()
nltk.download("punkt")  # Download the punkt package
article.nlp()  # Apply Natural Language Processing

# Get the article's text and store it into a variable called "mytext"
mytext = article.text
print(mytext)

language = "en"  # English

# Convert the text to speech
myobj = gTTS(text=mytext, lang=language, slow=False)

# Save the converted audio to a file
myobj.save("article_audio.mp3")

# Play the converted file
os.system("start article_audio.mp3")
