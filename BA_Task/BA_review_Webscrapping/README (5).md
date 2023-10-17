

# British Airways Review Dataset Analysis

This project involves the analysis of a British Airways review dataset, where we aim to gain insights from customer reviews. We utilize various Python libraries for data manipulation, text preprocessing, and sentiment analysis.

## Libraries Used

- **requests**: Used for web scraping or accessing remote data.
- **Beautiful Soup (bs4)**: Employed to parse HTML and extract data from web pages.
- **pandas**: Utilized for data manipulation and analysis.
- **matplotlib**: Employed for data visualization, such as creating plots and charts.
- **nltk (Natural Language Toolkit)**: Utilized for natural language processing tasks, including sentiment analysis.
    - `nltk.download('vader_lexicon')`: Downloads the VADER sentiment analysis lexicon.
    - `nltk.download('punkt')`: Downloads the Punkt tokenizer model for sentence splitting.
    - `nltk.download('stopwords')`: Downloads a list of common stopwords for text preprocessing.
    - `nltk.download('wordnet')`: Downloads WordNet lexical database.
    - `nltk.download('omw-1.4')`: Downloads Open Multilingual WordNet (used for word sense disambiguation).
    - `nltk.download('averaged_perceptron_tagger')`: Downloads the averaged_perceptron_tagger for part-of-speech tagging.
- **wordcloud**: Utilized to generate word clouds for visualizing frequently occurring words in text data.

## Text Preprocessing

The preprocessing of text data is a crucial step in the analysis of reviews. The following text preprocessing steps have been performed:

- **Cleaning Text**: A function has been defined to remove special characters and numericals, leaving only alphabets.

```python
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

def clean(text):
    # Removes all special characters and numericals, leaving the alphabets
    text = re.sub('[^A-Za-z]+', ' ', str(text))
    return text
```

- **Tokenization**: The NLTK library's tokenization function is used to split text into words.

```python
from nltk.tokenize import word_tokenize
from nltk import pos_tag
```

- **Part-of-Speech (POS) Tagging**: Each word in the text is tagged with its part of speech (e.g., noun, verb, adjective, adverb).

```python
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
from nltk.corpus import wordnet
```

- **Lemmatization**: Lemmatization is performed based on part of speech tags, which improves the accuracy of the analysis.

```python
data['Lemma'] = data['POS tagged'].apply(lemmatize)
```

## Sentiment Analysis

Sentiment analysis is a key part of this project. It involves using the VADER sentiment analysis tool from NLTK to determine the sentiment of the reviews. The sentiment analysis process is divided into two steps:

1. **Sentiment score calculation**:

```python
sid = SentimentIntensityAnalyzer()

def vadersentimentanalysis(review):
    vs = sid.polarity_scores(review)
    return vs['compound']

data['Sentiment'] = data['Lemma'].apply(vadersentimentanalysis)
```

2. **Sentiment classification (positive, negative, or neutral)**:

```python
def vader_analysis(compound):
    if compound >= 0.5:
        return 'Positive'
    elif compound < 0:
        return 'Negative'
    else:
        return 'Neutral'

data['Analysis'] = data['Sentiment'].apply(vader_analysis)
```

The sentiment scores are calculated using the VADER lexicon, and then each review is classified as positive, negative, or neutral based on the compound sentiment score.

## Sentiment Distribution Visualization

To visualize the distribution of sentiment in the reviews, a bar chart is generated:

```python
# Visualization: Bar chart for sentiment distribution
sentiment_counts = data['Sentiment'].value_counts()
sentiment_counts.plot(kind='bar')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
```

This chart shows the distribution of sentiments in the dataset.

## Word Cloud Visualization

A word cloud is created to visualize the most common words in the reviews:

```python
# Create a word cloud of the most common words in the reviews
all_reviews = ' '.join(data['reviews'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_reviews)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Reviews')
plt.show()
```

The word cloud provides a visual representation of frequently occurring words in the reviews.

Feel free to adapt and expand this README with any additional information about your project, data sources, or findings from the analysis.