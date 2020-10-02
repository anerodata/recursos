## AND *EVERYBODY* SHOULD RUN THIS CELL
import warnings
import torch
#print(torch.randn(2,2).cuda())
warnings.filterwarnings('ignore')
from fastai.vision import *
from fastai.metrics import error_rate
from os import listdir
import fastai
#defaults.device = torch.device('cuda')  # for the gpu it would be 'cuda'
print(f'fastai: {fastai.__version__}')
print(f'cuda: {torch.cuda.is_available()}')
save_path = Path('../data/pkl/')
print (save_path)   
learn = load_learner(save_path)
print (listdir('../data/img/helicopters/'))
img = open_image('../data/img/helicopters/not_yet_seen.png')
pred_class,pred_idx,outputs = learn.predict(img)  
print (pred_class)    
