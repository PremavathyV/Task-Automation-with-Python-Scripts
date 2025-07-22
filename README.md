
# 📧 Email Extractor - Task Automation with Python

## 📌 Description
This project is a **Python-based task automation script** that extracts email addresses from files such as `.txt`, `.pdf`, or `.docx`. It's a helpful utility for filtering and collecting email IDs from large documents, making it ideal for marketing, research, or data processing purposes.

## 🚀 Features
- Extract emails from:
  - ✅ Plain Text files (`.txt`)
  - ✅ Word Documents (`.docx`)
  - ✅ PDF Files (`.pdf`)
- Uses Regular Expressions (`re`) to match email patterns
- Clean and well-organized script structure
- Supports batch processing of multiple files in a folder

## 🛠️ Technologies Used
- 🐍 Python 3
- `re` module for regex
- `os` for file handling
- `PyPDF2` for PDF parsing
- `python-docx` for `.docx` reading

## 📂 Project Structure
```
email_extractor/
├── email_extractor.py
├── sample_files/
│   ├── file1.txt
│   ├── file2.pdf
│   └── file3.docx
└── README.md
```

## ▶️ How to Run the Script

### Step 1: Install Required Libraries
```bash
pip install PyPDF2 python-docx
```

### Step 2: Run the Script
```bash
python email_extractor.py
```

### Step 3: View Output
Extracted email addresses will be printed in the terminal or saved to a `.csv` or `.txt` file if configured.

## 🧠 How It Works
- Reads content from selected files
- Applies a regex pattern to extract valid emails
- Displays or stores the results

## ✍️ Author
**Premavathy V**  
Let’s connect on [LinkedIn](www.linkedin.com/in/premavathy-vijayan-921a39252)

