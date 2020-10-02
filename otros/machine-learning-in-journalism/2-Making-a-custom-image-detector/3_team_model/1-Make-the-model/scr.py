
## AND *EVERYBODY* SHOULD RUN THIS CELL
import warnings
warnings.filterwarnings('ignore')
from fastai.vision import *
from fastai.metrics import error_rate
import fastai
print(f'fastai: {fastai.__version__}')
print(f'cuda: {torch.cuda.is_available()}')

"""Bajar el zip de Github con las imágenes de los futbolistas, descomprimirlo y marcar la ruta"""

# Commented out IPython magic to ensure Python compatibility.
# Run this cell to download the data we'll use for this exercise
!wget -N https://github.com/anerodata/curso-machine-learning/raw/master/2-Making-a-custom-image-detector/3_team_model/data/img.zip --quiet
!unzip -q img.zip
print('Done!')
# %ls 'img/'
data_path = 'path-to-img'
my_transforms = None  # note: We'll talk more about transforms later
data = (ImageList.from_folder(data_path) # Where to find the data? -> in path and its subfolders
        .split_by_rand_pct()        # How to split in train/valid? -> do it *randomly* (Not by folder)
        .label_from_folder()        # How to label? -> get from the folder name
        .transform(my_transforms, size=600)  # Data augmentation? -> use tfms with a size of 600, because they all are
        .databunch(bs=16))          # Size of simultaneous batches -> 16 (higher is faster & uses more memory)

data.show_batch(rows=3)

print(data.classes)

learn = cnn_learner(data, models.resnet34, metrics=error_rate)
learn.fit_one_cycle(8)

!wget -N 'https://raw.githubusercontent.com/anerodata/curso-machine-learning/master/2-Making-a-custom-image-detector/3_team_model/data/img_test/sanchis-test.jpg' --quiet
img = open_image('sanchis-test.jpg')
pred_class, pred_idx, outputs = learn.predict(img)
print(pred_class)

