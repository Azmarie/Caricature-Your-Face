#!/bin/bash

# Common arguments
im_size='256'
content_name="barack_obama"
style_artist="Vincent_van_Gogh"
style_name="151"
content_path="data/content/${content_name}.jpg"
style_path="data/style/${style_artist}/${style_name}.png"
style_pts_path="data/style/pts/${style_name}.txt"

# 1. Detect Facial Landmarks with dlib
content_pts_path="data/content/pts/${content_name}.txt"
style_pts_path_dlib="data/style/pts/${style_name}_dlib.txt"

python face_landmark_detection.py ${content_path} ${style_path} ${content_pts_path} ${style_pts_path_dlib}

# 2. Run DST Style Transfer
output_dir="data/output/${style_artist}"
output_prefix="${content_name}-${style_name}"
max_iter='150'
checkpoint_iter='50'
content_weight='8' # alpha
warp_weight='0.5' # beta
reg_weight='50' # gamma
optim='sgd'
lr='0.3'
verbose='1'
save_intermediate='1'
save_extra='1'
device='cuda:0' # cpu or cuda

python -W ignore main.py ${content_path} ${style_path} ${content_pts_path} ${style_pts_path} \
  ${output_dir} ${output_prefix} ${im_size} ${max_iter} \
  ${checkpoint_iter} ${content_weight} ${warp_weight} ${reg_weight} ${optim} \
  ${lr} ${verbose} ${save_intermediate} ${save_extra} ${device}
