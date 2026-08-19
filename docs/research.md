# GuardX Research

## 1. Research Objective

GuardX wants to study how everyday pictures can inadvertently reveal personal or private information before they are shared online.

The research focuses on information that can be directly seen in an image, as well as information that is embedded in the image file.

---

## 2. Privacy-Sensitive Information

GuardX will investigate the detection of:

- Faces
- Phone numbers
- Email addresses
- Addresses
- Vehicle registration numbers
- Identity documents
- Tickets and boarding passes
- Receipts
- QR codes and barcodes
- Computer and mobile screens
- Street signs and house numbers
- Location-related visual clues
- EXIF metadata such as GPS, date/time, camera information and software details

---

## 3. Analysis Approach

GuardX will use multiple analysis layers rather than depending on a single detection technique.

### File-Level Analysis
Examine image metadata such as EXIF information.

### Visual Analysis
Identify objects, faces, screens, documents and other potentially sensitive regions.

### Text Analysis
Use OCR to identify visible text such as phone numbers, emails, addresses and identifiers.

### Contextual Analysis
Consider combinations of detected information that may increase privacy exposure.

---

## 4. Protection Approach

When sensitive information is detected, GuardX will investigate privacy-preserving actions such as:

- Metadata removal
- Face blurring
- Number-plate blurring
- Sensitive-text redaction
- QR/barcode redaction
- Sanitized image generation

---

## 5. Verification

After protection, the sanitized image should be analyzed again.

GuardX will compare:

BEFORE → Detected privacy-sensitive information

PROTECTION → Applied privacy-preserving actions

AFTER → Remaining detectable information

The goal is to verify the effectiveness of the protection instead of assuming that the image is automatically safe.

---

## 6. Research Questions

- What privacy-sensitive information can be extracted from ordinary images?
- Which information can be detected using computer vision?
- Which information requires OCR or document analysis?
- What hidden information can be obtained from image metadata?
- How can contextual clues contribute to privacy exposure?
- Which modern AI/computer-vision approaches are suitable?
- How can detected information be protected?
- How can sanitization effectiveness be verified?

---

## 7. Current Status

Research and technology selection are currently in progress.

Implementation will begin after the major detection and protection components have been evaluated.