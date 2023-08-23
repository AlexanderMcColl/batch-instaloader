import pandas as pd
import os

df = pd.read_csv('df.csv')

# get the number of rows that have a link in them
totalposts = df[df["link"].notnull()].shape[0]

# print to the console what's going to happen and about how long it will take (on my terrible internet)
os.system(f'echo Going to download {totalposts} posts. This will take approximately {totalposts * 10} seconds or {totalposts / 6} minutes.')
os.system('echo Remember you can ctrl+c at any time to halt this process.')

for ind in df.index:
    link = df['link'][ind]
    title = df['title'][ind]
    subfolder = df['subfolder'][ind]
    cmd = f'instaloader --dirname-pattern="{subfolder}" --filename-pattern="{title}" -- -{link}'
    link_check = ''
    # don't download the same post twice
    if link_check == link:
        continue
    # don't download posts that don't have all required information
    elif not link or not title or not subfolder or not cmd:
        continue
    else:
        os.system(cmd)
    link_check = link