import pandas as pd
import os

df = pd.read_csv('df.csv')

# get the number of rows that have a link in them
totalposts = df[df["link"].notnull()].shape[0]
link_check = ''

# print to the console what's going to happen and about how long it will take
os.system(f'echo Going to download {totalposts} posts. This will take approximately {totalposts * 5} seconds or {round(totalposts / 12, 2)} minutes.')
os.system('echo Remember you can ctrl+c at any time to halt this process.')

for ind in df[df["link"].notnull()].index:
    link = df['link'][ind]
    title = df['title'][ind]
    subfolder = df['subfolder'][ind]
    cmd = f'instaloader --dirname-pattern="{subfolder}" --filename-pattern="{title}" -- -{link}'
    # don't download the same post twice
    if link_check == link:
        continue
    else:
        os.system(cmd)
    link_check = link