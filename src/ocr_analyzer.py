import pytesseract
from PIL import Image
import re


def analyze_ocr(image_path):
    """
    Extract visible text from an image and identify
    potentially privacy-sensitive information.
    """

    try:
        image = Image.open(image_path)

        # Extract text using OCR
        extracted_text = pytesseract.image_to_string(image).strip()

        if not extracted_text:
            return {
                "text_found": False,
                "extracted_text": "",
                "sensitive_data": []
            }

        sensitive_data = []

        # Detect email addresses
        if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
                     extracted_text):
            sensitive_data.append("Email address")

        # Detect phone numbers
        if re.search(r'\b(?:\+91[-\s]?)?[6-9]\d{9}\b',
                     extracted_text):
            sensitive_data.append("Phone number")

        # Detect common identity-related keywords
        keywords = [
            "name",
            "address",
            "date of birth",
            "dob",
            "aadhar",
            "aadhaar",
            "pan",
            "passport",
            "license",
            "account number"
        ]

        lower_text = extracted_text.lower()

        for keyword in keywords:
            if keyword in lower_text:
                sensitive_data.append("Identity-related information")
                break

        return {
            "text_found": True,
            "extracted_text": extracted_text,
            "sensitive_data": sensitive_data
        }

    except Exception as error:
        return {
            "text_found": False,
            "extracted_text": "",
            "sensitive_data": [],
            "error": str(error)
        }


if __name__ == "__main__":

    print("\n========== GUARDX OCR ANALYSIS ==========")

    image_path = input("Enter image path: ").strip()

    result = analyze_ocr(image_path)

    if "error" in result:
        print("\nError:", result["error"])

    elif not result["text_found"]:
        print("\nNo visible text detected.")

    else:
        print("\nExtracted Text:")
        print("----------------------------------------")
        print(result["extracted_text"])

        print("\nPrivacy Analysis:")
        print("----------------------------------------")

        if result["sensitive_data"]:
            print("Potentially sensitive information detected:")

            for item in result["sensitive_data"]:
                print("-", item)

            print("\nPrivacy Status: Visible text exposure detected.")

        else:
            print("No commonly sensitive information detected.")
            print("\nPrivacy Status: No major text exposure detected.")

    print("========================================")