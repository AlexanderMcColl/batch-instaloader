import pandas as pd
import os
import sys

df = pd.read_csv('df.csv')

for ind in df.index:
    link = df['link'][ind]
    title = df['title'][ind]
    subfolder = df['subfolder'][ind]
    cmd = f'instaloader --dirname-pattern="{subfolder}" --filename-pattern="{title}" -- -{link}'
    if cmd_check == cmd:
        sys.exit("script was going to run the same cmd again. Exited instead")
    elif not link or not title or not subfolder or not cmd:
        sys.exit("script was going to run with empty commands. Exited instead")
    else:
        os.system(cmd)
    cmd_check = cmd