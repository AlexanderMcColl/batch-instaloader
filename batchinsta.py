import pandas as pd
import os

df = pd.read_csv('df.csv')

# Remove all rows without a link in them and all duplicates:
# Record the number of rows going to be processed:
df = df.dropna(subset=['link']).drop_duplicates(subset=['link'])
totalposts = df.shape[0]

# The function that constraucts and calls our instaloader command:
def instaloader_cmd(link, title, subfolder):
    cmd = f'instaloader --dirname-pattern="{subfolder}" --filename-pattern="{title}" -- -{link}'
    return os.system(cmd)

# print to the console what's going to happen and about how long it will take:
os.system(f'echo Going to download {totalposts} posts. This will take approximately {totalposts * 5} seconds or {round(totalposts / 12, 2)} minutes.')
os.system('echo Remember you can ctrl+c at any time to halt this process.')

# iterate through the dataframe calling the function:
for row in df.index:
    instaloader_cmd(df['link'][row], df['title'][row], df['subfolder'][row])