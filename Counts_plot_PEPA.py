#!/usr/bin/env python
# coding: utf-8

# In[53]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from matplotlib.pyplot import figure, draw
sns.set(style="white")

df = pd.read_csv("https://raw.githubusercontent.com/kimpar/THL_densityplot/master/kuntien_kustannukset2018.csv", sep=";")
fn = Path('/Users/kimmoparhiala/Python_projects/thl_counts_valve.svg').expanduser()

#print(df.head(5))

df_counts = df.groupby(['vaestonmuutos_lk', 'Yhteensä']).size().reset_index(name='counts')

df2 = pd.DataFrame(np.array([[1, 2988], [2,3373], [3, 3298], [4, 3563], [5, 4128], [6, 3621], [7, 4763]]),
                   columns=['med1','med2'])

df_counts2 = df2.groupby(['med1', 'med2']).size().reset_index(name='counts')        
visu = ['#519b2f', '#94be7b', '#b8ceae', '#dcdfe2', '#d2aabd','#c97498', '#be3f72']

fig, ax = plt.subplots(figsize=(20,11), dpi= 80)    
sns.stripplot(df_counts.vaestonmuutos_lk, df_counts.Yhteensä, size=df_counts.counts*15, dodge=False, palette='viridis_r', linewidth=0, ax=ax, jitter=0.25, facecolor='white')

#keskiarvot
#sns.stripplot(df_counts2.med1, df_counts2.med2, size=df_counts2.counts*100, marker="_", color='black', linewidth=5, ax=ax, jitter=0, facecolor='white')

plt.title('Kuntien sosiaali- ja terveydenhuollon kustannukset kuntaluokissa, viiden vuoden väestönmuutos (2018)', fontsize=24, fontname="Arial")
plt.xticks(rotation='0', fontsize=22, fontname="Arial")
plt.yticks(fontsize=22, fontname="Arial")
plt.ylabel("€ / asukas", fontsize=24, rotation=90)

#luvut = ['> 100 000','40 000 - 100 000', '20 000 - 40 000', '10 000 - 20 000', '5 000 - 10 000', '2 000 - 5 000', '< 2 000'] 
kuvaajat = ['Nopeasti kasvavat', 'Kasvavat', 'Väestöään menettävät', 'Väestöään nopeasti menettävät']

plt.gca().set_xticklabels(kuvaajat)

plt.axhline(y=3319, color='black', linestyle='--')
ax.set_xlabel("")

plt.legend(["Koko maan keskiarvo, € / asukas"], handlelength=2.2, loc='upper left', fontsize=24)
plt.show()
#plt.draw()
#plt.savefig(fn, bbox_inches='tight')


# In[ ]:





# In[ ]:




