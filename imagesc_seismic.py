import matplotlib.pyplot as plt
import seaborn
import numpy
def imagesc(data,cmap='seismic_r',figsize=(9.3,7),cbar=False):
    size = data.shape
    plt.figure(figsize=figsize)
    ax = seaborn.heatmap(data,cmap=cmap,cbar=cbar)
    ax.set_xlabel('Trace number',fontdict={'family' : 'Times New Roman', 'size': 12})
    ax.set_ylabel('Time sample number',fontdict={'family' : 'Times New Roman', 'size': 12})
    ax.set_xticks([i*20 for i in range(1,size[0]//20+1)])
    ax.set_xticklabels([str(i*20) for i in range(1,size[0]//20+1)],fontproperties = 'Times New Roman', size = 12)
    ax.set_yticks([i*20 for i in range(1,size[1]//20+1)])
    ax.set_yticklabels([str(i*20) for i in range(1,size[1]//20+1)],fontproperties = 'Times New Roman', size = 12)
    p = ax.get_figure()
    plt.show()
    return p