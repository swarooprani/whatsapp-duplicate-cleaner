import os

# Folder structure
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

for path, content in files.items():
    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

print("✅ Sample backup folder with duplicates created!")
