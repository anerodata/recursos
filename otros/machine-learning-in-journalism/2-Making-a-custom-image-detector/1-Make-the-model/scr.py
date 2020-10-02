## AND *EVERYBODY* SHOULD RUN THIS CELL
import warnings
warnings.filterwarnings('ignore')
from fastai.vision import *
from fastai.metrics import error_rate
import fastai
#print(f'fastai: {fastai.__version__}')
#print(f'cuda: {torch.cuda.is_available()}')
#Esta linea le dice a fast.ai que use la cpu, en lugar de la gpu para el proceso. Si queremos crear el modelo, necesita cpu
defaults.device = torch.device('cpu')  # for the gpu it would be 'cuda'
from os import listdir

data_path = '../data/img/helicopters/choppers'
pkl_path = '../data/pkl'

my_transforms = None  # note: We'll talk more about transforms later
data = (ImageList.from_folder(data_path) # Where to find the data? -> in path and its subfolders
        .split_by_rand_pct()        # How to split in train/valid? -> do it *randomly* (Not by folder)
        .label_from_folder()        # How to label? -> get from the folder name
        .transform(my_transforms, size=600)  # Data augmentation? -> use tfms with a size of 600, because they all are
        .databunch(bs=16))          # Size of simultaneous batches -> 16 (higher is faster & uses more memory)

learn = cnn_learner(data, models.resnet34, metrics=error_rate)
#permitir multi proceso
if __name__ == '__main__':
    learn.fit_one_cycle(1)
    learn.export("helicopters_model.pkl")