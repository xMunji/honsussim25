import csv
import argparse
import sys

def clean_text_field(text: str) -> str:
    """
    Cleans a text field by keeping only basic English letters, numbers,
    common punctuation, and essential whitespace.
    Removes other characters and normalizes whitespace.
    """
    if not isinstance(text, str):
        # In case a field is not a string (e.g., already a number type from CSV reader)
        # though CSV reader usually gives strings.
        return str(text)

    allowed_chars = []
    for char_code in [ord(c) for c in text]:
        # Allow ASCII letters (A-Z, a-z)
        if (65 <= char_code <= 90) or \
           (97 <= char_code <= 122):
            allowed_chars.append(chr(char_code))
        # Allow digits (0-9)
        elif (48 <= char_code <= 57):
            allowed_chars.append(chr(char_code))
        # Allow space, newline. Convert tab to space.
        elif char_code == 32: # space
            allowed_chars.append(' ')
        elif char_code == 10: # newline
            allowed_chars.append('\n')
        elif char_code == 9:  # tab
            allowed_chars.append(' ') # Convert tab to space
        # Allow common punctuation: . , ! ? - + ( ) ; : ' " /
        elif char_code in [
            46,  # .
            44,  # ,
            33,  # !
            63,  # ?
            45,  # -
            43,  # +
            40,  # (
            41,  # )
            59,  # ;
            58,  # :
            39,  # '
            34,  # "
            47,  # /
        ]:
            allowed_chars.append(chr(char_code))
        # Else: character is skipped (e.g., ï, , º, â, •, etc.)

    cleaned_text = "".join(allowed_chars)

    # Normalize whitespace:
    # 1. Split into lines
    # 2. For each line, strip leading/trailing whitespace and collapse multiple spaces within the line
    # 3. Join lines back with newline, filtering out any completely empty lines
    lines = cleaned_text.split('\n')
    normalized_lines = []
    for line in lines:
        # Remove leading/trailing whitespace from the line and collapse multiple spaces
        normalized_line = ' '.join(filter(None, line.strip().split(' ')))
        normalized_lines.append(normalized_line)
    
    # Join lines, but filter out any completely empty lines that might result 
    # from original all-whitespace lines or lines that became empty after character stripping.
    final_text = '\n'.join(filter(None, normalized_lines))
    
    return final_text

def process_csv(input_filepath: str, output_filepath: str, delimiter: str):
    """
    Reads a CSV file, cleans each field, and writes to an output CSV file.
    """
    try:
        # Note: It's important that the input file is read with an encoding
        # that can represent its actual content. UTF-8 is a good default.
        # If you encounter issues, you might need to specify a different encoding
        # like 'latin-1' or 'cp1252' if your file uses those.
        with open(input_filepath, mode='r', newline='', encoding='utf-8') as infile, \
             open(output_filepath, mode='w', newline='', encoding='utf-8') as outfile:

            # Handle potential single-character escaped delimiters like '\t'
            if delimiter == '\\t':
                delimiter_char = '\t'
            elif len(delimiter) == 1:
                delimiter_char = delimiter
            else:
                raise ValueError(f"Delimiter must be a single character or '\\t'. Got: {delimiter}")

            reader = csv.reader(infile, delimiter=delimiter_char)
            writer = csv.writer(outfile, delimiter=delimiter_char, quoting=csv.QUOTE_MINIMAL)

            # Process header row
            try:
                header = next(reader)
                cleaned_header = [clean_text_field(field) for field in header]
                writer.writerow(cleaned_header)
            except StopIteration:
                print("Warning: Input CSV file is empty or has no header.", file=sys.stderr)
                return # Nothing more to do for an empty file
            except Exception as e:
                print(f"Error processing header: {e}", file=sys.stderr)
                # Decide if you want to stop or continue without a header
                return


            # Process data rows iteratively
            row_count = 0
            for row in reader:
                cleaned_row = [clean_text_field(field) for field in row]
                writer.writerow(cleaned_row)
                row_count += 1
                if row_count % 1000 == 0: # Optional: progress update for large files
                    print(f"Processed {row_count} rows...", file=sys.stderr)
            
            print(f"Successfully cleaned {row_count + 1} total rows (including header).")
            print(f"Output written to: {output_filepath}")

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_filepath}'", file=sys.stderr)
        sys.exit(1)
    except ValueError as ve:
        print(f"Configuration error: {ve}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Clean CSV data by retaining basic English characters and normalizing text.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("output_file", help="Path to save the cleaned CSV file.")
    parser.add_argument("-d", "--delimiter", default=",",
                        help="Delimiter character used in the CSV file (e.g., ',', ';', '\\t' for tab). Default is comma.")

    args = parser.parse_args()

    process_csv(args.input_file, args.output_file, args.delimiter)

if __name__ == "__main__":
    main()

"""
How to use this script:

1.  Save the code: Save the code above as a Python file (e.g., `csv_cleaner.py`).
2.  Open your terminal or command prompt.
3.  Run the script with the following command structure:

    python csv_cleaner.py <path_to_input_csv> <path_to_output_csv> [options]

Examples:

* Cleaning a comma-delimited CSV:
    python csv_cleaner.py input.csv cleaned_output.csv

* Cleaning a semicolon-delimited CSV:
    python csv_cleaner.py data.csv cleaned_data.csv -d ";"

* Cleaning a tab-delimited CSV (TSV):
    python csv_cleaner.py source_data.tsv cleaned_source_data.tsv -d "\\t"
    (Note: Depending on your shell, you might need to quote the tab delimiter, e.g., -d $'\t' on bash/zsh, or ensure Python interprets \\t correctly)

The script will:
- Read your input CSV.
- Clean each field according to the rules (keeping basic English letters, numbers, specified punctuation, and normalizing whitespace).
- Write the cleaned data to your specified output CSV file.
- Print status messages or errors to the console.

Regarding your example string:
Input: "ïº\nPlanet, Place,\nPurpose\nâ€¢ Share your name + discipline..."
The cleaning function aims to produce something like:
"Planet, Place,\nPurpose\nShare your name + discipline..."
(after removing the non-standard characters and normalizing whitespace).
"""
