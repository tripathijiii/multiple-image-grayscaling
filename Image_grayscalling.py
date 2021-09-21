import os
import time
import cv2
from google.colab.patches import cv2_imshow
import argparse
import matplotlib.pyplot as plt
start=time.process_time()
parser = argparse.ArgumentParser()
parser.add_argument('folder1')
parser.add_argument('folder2')
args=parser.parse_args()

path1='/content/'+args.folder1
path2= '/content/'+args.folder2
os.mkdir(path2)
os.chdir(path1)

def convert(file_path,count,path2):
    image=cv2.imread(file_path,0)
    filename='newfile{}.jpeg'.format(count)
    cv2.imwrite(os.path.join(path2,filename),image)


count=0
X=[]
Y=[]
for file in os.listdir():
    file_path=f'{path1}/{file}'
    convert(file_path,count,path2)
    count+=1
    if count%1000==0:
        X.append(count)
        Y.append(time.process_time()-start)

plt.plot(X,Y,color='blue')
plt.title('Time taken plot')
plt.xlabel('NO. of files')
plt.ylabel('Time in seconds')
plt.show()
plt.savefig('/content/plot_of_time.jpg')


