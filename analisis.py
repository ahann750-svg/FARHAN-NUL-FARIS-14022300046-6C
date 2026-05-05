import pandas as pd
from transformers import pipeline
import warnings
warnings.filterwarnings('ignore')

# Load the data from CSV
df = pd.read_csv('ulasan_google_play.csv')

# Remove rows with missing content
df = df.dropna(subset=['content'])

# Initialize the sentiment analysis pipeline with an Indonesian RoBERTa model
sentiment_pipeline = pipeline(
    'sentiment-analysis',
    model='w11wo/indonesian-roberta-base-sentiment-classifier',
    tokenizer='w11wo/indonesian-roberta-base-sentiment-classifier'
)

# Apply sentiment analysis to the 'content' column with error handling
def analyze_sentiment(text):
    try:
        if isinstance(text, str) and len(text.strip()) > 0:
            result = sentiment_pipeline(text[:512])  # Limit to 512 chars
            return result[0]['label']
        return 'NEUTRAL'
    except:
        return 'NEUTRAL'

def analyze_sentiment_score(text):
    try:
        if isinstance(text, str) and len(text.strip()) > 0:
            result = sentiment_pipeline(text[:512])  # Limit to 512 chars
            return result[0]['score']
        return 0.0
    except:
        return 0.0

print("Analyzing sentiments...")
df['sentiment'] = df['content'].apply(analyze_sentiment)
df['sentiment_score'] = df['content'].apply(analyze_sentiment_score)

# Display the DataFrame with the new sentiment columns
print(df.head())

# Save the results to a CSV file
df.to_csv('hasil_analisis_sentimen.csv', index=False, encoding='utf-8')
print("\nHasil analisis sentimen disimpan ke 'hasil_analisis_sentimen.csv'")