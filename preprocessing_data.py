import os

import numpy as np
import pandas as pd
from tqdm import trange

df = pd.read_csv(os.path.join('../../FolkScope', 'TOTAL_typicality_result.csv'))
img_features = np.load('vision_features/amazon_img_detr.npy')
source_text = []
target_text = []
img_id_as = []
img_id_bs = []
for i in trange(len(df)):
    item_a_id = df['item_a_id'][i]
    item_b_id = df['item_b_id'][i]
    for j in range(1, 4):
        img_id_a = f'{item_a_id}_{j}'
        for k in range(1, 4):
            img_id_b = f'{item_b_id}_{k}'
            if img_id_a in img_features and img_id_b in img_features:
                source_text.append(f"Question: Why PeopleX buy these two items at the same time?; category:{df['cate'][i]}; item A name:{df['item_a_name'][i]}, item B name: {df['item_b_name'][i]}.")
                target_text.append(df['assertion'][i])
                img_id_as.append(img_id_a)
                img_id_bs.append(img_id_b)

train_df = pd.DataFrame()

train_df['targets'] = target_text
train_df['sources'] = source_text
train_df['img_id_a'] = img_id_as
train_df['img_id_b'] = img_id_bs

pd.save_csv('amazon_train_samples_img.csv',train_df)