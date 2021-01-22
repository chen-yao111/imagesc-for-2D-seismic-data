import os
from imagesc_seismic import imagesc
import scipy.io
path = 'C:/Users/86173/Desktop/seismic_data/2D'
os.chdir(path)
database = scipy.io.loadmat('database.mat')
database = database['database']
data = database[0,8]
print(data.shape)
p = imagesc(data)
p.savefig(path+'/original_data.png',dpi=600)
