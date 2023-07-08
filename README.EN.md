# Tumor Detection-Segmentation App


we wrote 2 deep learning model for classification and segmetation of tumor and i also  create exe GUI application for who wants to use this project but donot have computer knowledge like doctors and medical reaserchers ...
i hope it will useful for you
 
## use GUI Aplication

for using the exe appilcation you can easily download the latest release in github after downloading extract it and run the app_interface_5 and wait for a second and easily use it
GUI Aplication does not need download any dependencies all of them is already exist in github release



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/ce286372-576a-40b6-9061-cb6c10d0dc46)



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/add25503-031d-415a-983a-9f6bd90affc0)




### install dependencies


we use 3.11 to wrote this code but pay attention to using 3.7 or latest version of python to run thease code 
you can easily download source code from my github page or if you are familiar with github you can clone the source code in your envirement(better use virtual envierment in these case) 

first tip  : for next step we have to install python library dependencies you can use Requierments.txt file and then open your terminal and change directory to your virtual envierments and use this command for installing all library with one line code : pip install -r Requirements.txt


second tip : also you can download bellow dependencies manually with pip install 

- tensorflow
- scikit-learn
- numpy
- opencv-python
- matplotlib
- pillow
- pandas
- keras

- 
### important file


we have 3 important python file(notebook)
classification-tumor-finall: in this file i implement a model that able us to know what MRI has tumor and what MRI has not any tumor in fact this model classification all brain MRI to 2 class : has tumot , has not tumor
this model do this job with more than 97% so it is reliable model
finall-version-tumor-segmentation : in this file i implement a model that able us to know location of the tumor in image this model has more than 98% accuracy in identifying the correct location and it has more than 78% accuracy in identifying the entire tumor area and it means i creat reliable model to know where tumor it is 
mask maker : in this file i wrote some code to make my input data readable for my model i created
i download   some dataset from kaggle and i  use them for training my model and i use annotation_data_1 and image_dataset directory for train tumor segmentation and i ues no , yes directory for training tumor classification.


### some explanation


i ues  depp learning alghorithm call convolutional neural network(CNN) and dense neural network for train my data 
and  i use U-Net alghorithm for tumor segmentation beacuse U-Net is so accurate even with little dataset(like this case) and beacuse thease reason it is use a lot in medical AI model 

### Classification Model  Architecture 


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/598e882c-b5dd-4292-b583-48bbfbf34421)



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/0537f05b-0f0f-4468-a655-45dc7e87ada2)



### Segmentation Model Architecture


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/85522af7-1e2e-4a53-89df-e763b336a85d)



### statistics model  evaluate 


evaluate on classification test dataset :


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/19702c3e-750d-460f-8575-a18b6d987b20)


statistics during training classification model : 


![plot_acc_class](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/65a14a8d-9ee9-4aef-8b99-9da458b645b4)




![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/fe437163-8fc9-42df-84dc-d6b57b1b177c)


evaluate on segmentation test dataset :

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/fa3816af-7b9d-4e6b-aacf-cc080f843b64)



statistics during training segmentation model  :




![plot_acc_seg](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/9b3bbf55-d45c-45e1-95a4-2794e7f8e0c1)




![plot_loss_seg](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/b95b41cf-bb32-4c55-848b-71950917f3c2)




### for read more about this project follow bellow link : 


https://docs.google.com/document/d/1Ks_FQasrY04Yzl6VKujV9JxzLBfAXbLxyykMz2dH51I/edit
  
