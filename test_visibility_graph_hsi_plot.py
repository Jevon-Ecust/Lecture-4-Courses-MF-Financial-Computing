from visibility_graph import visibility_graph
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns

data=np.loadtxt('Vec_HSI_Network.txt',skiprows=1)
# data_zs=data[1:len(data),:]
print(data)
data=data[:,1:]
data=data.T
data=pd.DataFrame(data)

corr = data.corr()
cmap = sns.diverging_palette(230, 20, as_cmap=True)
# sns.heatmap(corr,cmap=cmap)


df = pd.read_csv('HSI-s.csv')
data=df
# data = df[(df.datadate >= 20200101) & (df.datadate <= 20210101)]

print(data)
data=data.sort_values(['datadate','tic'])
series = data['prcld']
date = data['datadate']

date = date[1:-1]
# date=list(date)
# date=date[:,2:]
print(date)
plt.axes([0.2, 0.2, 0.7, 0.7])
# fig, ax = plt.subplots()
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.imshow(corr)
plt.colorbar()
xt=np.array(range(0,len(date),50))

plt.xticks(xt,date[0:len(date):50],rotation=60)
plt.yticks(xt,date[0:len(date):50])


    # Draw each cell as a scatter point with varying size and color

# corr_mat = data.corr().stack().reset_index(name="correlation")
# sns.set_theme(style="whitegrid")
# g = sns.relplot(
# data=corr_mat,    
# x="level_0", y="level_1", hue="correlation", size="correlation",
# palette="vlag", hue_norm=(-1, 1), edgecolor=".7",
# height=10, sizes=(50, 1550), size_norm=(-.8, .8),
# )

# # Tweak the figure to finalize
# g.set(xlabel="", ylabel="", aspect="equal")
# g.despine(left=True, bottom=True)
# g.ax.margins(.05)
# for label in g.ax.get_xticklabels():
#     label.set_rotation(25)
#     label.set_fontsize(16)
# for label in g.ax.get_yticklabels():
#     label.set_fontsize(16)
# for artist in g.legend.legendHandles:
#     artist.set_edgecolor(".7")

plt.savefig(f'HSI_Network_CorrMatrix.pdf')