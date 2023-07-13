# Tumor Detection-Segmentation Project


i wrote 2 deep learning model for classification and segmetation of tumor and i also  create exe GUI application for who wants to use this project but donot have computer knowledge like doctors and medical reaserchers ...
i hope it will useful for you
 
## usage GUI Aplication

for using the exe appilcation you can easily download the latest release in github  and run the app_GUI_interface.exe and wait for a second and easily use it
GUI Aplication does not need download any dependencies all of them is already exist in github release


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/1c97b792-96a1-4f7c-a5da-2e18e0f6dd16)



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/1bce1b16-7992-4ad0-a947-8f803531a85c)





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


### important file


we have 3 important python file(notebook)


classification-tumor-finall: in this file i implement a model that able us to know what MRI has tumor and what MRI has not any tumor in fact this model classification all brain MRI to 2 class ( has tumot , has not tumor) also this model do this job with more than 97% accuracy  so it is reliable model


finall-version-tumor-segmentation : in this file i implement a model that able us to know location of the tumor in image this model has more than 98% accuracy in identifying the correct location and it has more than 78% accuracy in identifying the entire tumor area and it means i creat reliable model to know where tumor it is 


mask maker : in this file i wrote some code to make my input data readable for my model i created
i download   some dataset from kaggle and i  use them for training my model and i use annotation_data_1 and image_dataset directory for train tumor segmentation and i ues no , yes directory for training tumor classification.


### some explanation


i ues  deep learning alghorithm call convolutional neural network(CNN) and dense neural network for train my data 
and  i use U-Net alghorithm for tumor segmentation beacuse U-Net is so accurate even with little dataset(like this case) and beacuse thease reason it is use a lot in medical AI model 

### Classification Model  Architecture 


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/bcae4663-322f-48a4-8d34-c10244abf755)



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/6c9dd3c0-d049-4361-a34a-bf418240cccc)




### Segmentation Model Architecture

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/8beebee2-3dec-41a7-bfe8-3ba977fdcf87)




### Model Performance Statistics 


evaluate on classification test dataset :

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/ac769932-b888-4408-8888-09298a235ce6)



statistics during training classification model : 


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/39f29f23-317e-4eb4-951a-fca4455912b7)





![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/6a73857b-5477-48a3-b127-72c2ec1d520d)



evaluate on segmentation test dataset :

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/be78de80-89e7-4121-afd3-22be509525c5)




statistics during training segmentation model  :



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/6c2504e0-6070-40d3-897e-573ae33fabb0)





![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/afe924df-6408-48af-a417-9dbafc6ef048)






  
