import pandas as pd
import os

# CLASSES
class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

# FUNCTIONS
#
# Accepts user input to import their csv file. Exits with an error message if the csv couldn't be imported.
# Add a while or if counter to let the user try 3 times to input their path. Show their last entered path back to them to let them edit it.
def import_csv():
    df_filepath = input('enter the full or relative path to your .csv file:\n')
    try:
        df = pd.read_csv(df_filepath)
    except:
        print(f'You entered: {bcolors.UNDERLINE}{df_filepath}{bcolors.ENDC}. {bcolors.WARNING}This file was not found.{bcolors.ENDC} Please check the filepath.')
        exit()
    return df

# Removes all rows without a link in them and any duplicate links:
def clean_csv(df):
    df = df.dropna(subset=['link']).drop_duplicates(subset=['link']).copy()
    return df

# Constructs and calls the instaloader command.
def batch_instaloader(link, title, subfolder):
    cmd = f'instaloader --dirname-pattern="{subfolder}" --filename-pattern="{title}" -- -{link}'
    return os.system(cmd)

# PROGRAM
#
# Import and clean the data. Record the number of rows going to be processed:
df = import_csv()
df = clean_csv(df)
totalposts = df.shape[0]

# print to the console what's going to happen and about how long it will take:
os.system(f'echo Going to download {totalposts} posts. This will take approximately {totalposts * 5} seconds or {round(totalposts / 12, 2)} minutes.')
os.system('echo Remember you can ctrl+c at any time to halt this process.')

# # iterate through the dataframe downloading and renaming videos and images:
for row in df.index:
    batch_instaloader(df['link'][row], df['title'][row], df['subfolder'][row])