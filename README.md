# WhatsApp Duplicate Cleaner 🧹

A Python script to detect and remove duplicate files in WhatsApp or mobile backup folders, helping you free up storage space and organize your media efficiently.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Sample Data](#sample-data)
5. [Usage](#usage)
6. [Example Output](#example-output)
7. [Contributing](#contributing)

---

## Project Overview

This project scans a backup folder containing WhatsApp or mobile media files and identifies duplicates based on file content. It can help you:

* Free up storage by removing duplicates
* Organize your photos, videos, and documents efficiently
* Quickly analyze backup folders without manual searching

---

## Features

* Detects duplicate files across multiple folders
* Works with Photos, Videos, and Documents
* Generates a summary of duplicates before removal
* Safe deletion (optional: only remove after confirmation)

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/swarooprani/whatsapp-duplicate-cleaner.git
cd whatsapp-duplicate-cleaner
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the script:**

```bash
python duplicate_cleaner.py
```

---

## Sample Data

The repository includes a small `sample_backup/` folder for testing.
Structure of the sample backup:

```
sample_backup/
├── Photos/
│   ├── IMG_20250101.txt
│   ├── IMG-20250101-WA0001.txt  # duplicate
│   ├── IMG_20250102.txt
│   ├── IMG_20250102 (1).txt     # duplicate
├── Documents/
│   ├── Report.txt
│   ├── Report (1).txt           # duplicate
├── Videos/
│   ├── Meeting.txt
│   ├── Meeting (copy).txt       # duplicate
```

**Note:** These are text files for demonstration. The script works similarly with actual media files.

---

## Usage

1. Place your backup folder path in the script or run it from the folder containing your backup.
2. The script will scan for duplicates across all subfolders.
3. A summary will be displayed showing duplicates for review before deletion.

---

## Example Output

```
Duplicate files found:
- sample_backup/Photos/IMG-20250101-WA0001.txt
- sample_backup/Photos/IMG_20250101.txt
- sample_backup/Documents/Report (1).txt
- sample_backup/Documents/Report.txt
- sample_backup/Videos/Meeting (copy).txt
- sample_backup/Videos/Meeting.txt

Total duplicates: 6
```

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

