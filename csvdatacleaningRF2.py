import pandas as pd
import re
import nltk



from nltk.tokenize import sent_tokenize, word_tokenize
from spellchecker import SpellChecker
from nltk.corpus import stopwords
import string

# Download necessary NLTK data (run once)
nltk.data.find('tokenizers/punkt')
nltk.download('punkt')
nltk.data.find('taggers/averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('punkt_tab')
print("--- Word Vertex Extraction from Muddy CSV ---")

# --- 1. Configuration ---
# IMPORTANT: Replace 'your_muddy_data.csv' with the actual path to your CSV file.
# Ensure your CSV has a column containing the text data you want to clean and extract words from.
csv_file_path = r'F:\extracted_data\extracted_pdf_data_1.csv' # <--- CHANGE THIS TO YOUR CSV FILE PATH
text_column_name = 'text_column'       # <--- CHANGE THIS TO THE NAME OF YOUR TEXT COLUMN
id_column_name = 'id_column'           # <--- CHANGE THIS TO THE NAME OF YOUR ID COLUMN (if applicable)

# Output file paths
output_all_words_file = 'all_cleaned_words_with_ids.csv'
output_unique_words_file = 'unique_cleaned_words.csv'

# --- 2. Load CSV Data ---
try:
    df = pd.read_csv(csv_file_path)
    if text_column_name not in df.columns:
        raise ValueError(f"'{text_column_name}' not found in the CSV. Please check 'text_column_name'.")
    if id_column_name not in df.columns:
        print(f"Warning: '{id_column_name}' not found. Creating a default ID column.")
        df[id_column_name] = df.index + 1
    
    df.rename(columns={text_column_name: 'text_column', id_column_name: 'id_column'}, inplace=True)

except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found.")
    print("Please make sure the CSV file is in the correct directory or provide the full path.")
    print("\nFalling back to simulated data for demonstration purposes.")
    data = {
        'text_column': [
            "John Doe lives at 123 Main St, Anytown. He is a software engineer.",
            "Please contact Jane Smith at jane.smith@example.com for details.",
            "The new product features enhanced security and user-friendly interface.",
            "My phone number is (555) 123-4567. Call me anytime.",
            "This is a teeeeeeeeeeeeeeeeeeeeeext with lots of spaaaaaaaaam and some intellligence typos.",
            "The quick brown foxx jumps over the lazy doggg. A lot of !!!!!!!! and @@@@@@@ here."
        ],
        'id_column': [1, 2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)
except ValueError as e:
    print(f"Error: {e}")
    print("\nFalling back to simulated data for demonstration purposes.")
    data = {
        'text_column': [
            "John Doe lives at 123 Main St, Anytown. He is a software engineer.",
            "Please contact Jane Smith at jane.smith@example.com for details.",
            "The new product features enhanced security and user-friendly interface.",
            "My phone number is (555) 123-4567. Call me anytime.",
            "This is a teeeeeeeeeeeeeeeeeeeeeext with lots of spaaaaaaaaam and some intellligence typos.",
            "The quick brown foxx jumps over the lazy doggg. A lot of !!!!!!!! and @@@@@@@ here."
        ],
        'id_column': [1, 2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)

print("\nOriginal DataFrame (first 5 rows):")
print(df.head())
print("-" * 50)

# --- 3. PII Redaction Functions (Reused from previous script) ---
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\b(?:\d{3}[-.\s]?\d{3}[-.\s]?\d{4}|\(\d{3}\)\s*\d{3}[-.\s]?\d{4})\b'
name_pattern = r'\b(?:[A-Z][a-z]+(?:\s[A-Z][a-z]+)?)\b'

def redact_pii(text):
    """Redacts common PII patterns from text."""
    text = str(text) # Ensure text is string
    text = re.sub(email_pattern, '[EMAIL_REDACTED]', text)
    text = re.sub(phone_pattern, '[PHONE_REDACTED]', text)
    if re.search(name_pattern, text) and (re.search(email_pattern, text) is None and re.search(phone_pattern, text) is None):
         text = re.sub(name_pattern, '[NAME_REDACTED]', text, count=1)
    return text

df['text_column_pii_cleaned'] = df['text_column'].astype(str).apply(redact_pii)
print("\nDataFrame after PII Cleaning (Redaction - first 5 rows):")
print(df[['text_column', 'text_column_pii_cleaned']].head())
print("-" * 50)

# --- 4. Spam and Typo Handling Functions (Reused from previous script) ---
def remove_excess_spam(text):
    """Removes excess character spam and non-standard symbols."""
    text = str(text)
    text = re.sub(r'(.)\1{2,}', r'\1', text)
    text = re.sub(r'[^a-zA-Z0-9\s.,!?;:]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

spell = SpellChecker()

def handle_typos(text):
    """Attempts to correct typos using a spell checker."""
    text = str(text)
    words = word_tokenize(text)
    corrected_words = []
    for word in words:
        if not spell.unknown([word]) and len(word) > 2:
            corrected_word = spell.correction(word)
            if corrected_word and corrected_word != word and spell.distance(word, corrected_word) <= 2:
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)
        else:
            corrected_words.append(word)
    return " ".join(corrected_words)

df['text_column_cleaned_final'] = df['text_column_pii_cleaned'].apply(remove_excess_spam)
df['text_column_cleaned_final'] = df['text_column_cleaned_final'].apply(handle_typos)

print("\nDataFrame after Spam and Typo Cleaning (first 5 rows):")
print(df[['text_column_pii_cleaned', 'text_column_cleaned_final']].head(10))
print("-" * 50)

# --- 5. Word Tokenization and Further Cleaning for Vertex Representation ---
# This step prepares individual words for use as "vertices".

stop_words = set(stopwords.words('english'))

def clean_and_tokenize_words_for_vertex(text):
    """
    Cleans text, tokenizes into words, removes punctuation and stopwords,
    and converts to lowercase.
    """
    text = str(text).lower() # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)) # Remove punctuation
    words = word_tokenize(text)
    
    # Remove stopwords and filter out empty strings or words that are just spaces
    cleaned_words = [word for word in words if word.isalnum() and word not in stop_words]
    return cleaned_words

# Apply the word cleaning and tokenization
df['cleaned_words'] = df['text_column_cleaned_final'].apply(clean_and_tokenize_words_for_vertex)

# --- 6. Prepare Output: List of Words as Vertices ---
# We'll create two types of output:
# 1. A list of all cleaned words, associated with their original row ID.
# 2. A list of unique cleaned words (for a set of all possible vertices).

all_words_with_ids = []
for index, row in df.iterrows():
    row_id = row['id_column']
    for word in row['cleaned_words']:
        all_words_with_ids.append({'word': word, 'original_id': row_id})

# Convert to DataFrame for easy viewing/export
words_df = pd.DataFrame(all_words_with_ids)

# Get unique words
unique_words_list = words_df['word'].unique().tolist()

print("\nAll Cleaned Words (as Vertices) with Original IDs (first 10 rows):")
print(words_df.head(10))
print("-" * 50)

print("\nUnique Cleaned Words (Potential Vertex Set):")
print(unique_words_list)
print(f"\nTotal unique words: {len(unique_words_list)}")
print("-" * 50)

# --- 7. Save Output Files ---
try:
    words_df.to_csv(output_all_words_file, index=False)
    print(f"\nSaved all cleaned words with IDs to: {output_all_words_file}")
except Exception as e:
    print(f"Error saving {output_all_words_file}: {e}")

try:
    pd.DataFrame({'unique_words': unique_words_list}).to_csv(output_unique_words_file, index=False)
    print(f"Saved unique cleaned words to: {output_unique_words_file}")
except Exception as e:
    print(f"Error saving {output_unique_words_file}: {e}")

print("\nScript finished. Check the generated CSV files.")
