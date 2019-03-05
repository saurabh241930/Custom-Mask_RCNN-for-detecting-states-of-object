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
pip install IPython[all] 
```

Now clone this repository

* To run predictions on pre-trained weights ,download weights here [!click to download weights](https://drive.google.com/open?id=1hKfu69Oac5JRh8FfGWLOkzCU-duw5pJn)

* place **`mask_rcnn_objects_0030-gen2(old2).h5`** inside `Mask_RCNN/logs/objects_old/` (make it if does not exist)

* run `inspect_objects_model.ipnyb` cells by cells and int the last you can append
```python
import PIL
import numpy as np
import skimage 




for x in range(1,"total images to predict"):
    print("image{x}".format(x=x))
    testImage = np.asarray(PIL.Image.open('/path/to/image{x}.jpg'.format(x=x)))
    predict = model.detect([testImage], verbose=1)
    ax = get_ax(1)
    prediction = predict[0]
    visualize.display_instances(testImage, prediction['rois'], prediction['masks'], prediction['class_ids'], 
                            dataset.class_names, prediction['scores'], ax=ax,
                            title="Predictions-image{x}".format(x=x))
  ```                          
