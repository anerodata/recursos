## AND *EVERYBODY* SHOULD RUN THIS CELL
from fastai.vision import *
from fastai.widgets import *
from IPython.display import Image as Show
from IPython.display import display
from io import BytesIO
import warnings
warnings.filterwarnings('ignore')
import fastai
print(f'fastai: {fastai.__version__}')
print(f'cuda: {torch.cuda.is_available()}')

Show('data/images/IMG_8027.JPG', width=600)

json_file = json.load(open('data/imagenet_class_index.json'))
classes = [json_file[str(k)][1] for k in range(len(json_file))]

#LOAD THE MODEL

# Get weights of the model and add nn.LogSoftmax(dim=1) to the end
model = models.resnet50(pretrained = True)
model = nn.Sequential(model, nn.LogSoftmax(dim=1))

# Transformation to apply to image before prediction (center crop)
# tfms = get_transforms() is possible too
tfms = [ [], [crop_pad()] ]

# Get an empty databunch with the ImageNet classes
# WARNING single_from_classes is deprecated (https://docs.fast.ai/vision.data.html#ImageDataBunch.single_from_classes)
data = ImageDataBunch.single_from_classes('data/', classes, ds_tfms=tfms, size=224).normalize(imagenet_stats)

# Get the learner of the model
learn = Learner(data, model)

#Load images
imageFiles = os.listdir('data/images')
print(imageFiles)

# Loop through the list of files and check the result
for file in imageFiles:
    img = open_image('data/images/' + file)
    pred_class, pred_idx, prediction_list = learn.predict(img)
    confidence = str(round(float(prediction_list[pred_idx]),2))
    # print the file name and the category guess
    print(file, pred_class, confidence)
    
""" 
boat2.jpg liner 0.72
chiquito.jpg bow_tie 0.99
finesse.jpg electric_guitar 0.43
IMG_1407.JPG umbrella 0.61
IMG_1454.JPG marmot 0.53
IMG_8027.JPG valley 0.88
IMG_8039.jpg stopwatch 0.86
IMG_8040.JPG beer_glass 0.54
IMG_8098.JPG barn 0.37
IMG_8592.JPG aircraft_carrier 0.5
la polla records 5.jpg packet 0.29
sprite.png toilet_tissue 0.62
zapatero.jpg suit 0.51
"""