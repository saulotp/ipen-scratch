import matplotlib.pyplot as plt
from skimage import io
from skimage.filters.rank import entropy
from skimage.morphology import disk
import numpy as np

import glob
test = []
for i in range (1,9):
    img = io.imread(f"C:\python\img_{i}.jpg", as_gray=True)
    entropy_img = entropy(img, disk(3))
    plt.imshow(entropy_img)
    plt.savefig(f'post_{i}.png')
    
    
    
    ## apply filter
    #from skimage.filters import threshold_otsu
    
    #tresh = threshold_otsu(entropy_img)
   # binary = entropy_img <= tresh
    #plt.imshow(binary)
    
    ## quantidade de pixels no espaço vazio do poço
  #  print(np.sum(binary == 1))
  #  px = (np.sum(binary == 1))
  #  test.append(px)

#plt.scatter(test)
    
