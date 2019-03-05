# oyo_coco

Working with multiple classes:

## Seting up enviroment

```
pip install numpy \
pip installscipy  \
pip install Pillow \
pip install cython \
pip install matplotlib \
pip install scikit-image \
pip install tensorflow>=1.3.0 \
pip install keras>=2.0.8 \
pip install opencv-python \
pip install h5py \
pip install imgaug \
pip install IPython[all] \
```

Make following directory structure:

Inside Mask_RCNN folder:

    ├── samples/

        ├── objects/
    
            ├── dataset/
        
                ├── train/[training images along with its JSONS]
             
                ├── val/[validation images along with its JSONS]
             
                ├── objects.py
             
                ├── inspect_data.ipynb
             
                ├── inspect_model.ipynb
             
    ├── mrcnn/
