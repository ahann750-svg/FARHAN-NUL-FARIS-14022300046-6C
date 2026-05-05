import pandas as pd
from transformers import pipeline

# Load the CSV file containing the reviews
df = pd.read_csv('ulasan_google_play.csv')
print(df.head())