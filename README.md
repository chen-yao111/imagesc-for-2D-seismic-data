# Imagesc for 2D Seismic Data
## File Introduction
imagesc_seismic: This is a python file that includes the function imagesc to depict the 
seismic data in Python. 

demo: This is an example to declare how to apply imagesc.

## Parameters Introduction
data: 2D NumPy array, seismic data.

cmap: default value: ‘seismic_r’, feasible values can be found in Matplotlib introduction.

figsize: default value: (9.3,7), the figure size will be 60*figsize.

cbar: on-off for the color bar.

return: a figure.

## Instance
```
print(data.shape)
imagesc(data)
```
(128, 128)
![20bdfb3fc4ecd008e9ff9f50e03408d1.png](en-resource://database/497:0)

## Enviroment Requirement
numpy
matplotlib
seaborn
