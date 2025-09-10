````markdown
## WhatsApp Backup Duplicate Cleaner

A simple Python project to detect and remove **duplicate files** in WhatsApp or mobile backup folders.  
Duplicates often happen when the same photo, video, or document is saved multiple times (like `IMG_20250101.jpg` and `IMG-20250101-WA0001.jpg`).

## Features
- Scans folders for duplicate files
- Detects duplicates based on **file content**, not just file names
- Works for Photos, Videos, Documents, and more
- Includes a **sample dataset** (`sample_backup/`) for testing

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/whatsapp-duplicate-cleaner.git
   cd whatsapp-duplicate-cleaner
````

2. Make sure Python is installed (Python 3.7+ recommended)

3. Run the Python script:

   ```bash
   python duplicate_cleaner.py
   ```

4. Check the console output for detected duplicate files.

---

## 📂 Sample Backup Folder

The repo includes a small `sample_backup/` folder with example files:

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
- sample_backup/Photos/IMG_20250101.txt
- sample_backup/Photos/IMG-20250101-WA0001.txt
- sample_backup/Photos/IMG_20250102.txt
- sample_backup/Photos/IMG_20250102 (1).txt
- sample_backup/Documents/Report.txt
- sample_backup/Documents/Report (1).txt
- sample_backup/Videos/Meeting.txt
- sample_backup/Videos/Meeting (copy).txt
```

---

## Notes

* Only reads the content of files to check duplicates
* Does not delete files automatically (you can add that functionality later)
* Works on any folder structure, not just WhatsApp backups
