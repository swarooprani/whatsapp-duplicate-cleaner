import os
import hashlib
import shutil

# Function to create hash for each file
def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        # read in chunks for large files
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def remove_duplicates(folder):
    seen_hashes = {}
    duplicates_folder = os.path.join(folder, "Duplicates")

    if not os.path.exists(duplicates_folder):
        os.makedirs(duplicates_folder)

    for root, _, files in os.walk(folder):
        # Skip the duplicates folder itself
        if root.startswith(duplicates_folder):
            continue

        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)

            if file_hash in seen_hashes:
                print(f"Duplicate found: {file} → moving to Duplicates/")
                shutil.move(file_path, os.path.join(duplicates_folder, file))
            else:
                seen_hashes[file_hash] = file_path

if __name__ == "__main__":
    folder = "sample_backup"
    remove_duplicates(folder)
    print("Duplicate check complete. Duplicates moved to 'Duplicates/' folder.")
