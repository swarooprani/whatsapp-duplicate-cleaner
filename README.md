
# WhatsApp Duplicate Cleaner

A Python utility to detect and manage duplicate files from your WhatsApp backups.  
This project helps you organize your Photos, Documents, and Videos by identifying duplicate content.


## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Sample Data](#sample-data)  
6. [Example Output](#example-output)  
7. [Contributing](#contributing)  
8. [License](#license)  
9. [Contact](#contact)

---

## Project Overview

WhatsApp backups often contain duplicate files due to multiple downloads, forwards, or automatic saves.  
This project demonstrates a Python solution to detect duplicate files based on their content, not just filenames, and provides insights about your backup storage.

We use a **hash-based approach**: files with identical content get the same hash, so duplicates can be easily identified.

---

## Features

- Detect duplicates across different folders (Photos, Documents, Videos).  
- Works on filenames with slight variations like `(1)`, `copy`, or `WA0001`.  
- Provides a summary of duplicates for cleanup.  
- Fully local – no need to upload files online.  
- Easy to extend for larger datasets.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/swarooprani/whatsapp-duplicate-cleaner.git
cd whatsapp-duplicate-cleaner
````

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate       # Linux / Mac
venv\Scripts\activate          # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> **Dependencies:** `hashlib`, `os` (standard Python modules, no external packages needed)

---

## Usage

1. Place your backup folder in the repository (or point to its path).
   Example structure:

```
sample_backup/
├── Photos/
├── Documents/
├── Videos/
```

2. Run the script:

```bash
python find_duplicates.py
```

3. View the output: list of duplicate files grouped by their content.

---

## Sample Data

Example backup structure for testing:

```
sample_backup/
├── Photos/
│   ├── IMG_20250101.txt          (content: "Holiday photo")
│   ├── IMG-20250101-WA0001.txt   (duplicate)
│   ├── IMG_20250102.txt          (content: "Office party")
│   ├── IMG_20250102 (1).txt      (duplicate)
├── Documents/
│   ├── Report.txt                (content: "Annual Report 2025")
│   ├── Report (1).txt            (duplicate)
├── Videos/
│   ├── Meeting.txt               (content: "Project meeting recording")
│   ├── Meeting (copy).txt        (duplicate)
```

---

## Example Output

```
Duplicate files found:

Hash: 3a7bd3f...
- sample_backup/Photos/IMG_20250101.txt
- sample_backup/Photos/IMG-20250101-WA0001.txt

Hash: 5b2f9c1...
- sample_backup/Photos/IMG_20250102.txt
- sample_backup/Photos/IMG_20250102 (1).txt

Hash: a1c7e92...
- sample_backup/Documents/Report.txt
- sample_backup/Documents/Report (1).txt

Hash: f9d8e13...
- sample_backup/Videos/Meeting.txt
- sample_backup/Videos/Meeting (copy).txt
```

---

## Contributing

Contributions, suggestions, and improvements are welcome!
To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make changes and commit (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.
