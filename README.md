# batch-instaloader

Very simple python script to batch instaloader downloads on Linux
Uses shell commands so you get real time updates in the shell of what it's doing.

# Requirements

Instaloader: https://instaloader.github.io/
https://github.com/instaloader/instaloader

Pandas (any version)

# Templates

Copy the Google Sheets template from here:
https://docs.google.com/spreadsheets/d/14oC_ZjHHk_nnnS6YYvPz4jUb-igfXLkZKlfSRS8gy8o/edit?usp=sharing

# Usage

1. Clone the repo.
2. Fill out the user editable areas of the Google Sheet as you browse Instagram.
   (The sheet will cleanse and validate your data.
   You can keep blank rows to store a list of subfolder names, they get skipped by the script).
3. File > Download > Comma-separated values (.csv). Name it `df.csv`.
4. Run the script.
   ```
   python batchinsta.py
   python3 batchinsta.py
   python .\batchinsta.py
   ```
5. Watch for any errors or warnings and act on them as necessary.
6. Delete df.csv, clear the Sheet and fill it up again.
7. Periodically delete all the extra fluff that gets downloaded;
   search for .json, .jpg (careful of unintentional image deletions).
