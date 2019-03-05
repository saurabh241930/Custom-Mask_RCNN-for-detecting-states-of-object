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

## To make predicions on pre-trained weights
Clone this repository

* To run predictions on pre-trained weights ,download weights here [click to download weights](https://drive.google.com/open?id=1hKfu69Oac5JRh8FfGWLOkzCU-duw5pJn)

* place **`mask_rcnn_objects_0030-gen2(old2).h5`** inside `Mask_RCNN/logs/objects_old/` (make it if does not exist)

* run `inspect_objects_model.ipnyb` cell by cell and in the last you can append
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

## Test results
 Predictions                                              |  Input Images
:--------------------------------------------------------:|:-------------------------:
<img src="https://i.imgur.com/vD1wSBc.png" width="800" /> | <img src="https://i.imgur.com/4FaCF4o.jpg" width="400" />
<img src="https://i.imgur.com/uIAHaRp.png"  width="800" />| <img src="https://i.imgur.com/PFYRd53.jpg"  width="400" />
 

## To train on your own classes

* divide amount images into 90 : 10 > train : val
* annoate image based on their classes ,you can use this tool [tool link](http://www.robots.ox.ac.uk/~vgg/software/via/via.htm)
* make sure you returned each jsons will look like this 

```jsons

"imagename.jpg35881": {
        "filename": "imagename.jpg",
        "size": 35881,
        "regions": [
            {
                "shape_attributes": {
                    "name": "polygon",
                    "all_points_x": [
                        232,
                        319,
                        330,
                        345,
               
                    ],
                    "all_points_y": [
                        344,
                        345,
                        349,
                        341,
    
                    ]
                },
                "region_attributes": {
                    "name": "That object classsname"
                }
            }
        ],
        "file_attributes": {}
    },
```


### Edit the following lines in objects.py:

```python


68 > IMAGES_PER_GPU = 2    # if you have less than 11gb graphic card other wise set it to 1
71 > NUM_CLASSES = 1 + n  # where n is no of your classes 
77 > DETECTION_MIN_CONFIDENCE = 0.9 # adjust confidence in your training 0.9 => 90% 
90 > self.add_class("balloon", 1, "object0")    > :
>    self.add_class("objects", 2, "object1")
.    self.add_class("objects", 3, "object2")
.     
.    self.add_class("objects", n, "object nth")

202 > for i, p in enumerate(class_names):
            # Get indexes of pixels inside the polygon and set them to 1
            if p['name'] == 'object0':
                class_ids[i] = 1
            elif p['name'] == 'object1':
                class_ids[i] = 2
            elif p['name'] == 'object2':
                class_ids[i] = 3
            elif p['name'] == 'object3':
                class_ids[i] = 4
                .
                .
            elif p['name'] == 'object n':
                class_ids[i] = n
                
318 >  class_names = ['BG', 'object0', 'object1', ' object2', 'object3',, , ,'object n']


```

### Start training

change path to cd `Mask_RCNN/samples/objects` and run

**`python3 objects.py train --dataset=/path/to/openbook/dataset --weights=coco`**

after training your latest weights should be saved in logs/objects(hash no) to  run prediction using follow the prediction process give above just  change the weight directory




