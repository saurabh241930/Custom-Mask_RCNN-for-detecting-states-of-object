import PIL
import numpy as np
import skimage 




for x in range(1,291):
    print("image{x}".format(x=x))
    testImage = np.asarray(PIL.Image.open('/tf/Mask_RCNN/samples/objects/frames_reception_1/image{x}.jpg'.format(x=x)))
    predict = model.detect([testImage], verbose=1)
    ax = get_ax(1)
    prediction = predict[0]
    visualize.display_instances(testImage, prediction['rois'], prediction['masks'], prediction['class_ids'], 
                            dataset.class_names, prediction['scores'], ax=ax,
                            title="Predictions-image{x}".format(x=x))
    

    
    

# for x in range(10):
#     print("test{x}.jpg".format(x=x))
