import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import gluonnlp as nlp
import numpy as np
from tqdm import tqdm, tqdm_notebook

from BERTDataset import BERTDataset
from model.BERTClassifier import BERTClassifier
from review_SA import review_SA

from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model

# parameter 
max_len = 128
batch_size = 32

# device 
device = torch.device('cpu')

#BERT 모델, Vocabulary 불러오기 
bertmodel, vocab = get_pytorch_kobert_model()

## 학습 모델 불러오기
PATH = './model/model_naver_11st.pt'
model = BERTClassifier(bert=bertmodel)
model.load_state_dict(torch.load(PATH, map_location=device))
model.eval()

# 토큰화 
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

while True:
    sentence = input("긍부정을 판단할 리뷰를 입력해주세요 : ")
    if sentence == "0":
      print(">> 긍부정 판단을 종료합니다!\n")
      break
    print(review_SA.predict(sentence))
    print("\n")
