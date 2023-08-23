import pandas as pd
import os

df = pd.read_csv('df.csv')

for ind in df.index:
    link = df['link'][ind]
    title = df['title'][ind]
    subfolder = df['subfolder'][ind]
    cmd = f'instaloader --dirname-pattern="{subfolder}" --filename-pattern="{title}" -- -{link}'
    os.system(cmd)