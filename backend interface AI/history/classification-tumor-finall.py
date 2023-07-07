#!/usr/bin/env python
# coding: utf-8

# In[30]:


from tensorflow.keras.layers import Conv2D, Input, ZeroPadding2D, BatchNormalization, Activation, MaxPool2D, Flatten, Dense,Dropout
from tensorflow.keras.models import Model, load_model, save_model

from tensorflow.keras.callbacks import EarlyStopping ,CSVLogger
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.utils import shuffle
from math import ceil
import pandas as pd 
import cv2 as cv
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import sklearn as sk
import keras 
from tensorflow.keras import datasets, layers, models
get_ipython().run_line_magic('matplotlib', 'inline')


# # Functions

# In[17]:


def load_data(dir_list, image_size):


    # load all images in a directory
    data = []
    label = []
    image_width, image_height = image_size
    
    for directory in dir_list:
        for filename in os.listdir(directory):
            
            image = cv.imread(directory + '/' + filename,0)

            image = cv.resize(image, dsize=(image_width, image_height), interpolation=cv.INTER_CUBIC)

            image = image / 255.0
            image= image.astype(np.float32)

            data.append(image)

            if directory == 'yes':
                label.append([1]) ## have tumor
                
            else:
                label.append([0]) ## donot have tumor 
            

    data_array = np.array(data)
    label = np.array(label) 
    return data_array, label


        


# # loading data 
# now time to loading data with pre procssing like resizing ...
# 

# In[14]:


x,y=load_data(['yes','no'],(256,256))
# print(x[2])
print(y[2])
plt.imshow(x[2], cmap='gray')
plt.axis('off')
plt.title('sample_image')


# # splitting data
# for training data we have to split our data 
# - train dataset 0.8
# - validate dataset 0.2 (optional)
# - test dataset 0.2 <br />
# validation dataset in this case are equal

# In[4]:


def split_data(test_size=0.2 , log=True):
    x_train, x_test_val, y_train, y_test_val = train_test_split(x, y, test_size=test_size,shuffle=True)
    if log==True : 
        print('Input Shape : ')
        print(x_train.shape,(y_train).shape)
        print(x_test_val.shape,(y_test_val).shape)
    x_test=x_test_val
    x_val=x_test_val
    y_test=y_test_val
    y_val=y_test_val
    
        
    x_train=x_train.reshape(-1,256,256,1)  
#     y_train=y_train.reshape(-1,100,100,1)  
#     y_test=y_test.reshape(-1,100,100,1)    
    x_test=x_test.reshape(-1,256,256,1)
    x_val=x_val.reshape(-1,256,256,1)
    if log==True : 
        print('Output Shape : ')
        print(x_train.shape,y_train.shape)
        print(x_test.shape,y_test.shape)
        print(x_val.shape,y_val.shape)
    return x_train, x_test, y_train, y_test,x_val,y_val
x_train, x_test, y_train, y_test,x_val,y_val=split_data()
validation_dataset=(x_val,y_val)


# # Build Model
# 
# 

# In[5]:


def Build_Model(input_shape=(256,256,1)):
    Model = keras.models.Sequential([
            Conv2D(16,kernel_size=(3,3),activation='relu',input_shape=input_shape),
            Conv2D(32,kernel_size=(3,3),activation='relu'),
            MaxPool2D(2,2),
            Conv2D(32,kernel_size=(3,3),activation='relu'),    
            Conv2D(32,kernel_size=(3,3),activation='relu'),    
            Conv2D(64,kernel_size=(3,3),activation='relu'),
            MaxPool2D(4,4),
            Flatten() ,    
            Dense(64,activation='relu') ,        
            Dense(32,activation='relu') ,   
            Dense(16,activation='relu'),
            Dropout(rate=0.5) ,            
            Dense(1,activation='sigmoid') ,    
            ])
    return Model


# In[6]:


Model=Build_Model()
Model.summary()


# In[7]:


Model.compile(optimizer='adam',
              loss="binary_crossentropy",
              metrics=['accuracy'])


