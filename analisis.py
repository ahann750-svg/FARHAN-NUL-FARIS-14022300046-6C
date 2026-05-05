import pandas as pd
from transformers import pipeline

# Load the data from CSV
df = pd.read_csv('ulasan_google_play.csv')

# Initialize the sentiment analysis pipeline with an Indonesian RoBERTa model
sentiment_pipeline = pipeline(
    'sentiment-analysis',
    model='w11wo/indonesian-roberta-base-sentiment-classifier',
    tokenizer='w11wo/indonesian-roberta-base-sentiment-classifier'
)

# Apply sentiment analysis to the 'content' column
df['sentiment'] = df['content'].apply(lambda x: sentiment_pipeline(x)[0]['label'])
df['sentiment_score'] = df['content'].apply(lambda x: sentiment_pipeline(x)[0]['score'])

# Display the DataFrame with the new sentiment columns
print(df.head())