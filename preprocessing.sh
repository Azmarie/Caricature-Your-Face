#!/bin/bash

style_path='data/style/*/*.ljson'
style_pts_path_foa='data/style/pts/'

# Only need to run once (if you don't have data/style/pts folder)
# Convert all Face of Art style images' correspondence points into .txt

python utils/utils_convert_foa_points.py ${style_path} ${style_pts_path_foa}