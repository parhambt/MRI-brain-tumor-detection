from tensorflow.keras.models import load_model ,Model
from math import ceil
import cv2 as cv
import os
import matplotlib.pyplot as plt
from tensorflow.keras import backend as K
import numpy as np 

def Dice_Coefficient(y_true, y_pred, smooth=1):
    intersection = K.sum(y_true * y_pred, axis=[1,2,3])
    union = K.sum(y_true, axis=[1,2,3]) + K.sum(y_pred, axis=[1,2,3])
    dice = K.mean((2.0 * intersection + smooth)/(union + smooth), axis=0)
    return dice

def Dice_Loss(y_true, y_pred):
    return 1.0 - Dice_Coefficient(y_true, y_pred)


Unet_Model = load_model('segmetation_parham.h5', custom_objects={'Dice_Loss':                   
Dice_Loss,'Dice_Coefficient':Dice_Coefficient})

Model = load_model('tumor_classification_trained_model_by_parham_2.h5')

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
        array=array_1.reshape(1,y,x,1)
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

                array=array_1.reshape(1,y,x,1)
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
# a=predict_on_custome_image('plot_testing',img_or_directory=True,plot=True)
# print(a)






def threshold(array):
    array=array.flatten()
    flat_array=list(map(lambda x :255 if x>0.5 else 0,array))
    flat_array=np.array(flat_array)
    th=flat_array.reshape(256,256)
    return th 
def combine_pred_original(path,dir_path=False,plot=False):
    if dir_path==False : 
        image=cv.imread(path)
        image=cv.resize(image,(256,256))

        image_gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

        image_1=image_gray / 255.0
        image_1= image_1.astype(np.float32)
        # plt.imshow(image,cmap='gray')

        image_1=image_1.reshape(-1,256,256,1)
        y_hat = Unet_Model.predict(image_1)

        y_hat=y_hat.reshape(256,256)
        mask=threshold(y_hat)
        finall_img=np.copy(image)
        index_mask=np.where(mask==255)
        finall_img[index_mask]=[0,0,255]
        finall_img=cv.resize(finall_img,(512,512))
        if plot==True : 
            plt.imshow(finall_img[:,:,::-1])
        return finall_img
    #     plt.imshow(image_gray,cmap='gray')
        
    else  :
        all_result={}
        all_img_name=os.listdir(path)
        image_count=len(all_img_name)
        if plot==True :
            rows,columns=3,ceil(image_count/3)
            fig = plt.figure(figsize=(10, 7))
        for c,name in enumerate(all_img_name) : 
            image=cv.imread(path+'/'+name)
            image=cv.resize(image,(256,256))

            image_gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

            image_1=image_gray / 255.0
            image_1= image_1.astype(np.float32)
        # plt.imshow(image,cmap='gray')

            image_1=image_1.reshape(-1,256,256,1)
            y_hat = Unet_Model.predict(image_1)

            y_hat=y_hat.reshape(256,256)
            mask=threshold(y_hat)
            finall_img=np.copy(image)
            index_mask=np.where(mask==255)
            finall_img[index_mask]=[255,0,0]
            finall_img=cv.resize(finall_img,(512,512))
            all_result.update({name:finall_img})
            if plot==True :
                fig.add_subplot(rows, columns, c+1)
                plt.imshow(finall_img[:,:,::-1])
    
                plt.axis('off')
            
        return all_result
    
    

# a=combine_pred_original(path='segmentation_testing',dir_path=True,plot=True)


