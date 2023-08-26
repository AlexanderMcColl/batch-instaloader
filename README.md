# batch-instaloader

Very simple python script to batch instaloader downloads on Linux.\
Uses shell commands so you get real time updates in the shell of what it's doing.

## Requirements

Instaloader: https://instaloader.github.io

Pandas (any version)

## Templates

Copy the Google Sheets template from here:\
https://docs.google.com/spreadsheets/d/14oC_ZjHHk_nnnS6YYvPz4jUb-igfXLkZKlfSRS8gy8o/edit?usp=sharing

## Usage

1. Clone the repo. Copy the Sheet to your Google Drive.
2. Fill out the user editable areas of the Google Sheet as you browse Instagram.\
   The sheet will cleanse and validate your data.\
   You can keep blank rows to store a list of subfolder names, they get skipped by the script.
3. File > Download > Comma-separated values (.csv). Name it `df.csv`.
4. Run the script.
   ```
   python batchinsta.py
   python3 batchinsta.py
   python .\batchinsta.py
   ```
5. Watch for any errors or warnings and act on them as necessary.

   ```
   Errors or warnings occurred:
   -Cu9wMVWu5Kz: Fetching Post metadata failed.
   ```

   In this case the post has been deleted or made private since you first viewed it, too bad 🤷

6. Delete `df.csv`, clear the Sheet and fill it up again.
7. Periodically delete all the extra fluff that gets downloaded;\
   Search for .json, .jpg (careful of unintentional image deletions).

## Coming next

Use Python native csv.DictReader which is apparently faster, and won't need Pandas.
