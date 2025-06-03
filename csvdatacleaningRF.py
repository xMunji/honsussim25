import pandas as pd
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from spellchecker import SpellChecker # New import for typo handling

# Download necessary NLTK data (run once)
# try:
#     nltk.data.find('tokenizers/punkt')
# except nltk.downloader.DownloadError:
    
# try:
#     nltk.data.find('taggers/averaged_perceptron_tagger')
# except nltk.downloader.DownloadError:
#     nltk.download('averaged_perceptron_tagger')
nltk.download('punkt_tab')
print("--- CSV Data Cleaning with Random Forest ---")

# --- 1. Load CSV Data ---
# IMPORTANT: Replace 'your_data.csv' with the actual path to your CSV file.
# Ensure your CSV has a column containing the text data you want to clean.
csv_file_path = r'F:\extracted_data\extracted_pdf_data_1.csv' # <--- CHANGE THIS TO YOUR CSV FILE PATH
text_column_name = 'tables' # <--- CHANGE THIS TO THE NAME OF YOUR TEXT COLUMN
id_column_name = 'text_content'     # <--- CHANGE THIS TO THE NAME OF YOUR ID COLUMN (if applicable)

try:
    df = pd.read_csv(csv_file_path)
    # Ensure the specified text column exists
    if text_column_name not in df.columns:
        raise ValueError(f"'{text_column_name}' not found in the CSV. Please check 'text_column_name'.")
    # If an ID column is specified and exists, use it. Otherwise, create a default index.
    if id_column_name not in df.columns:
        print(f"Warning: '{id_column_name}' not found. Creating a default ID column.")
        df[id_column_name] = df.index + 1
    
    # Rename columns for consistency with the rest of the script
    df.rename(columns={text_column_name: 'text_column', id_column_name: 'id_column'}, inplace=True)

except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found.")
    print("Please make sure the CSV file is in the correct directory or provide the full path.")
    # Fallback to simulated data for demonstration if file not found
    print("\nFalling back to simulated data for demonstration purposes.")
    data = {
        'text_column': [
            "John Doe lives at 123 Main St, Anytown. He is a software engineer.",
            "Please contact Jane Smith at jane.smith@example.com for details.",
            "The new product features enhanced security and user-friendly interface.",
            "My phone number is (555) 123-4567. Call me anytime.",
            "This is a very important document outlining the project's scope.",
            "The meeting minutes from yesterday, 2024-05-30, were approved.",
            "Sarah Johnson works as a data scientist at Tech Corp.",
            "The system provides real-time analytics for business intelligence.",
            "For urgent matters, reach out to David Lee at 987-654-3210.",
            "The research paper discusses novel algorithms for machine learning tasks.",
            "This is a teeeeeeeeeeeeeeeeeeeeeext with lots of spaaaaaaaaam and some intellligence typos.",
            "The quick brown foxx jumps over the lazy doggg. A lot of !!!!!!!! and @@@@@@@ here."
        ],
        'id_column': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
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
            "This is a very important document outlining the project's scope.",
            "The meeting minutes from yesterday, 2024-05-30, were approved.",
            "Sarah Johnson works as a data scientist at Tech Corp.",
            "The system provides real-time analytics for business intelligence.",
            "For urgent matters, reach out to David Lee at 987-654-3210.",
            "The research paper discusses novel algorithms for machine learning tasks.",
            "This is a teeeeeeeeeeeeeeeeeeeeeext with lots of spaaaaaaaaam and some intellligence typos.",
            "The quick brown foxx jumps over the lazy doggg. A lot of !!!!!!!! and @@@@@@@ here."
        ],
        'id_column': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    }
    df = pd.DataFrame(data)


print("\nOriginal DataFrame (first 5 rows):")
print(df.head())
print("-" * 50)

# --- 2. Feature Engineering for PII Detection ---
# We'll create features to help a Random Forest classifier identify PII.
# This is a simplified approach; real PII detection is more complex.

# Regex patterns for common PII (simplified)
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\b(?:\d{3}[-.\s]?\d{3}[-.\s]?\d{4}|\(\d{3}\)\s*\d{3}[-.\s]?\d{4})\b'
# A very basic name pattern (prone to false positives, for demo only)
name_pattern = r'\b(?:[A-Z][a-z]+(?:\s[A-Z][a-z]+)?)\b'

def extract_pii_features(text):
    """Extracts simple PII-related features from text."""
    # Ensure text is a string before applying regex
    text = str(text)
    features = {
        'has_email': bool(re.search(email_pattern, text)),
        'has_phone': bool(re.search(phone_pattern, text)),
        'has_name_like_pattern': bool(re.search(name_pattern, text))
    }
    return pd.Series(features)

# Apply feature extraction to each row
# IMPORTANT FIX: Convert 'text_column' to string type before applying the function
pii_features_df = df['text_column'].astype(str).apply(extract_pii_features)
df = pd.concat([df, pii_features_df], axis=1)

