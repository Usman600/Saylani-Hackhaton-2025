import re

def parse_lab_results(text):
    results = []
    test_keywords = ["hemoglobin", "glucose", "wbc", "rbc", "platelet", "cholesterol", "creatinine", "bilirubin", "sugar", "blood", "urine"]

    lines = text.lower().split('\n')

    current_test = None
    description = ""

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Try to detect a new test by checking for keywords
        if any(keyword in line for keyword in test_keywords):
            if current_test:
                results.append(current_test)
            current_test = {"test_name": line, "value": "N/A", "normal_range": "N/A", "description": ""}

        elif current_test:
            # Add line as description
            current_test["description"] += " " + line

            # Try to extract normal range if present
            range_match = re.search(r'normal.*?(range|value).*?:?\s*([\d.,\-–]+.*)', line, re.IGNORECASE)
            if range_match:
                current_test["normal_range"] = range_match.group(2)

    if current_test:
        results.append(current_test)

    return results
