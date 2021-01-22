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
![Image text](https://github.com/chen-yao111/imagesc-for-2D-seismic-data/blob/main/image/original_data.png)
(128, 128)


## Enviroment Requirement
numpy

matplotlib

seaborn
