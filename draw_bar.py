# import libraries
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import string
import argparse
#%matplotlib inline

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica'

# set the style of the axes and the text color
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'
plt.rcParams['text.color']='#333F4B'




parser = argparse.ArgumentParser(description='Draw Bar')
parser.add_argument('--csv', default='input.csv', help='input file separted by \'\\t\' ')
parser.add_argument('--fig', default='out.png', help='the output figure')

args = parser.parse_args()

csv_file = unicode(args.csv)
fig_file = unicode(args.fig)

fin = open(csv_file,"r")
cpt_list = []
val_list = []
for line in fin:
	line = line.strip()
	cpt, val = line.split("\t")
	val_list.append(string.atoi(val))
	cpt_list.append(cpt)  
fin.close()

percentages = pd.Series(val_list, 
                        index=cpt_list)

df = pd.DataFrame({'percentage' : percentages})
df = df.sort_values(by='percentage')

# we first need a numeric placeholder for the y axis
my_range=list(range(1,len(df.index)+1))

fig, ax = plt.subplots(figsize=(10,25))

# create for each expense type an horizontal line that starts at x = 0 with the length 
# represented by the specific expense percentage value.
plt.hlines(y=my_range, xmin=0, xmax=df['percentage'], color='#007ACC', alpha=0.2, linewidth=5)

# create for each expense type a dot at the level of the expense percentage value
plt.plot(df['percentage'], my_range, "o", markersize=5, color='#007ACC', alpha=0.6)

# set labels
ax.set_xlabel('Coverage', fontsize=15, fontweight='black', color = '#333F4B')
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top() 
#ax.set_ylabel('')

# set axis
ax.tick_params(axis='both', which='major', labelsize=12)
plt.yticks(my_range, df.index)

# add an horizonal label for the y axis 
#fig.text(-0.23, 0.86, 'Concept Coverage (Fulltext)', fontsize=15, fontweight='black', color = '#333F4B')

# change the style of the axis spines
ax.spines['bottom'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['top'].set_smart_bounds(True)

'''
# set the spines position
ax.spines['bottom'].set_position(('axes', -0.04))
ax.spines['left'].set_position(('axes', 0.015))
'''
plt.savefig(fig_file, dpi=300, bbox_inches='tight')