# In[8]:


def make_callbacks(csv_path='/kaggle/working/my_class_log_5.csv'):
    early_stop=EarlyStopping(monitor='val_loss',patience=8,mode='min',restore_best_weights=False)
    csv_logger=CSVLogger(csv_path)
    callbacks =[early_stop,csv_logger]
    return callbacks
callbacks=make_callbacks()


# In[9]:


epochs = 32
Model.fit(x_train, y_train, epochs=epochs,batch_size=32,verbose=1,callbacks=callbacks,validation_data=validation_dataset)


# # saving trained model

# In[10]:


# Model.save('tumor_classification_trained_model_by_parham_2.h5')


# # load training model

# In[31]:


Model = load_model('tumor_classification_trained_model_by_parham_2.h5')


# # evaluating

# In[16]:


Model_loss, Model_accuracy = Model.evaluate(x_test, y_test)

print(f"it is Model accuracy: {Model_accuracy}")
print(f'it is Model loss: {Model_loss}')


# # Visualizing output

# In[34]:


def predict_human_readable(array):
    array=array.flatten()
    result=1 if array>0.5 else 0
    return result   
#----------------------------------------
def predict_on_custome_image(img_path,img_or_directory=False,plot=False):
    dict_1={}
    if img_or_directory==False :
        array=cv.imread(img_path,0)
        
        shape_array=array.shape
        array_1=cv.resize(array,(256,256))
        
        y,x=array_1.shape
#         array_1=array_1 / 255.0
        array=array_1.reshape(1,y,x)
        #-------
#         print(array.shape)
        y_predict=Model.predict(array)
        y_predict_res=predict_human_readable(y_predict)
        

        if y_predict_res== 1:
            predicted='Tumor Detected'
            
        else : 
            predicted='do not have tumor'
        
        dict_1.update({img_path:predicted})
        if plot==True :
            plt.imshow(array_1,cmap='gray')
            plt.title(predicted)
            plt.axis('off')
    else :
        all_img=os.listdir(img_path)
        image_count=len(all_img)
#         print(all_img)
        if plot==True :
            rows,columns=3,ceil(image_count/3)
            fig = plt.figure(figsize=(20, 14))
            
        for c,path in enumerate(all_img) :
            lst_1=path.split('.')
            if lst_1[1]=='jpg' or lst_1[1]=='png' or lst_1[1]=='jpeg': 
                array=cv.imread(img_path+'/'+path,0)
    #             print(img_path+'/'+path)
                shape_array=array.shape
                array_1=cv.resize(array,(256,256))
                y,x=array_1.shape

                array=array_1.reshape(1,y,x)
            #-------

                y_predict=Model.predict(array)
                y_predict_res=predict_human_readable(y_predict)
                if y_predict_res==1 :
                    predicted='Tumor Detected'

                else : 
                    predicted='do not have tumor'
                dict_1.update({path:predicted})
                if plot==True :
                    fig.add_subplot(rows, columns, c+1)
                    plt.imshow(array_1,cmap='gray')
                    plt.title(predicted)
                    plt.axis('off')
            else :
                continue
    return dict_1           
a=predict_on_custome_image('plot_testing',img_or_directory=True,plot=True)
print(a)


# # plot accuracy

# In[16]:


csv=pd.read_csv('my_class_log_5.csv')
accuracy=csv['accuracy']
loss=csv['loss']
val_accuracy=csv['val_accuracy']
val_loss=csv['val_loss']
print(csv[['loss','val_loss']])


# In[29]:


plt.plot(accuracy,label='Training Accuracy')
plt.plot(val_accuracy,label='Validation Accuracy')
plt.legend()
plt.title('Classification Model Accuracy')
plt.show()


# In[28]:


y_tic=np.arange(0,0.7,0.05)
plt.plot(loss,label='Training Loss',)
plt.plot(val_loss,label='Validation Loss')
plt.yticks(y_tic)
plt.legend()
plt.title('Classification Model Loss')
plt.show()


# In[ ]:




