import numpy as np
import os
from PIL import Image
import pickle as p


def image_to_array(file_path):
    result = np.array([])
    image = Image.open(file_path).resize((180, 180))
    r, g, b = image.split()
    r_arr = np.array(r).reshape(-1)
    g_arr = np.array(g).reshape(-1)
    b_arr = np.array(b).reshape(-1)

    result = np.concatenate((r_arr, g_arr, b_arr))
    file_name = os.path.basename(file_path).split('.')[0] # get file name
    with open(file_name + '.bin', 'wb') as f:
        p.dump(result, f)
    print('ok')

if __name__ == '__main__':
    image_to_array('end.jpg')
