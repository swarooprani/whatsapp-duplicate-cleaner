# WhatsApp Duplicate File Cleaner

## Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Solution Concept](#solution-concept)
- [Features](#features)
- [Installation](#installation)
- [Sample Data and Files](#sample-data-and-files)
- [Code](#code)
- [Example Output](#example-output)


## Project Overview

WhatsApp and other messaging apps create automatic backups that often contain duplicate files. These duplicates can waste storage space and make it harder to organize your media and documents. This Python project identifies and lists duplicate files in a backup folder, helping you clean them efficiently.

## Problem Statement

In reality, phones automatically store media and documents in backup folders. Over time, duplicates accumulate due to multiple downloads, forwards, or edits. Manual cleanup is tedious, and existing tools often don’t provide clear insights into duplicates before deletion.

## Solution Concept

This project scans a backup folder, identifies files with the same content, and lists them for review. You can then decide which duplicates to remove. The program is simple, beginner-friendly, and can be extended to automatically delete duplicates if desired.

## Features

- Identify duplicate files based on content.
- Works with any file type (text, images, videos, documents).
- Provides a clear list of duplicates grouped by their content.
- Can be extended to delete duplicates safely.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/swarooprani/whatsapp-duplicate-cleaner.git
```

## 2. Navigate to the project folder:

```bash
cd whatsapp-duplicate-cleaner
```

## 3. Make sure you have Python 3 installed. No external libraries are required.

## Sample Data and Files

Create a folder structure like this for testing:
```bash
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

You can create these files manually or programmatically using the provided script.

## Code
```bash
import os
import hashlib
from collections import defaultdict

def hash_file(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates(folder_path):
    duplicates = defaultdict(list)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            duplicates[file_hash].append(file_path)
    return {k: v for k, v in duplicates.items() if len(v) > 1}

folder = 'sample_backup'
duplicates = find_duplicates(folder)

print("Duplicate files found:")
for file_hash, files in duplicates.items():
    print("\nGroup:")
    for f in files:
        print(f"- {f}")
```
## Sample folder content:
```bash
Dictionary of files with paths and their content
files = {
    "sample_backup/Photos/IMG_20250101.txt": "Holiday photo",
    "sample_backup/Photos/IMG-20250101-WA0001.txt": "Holiday photo",   # duplicate
    "sample_backup/Photos/IMG_20250102.txt": "Office party",
    "sample_backup/Photos/IMG_20250102 (1).txt": "Office party",       # duplicate
    "sample_backup/Documents/Report.txt": "Annual Report 2025",
    "sample_backup/Documents/Report (1).txt": "Annual Report 2025",    # duplicate
    "sample_backup/Videos/Meeting.txt": "Project meeting recording",
    "sample_backup/Videos/Meeting (copy).txt": "Project meeting recording",  # duplicate
}
```
## Example Output
```bash
Duplicate found: Report.txt → moving to Duplicates/
Duplicate found: IMG_20250101.txt → moving to Duplicates/
Duplicate found: IMG_20250102.txt → moving to Duplicates/
Duplicate found: Meeting.txt → moving to Duplicates/
Duplicate check complete. Duplicates moved to 'Duplicates/' folder.


```


