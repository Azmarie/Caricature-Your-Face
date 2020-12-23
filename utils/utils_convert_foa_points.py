import os
import sys
import json
import glob

style_path = sys.argv[1:-1]
style_pts_path_foa = str(sys.argv[-1])

if not os.path.exists(style_pts_path_foa):
    os.makedirs(style_pts_path_foa)

for filename in style_path:
    print(filename)

    with open(filename) as f:
        data = json.load(f)
        points = data["landmarks"]["points"]
        pts_file_name = filename.split("/")[-1].partition('.')[0]+'.txt'

        with open(os.path.join(style_pts_path_foa, pts_file_name), 'w+') as opt_file:
            for j in range(len(points)):
                opt_file.write('%i, %i\n' % (points[j][0], points[j][1]))