# For demonstration, we'll manually label some rows as containing PII.
# In a real scenario, this would come from a labeled dataset.
# If you have a real dataset, you'll need to create this 'contains_pii_label' column
# based on your actual PII annotations.
# For now, we'll use a placeholder or generate based on simple rules for new data.
if 'contains_pii_label' not in df.columns:
    print("\nWarning: 'contains_pii_label' not found. Generating dummy labels for PII detection training.")
    # This is a very simplistic way to generate labels for new data.
    # In a real scenario, you would need actual labels for supervised training.
    df['contains_pii_label'] = df.apply(lambda row: 1 if row['has_email'] or row['has_phone'] or row['has_name_like_pattern'] else 0, axis=1)

print("\nDataFrame with PII Features and Labels (first 5 rows):")
print(df[['text_column', 'has_email', 'has_phone', 'has_name_like_pattern', 'contains_pii_label']].head())
print("-" * 50)

# --- 3. Train Random Forest for PII Detection ---
X_pii = df[['has_email', 'has_phone', 'has_name_like_pattern']]
y_pii = df['contains_pii_label']

# Check if there's enough data for splitting
if len(df) < 2:
    print("Not enough data to perform train-test split for PII detection. Skipping model training.")
    pii_classifier = None # Set classifier to None if not trained
else:
    X_train_pii, X_test_pii, y_train_pii, y_test_pii = train_test_split(
        X_pii, y_pii, test_size=0.3, random_state=42, stratify=y_pii if len(y_pii.unique()) > 1 else None
    )

    pii_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    pii_classifier.fit(X_train_pii, y_train_pii)

    y_pred_pii = pii_classifier.predict(X_test_pii)
    print("\nPII Detection Model Performance:")
    print(f"Accuracy: {accuracy_score(y_test_pii, y_pred_pii):.2f}")
    print(classification_report(y_test_pii, y_pred_pii))
    print("-" * 50)

# --- 4. Apply PII Cleaning (Redaction) ---
# We'll use the trained model to predict PII presence and redact.
# For simplicity, if a row is predicted to contain PII, we'll redact common PII patterns.

def redact_pii(text):
    """Redacts common PII patterns from text."""
    text = re.sub(email_pattern, '[EMAIL_REDACTED]', text)
    text = re.sub(phone_pattern, '[PHONE_REDACTED]', text)
    # More sophisticated name redaction would require NER
    # For this demo, we'll just redact the detected name-like pattern if it was the primary PII
    # This is a heuristic and not a robust NER solution.
    if re.search(name_pattern, text) and (re.search(email_pattern, text) is None and re.search(phone_pattern, text) is None):
         text = re.sub(name_pattern, '[NAME_REDACTED]', text, count=1) # Redact first occurrence
    return text

if pii_classifier: # Only predict if classifier was trained
    df['predicted_contains_pii'] = pii_classifier.predict(X_pii)
else:
    df['predicted_contains_pii'] = df['contains_pii_label'] # Use dummy labels if no training

cleaned_texts = []
for index, row in df.iterrows():
    original_text = row['text_column']
    if row['predicted_contains_pii'] == 1:
        cleaned_texts.append(redact_pii(original_text))
    else:
        cleaned_texts.append(original_text)

df['text_column_pii_cleaned'] = cleaned_texts
print("\nDataFrame after PII Cleaning (Redaction - first 5 rows):")
print(df[['text_column', 'text_column_pii_cleaned', 'predicted_contains_pii']].head())
print("-" * 50)

# --- 5. Additional Text Cleaning: Spam and Typo Handling ---

def remove_excess_spam(text):
    """Removes excess character spam and non-standard symbols."""
    # Ensure text is a string
    text = str(text)
    # Replace sequences of 3 or more identical characters with a single instance
    text = re.sub(r'(.)\1{2,}', r'\1', text)
    # Remove characters that are not alphanumeric, spaces, or common punctuation
    text = re.sub(r'[^a-zA-Z0-9\s.,!?;:]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Initialize spell checker
spell = SpellChecker()

def handle_typos(text):
    """Attempts to correct typos using a spell checker."""
    # Ensure text is a string
    text = str(text)
    words = word_tokenize(text)
    corrected_words = []
    for word in words:
        # Only attempt to correct if the word is not in dictionary and is longer than 2 chars
        # This avoids over-correcting abbreviations or very short words
        if not spell.unknown([word]) and len(word) > 2:
            # Get the most likely correction
            corrected_word = spell.correction(word)
            # If a correction is found and it's different, use it.
            # Add a simple check to ensure the correction isn't drastically different
            # (e.g., to avoid correcting proper nouns that aren't in the dictionary)
            if corrected_word and corrected_word != word and spell.distance(word, corrected_word) <= 2:
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)
        else:
            corrected_words.append(word)
    return " ".join(corrected_words)

# Apply spam and typo cleaning
df['text_column_cleaned_final'] = df['text_column_pii_cleaned'].apply(remove_excess_spam)
df['text_column_cleaned_final'] = df['text_column_cleaned_final'].apply(handle_typos)


print("\nDataFrame after Spam and Typo Cleaning (first 5 rows):")
print(df[['text_column_pii_cleaned', 'text_column_cleaned_final']].head(10)) # Show more to see effect
print("-" * 50)


