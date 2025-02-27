import pandas as pd
import re
import json
import os

class FalsePositiveDetector:
    def __init__(self, false_positive_keywords=None):
        # Define default keywords for false positives
        self.false_positive_keywords = false_positive_keywords or [
            "forgot", "reset", "change", "update", "policy", "field", "empty", "strength",
            "weak", "expired", "incorrect", "example", "default", "case-sensitive", "required",
            "confirm", "share", "write down", "compromised", "common", "recovery", "link", "sent"
        ]

    def is_false_positive(self, text):
        """
        Check if the given text is a false positive.
        """
        # Convert text to lowercase for case-insensitive matching
        text_lower = text.lower()

        # Check if the text contains any of the false positive keywords
        for keyword in self.false_positive_keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                return True  # Text is a false positive

        return False  # Text is not a false positive

    def gather_false_positives(self, input_file, output_file, column_name="text"):
        """
        Gather false positives from an Excel file and save them to a JSON file.
        """
        # Read the Excel file
        df = pd.read_excel(input_file)

        # Initialize a list to store new false positives
        new_false_positives = []

        # Iterate over the rows in the specified column
        for text in df[column_name]:
            if pd.notna(text) and self.is_false_positive(text):
                new_false_positives.append(text)

        # Load existing false positives from the JSON file (if it exists)
        existing_false_positives = []
        if os.path.exists(output_file):
            with open(output_file, 'r') as json_file:
                existing_false_positives = json.load(json_file)

        # Add only new false positives (ignore duplicates)
        for false_positive in new_false_positives:
            if false_positive not in existing_false_positives:
                existing_false_positives.append(false_positive)

        # Save the updated list of false positives to the JSON file
        with open(output_file, 'w') as json_file:
            json.dump(existing_false_positives, json_file, indent=4)

        print(f"False positives gathered and saved to {output_file}")