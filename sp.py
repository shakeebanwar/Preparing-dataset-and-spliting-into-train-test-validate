import os
import numpy as np
import shutil
import random

## Root dir means your dataset path
root_dir = "/home/shakeeb/Desktop/dataset/ECG Images dataset of Cardiac and COVID-19 Patients/data/orignal/Dataset/" # for requesting directly pics

##input_destination means the path would you like to copy train,test,validate data after spliting

input_destination =  "/home/shakeeb/Desktop/dataset/ECG Images dataset of Cardiac and COVID-19 Patients/data/orignal/Data/"
classes_dir = os.listdir(root_dir)

train_ratio = 0.6
val_ratio  = 0.1

for cls in classes_dir:
    os.makedirs(input_destination +'train_ds/' + cls, exist_ok=True)
    os.makedirs(input_destination +'test_ds/' + cls, exist_ok=True)
    os.makedirs(input_destination +'val_ds/' + cls, exist_ok=True)
    
    # for each class, let's counts its elements
    src = root_dir + cls
    allFileNames = os.listdir(src)

    # shuffle it and split into train/test/va
    np.random.shuffle(allFileNames)
    train_FileNames, test_FileNames, val_FileNames = np.split(np.array(allFileNames),[int(train_ratio * len(allFileNames)), int((1-val_ratio) * len(allFileNames))])
    
    # save their initial path
    train_FileNames = [src+'/'+ name  for name in train_FileNames.tolist()]
    test_FileNames  = [src+'/' + name for name in test_FileNames.tolist()]
    val_FileNames   = [src+'/' + name for name in val_FileNames.tolist()]
    print("\n *****************************",
          "\n Total images: ",cls, len(allFileNames),
          '\n Training: ', len(train_FileNames),
          '\n Testing: ', len(test_FileNames),
          '\n Validation: ', len(val_FileNames),
          '\n *****************************')
    
    # copy files from the initial path to the final folders
    for name in train_FileNames:
      shutil.copy(name, input_destination +'train_ds/' + cls)
    for name in test_FileNames:
      shutil.copy(name, input_destination +'test_ds/' + cls)
    for name in val_FileNames:
      shutil.copy(name, input_destination +'val_ds/' + cls)


# checking everything was fine
paths = ['train_ds/', 'test_ds/','val_ds/']
for p in paths:
  for dir,subdir,files in os.walk(input_destination + p):
    print(dir,' ', p, str(len(files)))