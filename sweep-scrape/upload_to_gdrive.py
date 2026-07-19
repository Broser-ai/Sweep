"""
Upload sweep-scrape zip files to Google Drive folder.
Requires: pip install google-api-python-client google-auth-oauthlib
Run: python upload_to_gdrive.py
"""
import os
import subprocess

FOLDER_ID = "1bb0-Orv0pfSZpivMZp5afrMwI2fSfsrT"
FILES = [
    "sweep-html-pages.zip",
    "sweep-text-extracts.zip",
    "sweep-code-analysis.zip",
    "sweep-net-complete.zip",
    "deep-research-1-esg-platforms.json",
]
BASE = r"C:\Users\Ambro2\sweep-scrape"

print("Uploading zip files to Google Drive...")
print(f"Target folder ID: {FOLDER_ID}")
print(f"Target folder URL: https://drive.google.com/drive/folders/{FOLDER_ID}")
print()

for f in FILES:
    path = os.path.join(BASE, f)
    if not os.path.exists(path):
        print(f"SKIP (not found): {f}")
        continue
    size_mb = os.path.getsize(path) / 1024 / 1024
    print(f"Ready to upload: {f} ({size_mb:.1f} MB)")

print()
print("--- MANUAL UPLOAD INSTRUCTIONS ---")
print(f"1. Open: https://drive.google.com/drive/folders/{FOLDER_ID}")
print("2. Drag and drop the following files from:")
print(f"   {BASE}")
print("3. Files to upload:")
for f in FILES:
    path = os.path.join(BASE, f)
    if os.path.exists(path):
        print(f"   - {f}")