# --- 6. Sentence Tokenization and Descriptor Classification Setup ---
# Now, we'll work on identifying full sentences as descriptors.
# We'll create a new dataframe where each row is a sentence.

sentences = []
original_row_indices = []

for idx, text in enumerate(df['text_column_cleaned_final']): # Use the final cleaned text
    sents = sent_tokenize(str(text)) # Ensure text is string
    for s in sents:
        sentences.append(s)
        original_row_indices.append(idx)

sentences_df = pd.DataFrame({
    'sentence': sentences,
    'original_row_index': original_row_indices
})

if sentences_df.empty:
    print("No sentences found after PII cleaning. Cannot proceed with descriptor classification.")
    cleaned_df_final = pd.DataFrame(columns=['id_column', 'cleaned_descriptors'])
else:
    # Feature Engineering for Descriptor Classification
    # Features could include: sentence length, presence of certain keywords, POS tags.
    # For simplicity, we'll use TF-IDF and sentence length.

    # TF-IDF features
    tfidf_vectorizer = TfidfVectorizer(max_features=100)
    tfidf_features = tfidf_vectorizer.fit_transform(sentences_df['sentence']).toarray()
    tfidf_feature_names = [f'tfidf_{i}' for i in range(tfidf_features.shape[1])]
    tfidf_df = pd.DataFrame(tfidf_features, columns=tfidf_feature_names)

    sentences_df = pd.concat([sentences_df, tfidf_df], axis=1)

    # Sentence length feature
    sentences_df['sentence_length'] = sentences_df['sentence'].apply(len)

    # Simulate 'is_descriptor' label
    # In a real scenario, this would be a human-labeled dataset.
    # We'll label sentences based on arbitrary criteria (e.g., length, absence of certain words).
    # For demo: sentences about product features, project scope, analytics, algorithms are descriptors.
    # Sentences with redacted PII are not.
    # For actual CSV data, you would need to provide a 'is_descriptor_label' column
    # or implement a more sophisticated labeling strategy.
    if 'is_descriptor_label' not in sentences_df.columns:
        print("\nWarning: 'is_descriptor_label' not found. Generating dummy labels for descriptor classification training.")
        # This is a very simplistic way to generate labels for new data.
        # In a real scenario, you would need actual labels for supervised training.
        sentences_df['is_descriptor_label'] = sentences_df['sentence'].apply(
            lambda s: 1 if not any(re.search(pattern, s) for pattern in ['[EMAIL_REDACTED]', '[PHONE_REDACTED]', '[NAME_REDACTED]']) and len(s) > 20 else 0
        )

    print("\nSentences DataFrame with Features and Labels for Descriptor Classification (first 5 rows):")
    print(sentences_df[['sentence', 'sentence_length', 'is_descriptor_label']].head())
    print("-" * 50)

    # --- 7. Train Random Forest for Descriptor Classification ---
    # Combine all features for descriptor classification
    X_descriptor = sentences_df.drop(['sentence', 'original_row_index', 'is_descriptor_label'], axis=1)
    y_descriptor = sentences_df['is_descriptor_label']

    if len(sentences_df) < 2 or len(y_descriptor.unique()) < 2:
        print("Not enough data or only one class for descriptor classification. Skipping model training.")
        descriptor_classifier = None
    else:
        X_train_desc, X_test_desc, y_train_desc, y_test_desc = train_test_split(
            X_descriptor, y_descriptor, test_size=0.3, random_state=42, stratify=y_descriptor
        )

        descriptor_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        descriptor_classifier.fit(X_train_desc, y_train_desc)

        y_pred_desc = descriptor_classifier.predict(X_test_desc)
        print("\nDescriptor Classification Model Performance:")
        print(f"Accuracy: {accuracy_score(y_test_desc, y_pred_desc):.2f}")
        print(classification_report(y_test_desc, y_pred_desc))
        print("-" * 50)

    # --- 8. Apply Descriptor Classification and Reconstruct Cleaned Data ---
    if descriptor_classifier:
        sentences_df['predicted_is_descriptor'] = descriptor_classifier.predict(X_descriptor)
    else:
        sentences_df['predicted_is_descriptor'] = sentences_df['is_descriptor_label'] # Use dummy labels if no training

    final_cleaned_data = {}
    for idx in df['id_column'].unique():
        final_cleaned_data[idx] = []

    for index, row in sentences_df.iterrows():
        if row['predicted_is_descriptor'] == 1:
            original_row_idx = row['original_row_index']
            original_id = df.loc[original_row_idx, 'id_column']
            final_cleaned_data[original_id].append(row['sentence'])

    # Reconstruct the cleaned DataFrame
    cleaned_output_rows = []
    for id_val, sents in final_cleaned_data.items():
        cleaned_output_rows.append({
            'id_column': id_val,
            'cleaned_descriptors': " ".join(sents)
        })

    cleaned_df_final = pd.DataFrame(cleaned_output_rows)

print("\nFinal Cleaned DataFrame with Descriptors (Random Forest Version):")
print(cleaned_df_final)
print("-" * 50)
