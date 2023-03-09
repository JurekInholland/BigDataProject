# Tensorflow + CUDA on Windows 11

This guide is bsaed on [this blogpost](https://thegeeksdiary.com/2021/10/07/how-to-setup-tensorflow-with-gpu-support-in-windows-11/) with slightly more recent versions of CUDA and CUDNN.

>Beware: tensorflow 2.11.0 and above [no longer supports gpus on native windows](https://github.com/tensorflow/tensorflow/blob/v2.11.0-rc1/RELEASE.md#major-features-and-improvements). (WSL2 can be used instead).  

## 1 Install latest nvidia driver
https://www.nvidia.com/Download/index.aspx

## 2 Install miniconda
https://conda.io/en/latest/user-guide/install/windows.html

## 3 Install CUDA Toolkit 11.8.0
https://developer.nvidia.com/cuda-toolkit-archive

## 4 Install CUDNN 8.7 for CUDA 11.x
https://developer.nvidia.com/rdp/cudnn-archive
Extract to `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin\`


## 5 Create conda env
1. Open conda prompt and paste:
```python
# create a new environment with name 'tensorflow-gpu' and python version 3.8
conda create --name tensorflow-gpu python=3.8
# activate the environment
conda activate tensorflow-gpu
# install tensorflow 2.8
pip install tensorflow==2.8
# enable notebook support in our environment
conda install -y -c conda-forge nb_conda
# add the environment to Jupyter Kernel
python -m ipykernel install --user --name tensorflow-gpu --display-name "Python 3.8 (tensorflow-gpu)"
# deactivate the environment
conda deactivate
 
# create a new directory for our test notebook to check the tensorflow GPU initialization
mkdir test-installation
# go inside the new directory
cd test-installation
# activate our test environment
conda activate tensorflow-gpu
# start jupyter notebook
jupyter notebook
```

## Verify tensorflow is detecting GPU
```python
import sys
 
import tensorflow.keras
import tensorflow as tf
print(f"Tensor Flow Version: {tf.__version__}")
print(f"Keras Version: {tensorflow.keras.__version__}")
print()
print(f"Python {sys.version}")
gpu = len(tf.config.list_physical_devices('GPU'))>0
print("GPU is", "available" if gpu else "NOT AVAILABLE")
```