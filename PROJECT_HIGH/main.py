from false_positive_detector import FalsePositiveDetector

# Example usage
if __name__ == "__main__":
    # Initialize the FalsePositiveDetector
    detector = FalsePositiveDetector()

    # Define file paths
    input_file = "input.xlsx"  # Replace with your input Excel file path
    output_file = "false_positives.json"  # Replace with your desired output JSON file path
    column_name = "text"  # Replace with the name of the column containing the text

    # Gather false positives and save to JSON
    detector.gather_false_positives(input_file, output_file, column_name)