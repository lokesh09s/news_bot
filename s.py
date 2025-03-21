from transformers import pipeline, BartTokenizer
import torch
from news import *

device = 0 if torch.cuda.is_available() else -1  # Use GPU if available

# Summarization function
def sum(text):


    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

    if len(text) > 4000:
        summary = summarizer(text[0:4000], max_length=1000, min_length=250)
    else:
        summary = summarizer(text, max_length=1000, min_length=250)


    # Combine all chunk summaries into one
    return summary[0]['summary_text']

# Run the summarization
