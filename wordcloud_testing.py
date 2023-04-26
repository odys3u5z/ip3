import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Download the German and French stop words from nltk
nltk.download('stopwords')

# Read the CSV file
csv_file = 'EN.csv'
df = pd.read_csv(csv_file)

# Combine all the descriptions into a single string
all_descriptions = ' '.join(df['Description'])

# Make all words lowercase
cleaned_descriptions = all_descriptions.lower()

# Remove telephone numbers
cleaned_descriptions = re.sub(r'\+41\d+', '', cleaned_descriptions)

# Remove punctuation from the text
translator = str.maketrans('', '', string.punctuation)
cleaned_descriptions = cleaned_descriptions.translate(translator)

# Split the cleaned string into a list of words
words_list = cleaned_descriptions.split()

# Get the German and French stop words
german_stopwords = set(stopwords.words('german'))
french_stopwords = set(stopwords.words('french'))
english_stopwords = set(stopwords.words('english'))

# Combine German and French stop words into a single set
all_stopwords = german_stopwords | french_stopwords| english_stopwords

# Add specific unwanted characters and abbreviations to the stop words
unwanted_words = {'', '•', 'ag', 'undoder', 'sowie'}
all_stopwords = all_stopwords | unwanted_words

# Remove common German, French words, and specific unwanted words from the list
filtered_words = [word for word in words_list if word not in all_stopwords]

# Remove entries that only consist of numbers
filtered_words = [word for word in filtered_words if not word.isdigit()]

# Count the occurrences of each word
word_count = Counter(filtered_words)
# Remove words that occur less than 10 times
word_count_filtered = {word: count for word, count in word_count.items() if count >= 20}

print(word_count_filtered)

# Generate a word cloud
wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=all_stopwords, min_font_size=10).generate_from_frequencies(word_count_filtered)

# Display the word cloud
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)

# Save the word cloud as an image
plt.savefig('wordcloud.png')

# Show the word cloud
plt.show()

