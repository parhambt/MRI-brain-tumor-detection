from tensorflow.keras.layers import Conv2D, Input, ZeroPadding2D, BatchNormalization, Activation, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.utils import shuffle
from math import ceil
import pandas as pd 
import cv2 as cv
import os
import numpy as np
from numpy import zeros
import tensorflow as tf
import matplotlib.pyplot as plt
import sklearn as sk
import keras 
from PIL import Image, ImageEnhance
import random
from tensorflow.keras import datasets, layers, models
import pickle
#Function
def load_data(dir_list, image_size):
    """
    Read images, resize and normalize them. 
    Arguments:
        dir_list: list of strings representing file directories.
    Returns:
        X: A numpy array with shape = (#_examples, image_width, image_height, #_channels)
        y: A numpy array with shape = (#_examples, 1)
    """

    # load all images in a directory
    data_ = []
    label = []
    image_width, image_height = image_size
    
    for directory in dir_list:
        for filename in os.listdir(directory):

            image = cv.imread(directory + '\\' + filename,0)

            image = cv.resize(image, dsize=(image_width, image_height), interpolation=cv.INTER_CUBIC)

            image = image / 255.

            data_.append(image)

            if directory == 'yes':
                label.append([1]) ## have tumor
            else:
                label.append([0]) ## donot have tumor 

    data_array = np.array(data_)
    label = np.array(label)
    
    # Shuffle the data
#     data_array, label = shuffle(data_array, label)
    
    print(f'Number of examples is: {len(data_array)}')
    print(f'X shape is: {data_array.shape}')
    print(f'y shape is: {label.shape}')
    
    return data_array, label
#------------------------------------------------
def replace_argmax(array,to_array=True):
    lst=[]
    for item in array :
        arg_max=np.argmax(item)
        lst.append([arg_max])
    if to_array==True :
        lst=np.array(lst)
    return lst
#---------------------------------------
def predict_on_custome_image(img_path,img_or_directory=False,plot=False):
    dict_1={}
    if img_or_directory==False :
        array=cv.imread(img_path,0)
        
        shape_array=array.shape
        array_1=cv.resize(array,(100,100))
        y,x=array_1.shape

        array=array_1.reshape(1,y,x)
        #-------
#         print(array.shape)
        y_predict=Model.predict(array)
        y_predict_res=replace_argmax(y_predict)


        if y_predict_res==np.array([0]) :
            predicted='do not have tumor'
            
        else : 
            predicted='have tumor'
        
        dict_1.update({img_path:predicted})
        if plot==True :
            plt.imshow(array_1,cmap='gray')
            plt.title(predicted)
            plt.axis('off')
    else :
        all_img=os.listdir(img_path)
        image_count=len(all_img)
        
        if plot==True :
            rows,columns=3,ceil(image_count/3)
            fig = plt.figure(figsize=(10, 7))
            
        for c,path in enumerate(all_img) :
            array=cv.imread(img_path+'/'+path,0)
        
            shape_array=array.shape
            array_1=cv.resize(array,(100,100))
            y,x=array_1.shape

            array=array_1.reshape(1,y,x)
        #-------
            
            y_predict=Model.predict(array)
            y_predict_res=replace_argmax(y_predict)
            if y_predict_res==np.array([0]) :
                predicted='do not have tumor'
            
            else : 
                predicted='have tumor'
            dict_1.update({path:predicted})
            if plot==True :
                fig.add_subplot(rows, columns, c+1)
                plt.imshow(array_1,cmap='gray')
                plt.title(predicted)
                plt.axis('off')
    return dict_1           




#------------------------------------

with open("tumor_trained_model_by_parham",'rb') as f : 
    Model=pickle.load(f)


# g_1=predict_on_custome_image('C:\\Users\\GIGA\\Downloads\\no9.jpg')
# print(g_1)
