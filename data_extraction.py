import re

def extract_data(input_string):
    patterns = {
        "Email Addresses": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        "URLs": r'https?://(?:[a-zA-Z0-9.-]+)\.[a-zA-Z]{2,}(?:/[\w/.-]*)?',
        "Phone Numbers": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
        "Currency Amounts": r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    }
    results = {}
    for data_type, pattern in patterns.items():
        matches = re.findall(pattern, input_string)
        results[data_type] = matches if matches else ["None found"]
    return results

def display_results(results):
    for data_type, matches in results.items():
        print(f"\n{data_type}:")
        for i, match in enumerate(matches, 1):
            print(f"  {i}. {match}")

sample_input = """
Contact us at user@example.com or john.doe@alustudent.com.
Visit our sites: https://www.example.com and https://alu.africa/about.
Call us at (123) 456-7890 or 123-456-7890 or 123.456.7890.
Prices: $19.99, $1,234.56, and $500.00.
Invalid data: user@com, http://, 123-456, $19
"""

if __name__ == "__main__":
    results = extract_data(sample_input)
    display_results(results)