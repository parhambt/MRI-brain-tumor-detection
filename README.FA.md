#  پروژه  تشخیص تومور مغزی و مشخص کردن تومور مغزی در MRI 

برای این پروژه 2 مدل هوش مصنوعی با بهره گیری از الگوریتم های یادگیری عمیق ماشین استفاده شده و همینطور یک اپلیکیشن گرافیکی (.exe) هم برای استفاده افرادی که دانش کامپیوتری زیادی ندارند مانند پزشک ها و محققان حوزه علم پزشکی و ... درست شده است 


## نحوه استفاده از اپلیکیشن تشخیص تومور 

در گام اول اخرین نسخه منتشر شده در بخش release گیت هاب به نام app_GUI_interface.exe را دانلود کنید  فایل را اجرا کنید کمی منتظر بمانید تا برنامه اجرا شود و سپس میتوانید به راحتی از این  برنامه گرافیکی استفاده کنید. لازم به ذکر است با دانلود این برنامه لازم نیست شما هیچ گونه پیشنیازی برای این برنامه نصب کنید و تمامی پکیج ها و کتابخانه ها و حتی مفسر پایتون 3.11 یکجا در برنامه ای که دانلود میکنید گنجانده شده است 



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/20bbb3e9-4a16-433b-b9b8-e832149be346)




![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/341ce923-bd59-49e4-920c-7d45b71f1822)








### نصب پیش نیاز ها برای ران کردن مستقیم کد 


در اولین گام کد ها را دانلود کنید (Download zip) از گیت هاب یا اگر با گیت هاب اشنا هستید میتوانید در محیط دلخواهتون کد ها رو clone کنید




![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/f4a4b7c8-5efd-48ba-9a5e-9d137ecc16c5)







دقت داشته باشید روی کامپیوتر خود نسخه پایتونی که نصب دارید بالا تر از 3.7 باشد (بخش هوش مصنوعی پروژه با پایتون 3.10 و بخش گرافیکی پروژه با پایتون 3.11 نوشته شده است )

توصیه : شدیدا پیشنهاد میشود  در یک virtual envierment یا از اپلیکیشن Anaconda کد ها را استفاده کنید بعد از ساخت یک virtual envierment به وسیله command line دایرکتوری خود را به دایرکتوری virtual envierment تغییر دهید و سپس کتابخانه های مورد نیاز را نصب کنید ( البته اگر از Anaconda استفاده کنید virtual envierments به صورت اتومات ساخته میشود )



https://www.geeksforgeeks.org/python-add-packages-to-anaconda-environment/


https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/                                            


راه اول نصب پیش نیاز ها : میتوانید با استفاده از فایل Requierments.txt و با نوشتن دستور pip install -r Requierments.txt در command line تمامی کتابخانه های مورد نیاز را دانلود کنید 


راه دوم نصب پیش نیاز ها : میتوانید به صورت دستی تمام کتابخانه های زیر را نصب کنید به صورت مثلا اگر بخوایم tensorflow را نصب کنیم باید pip install tensorflow را در command line بنویسیم 


- tensorflow
- scikit-learn
- opencv-python
- numpy
- pillow
- pandas
- keras
- matplotlib


### فایل های مهم 


3 فایل مهم پایتونی داریم که اصل backend هوش مصنوعی پروژه رو این 3 فایل تشکیل میدهند 
فایل classification-tumor-finall : در این فایل ما کد های مربوط به مدل tumor_classification_trained_model_by_parham_2.h5 است که این مدل ما را قادر میسازد بتوانیم عکس های MRI مغزی را به تو کتگوریhas tumor, has note tumor تقسیم میکنید دقت این مدل بیشتر از 97% که این میزان دقت این مدل را مدل قابل اتکایی میکند 

فایل finall-version-tumor-segmentation : در این فایل ما کد های مربوط به مدل segmetation_parham.h5 است که این مدل ما را قادر میسازد عکس های MRI ای که مدل قبلی تشخیص has tumor دادند را مکان تومور در تصویر را مشخص میکند این مدل با دقت 98 درصدی binary accuracy به معنای این که 98 درصد محدوده حدودی تومور را درست مشخص میکند و دقت Dice_Coeffient بین 70% و 80% است به معنای این که ان محدوده حدودی توموری که با دقت 98% درست شناسایی شد با دقتی بین 70 الی 80 درصد کله اون محدوده رو مشخص میکنه این بدین معنی است که میانگین از کله محدوده تومور 70 80 درصد ان شناسایی میشود که نتیجه ای بسیار رضایت بخش است ( برای بهبود دقت Dice_Coeffient به اطلاعات annoatate گذاری شده بیشتری نیاز است)

فایل mask maker : در این فایل ما بخشی از اطلاعات که خروجی annoatate گذاریشان به صورت فایل .json بود را به صورت ماسک هایی با فرمت jpg در اوردیم که با این کار ما اطلاعات را قابل خواندن و استفاده در مدل هوش مصنوعی نوشته شده کردیم 

### معماری مدل Classification 


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/1bae35b0-b791-48e1-9ee2-0a599f16be6c)



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/f56ec67a-8978-4523-aeb9-556c77c57842)






### معماری مدل Segmentation 


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/09c5f484-0900-45d4-b354-e5ac416cf6c8)

### کارایی مدل های نوشته شده 

 کارایی مدل Classification بر روی دیتاست های test


 ![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/2fe40483-d33c-4a9a-8ec1-622bfdbcac84)



 امار های مدل Classification حین train شدن 

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/a9a0af65-cf83-4ef4-be7a-fd57997372ca)



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/7e1a5a1f-3ed0-4d61-996a-d746a94f9781)



 کارایی مدل Segmentation بر روی دیتاست های test


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/aa1e3b35-a609-40c1-9bf8-034f1d230385)


امار های مدل Segmentation حین train شدن 


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/c31a717e-9001-4174-a0d2-324e489d7298)




![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/5041e9f2-db19-4a5a-b227-2046982f79e3)






## برای دیدن توضیحات تخصصی تر روی لینک زیر کلیک کنید 

https://docs.google.com/document/d/19GeA3v8mwwp-5-1g65cJfTQxWOOc-y5lLJME7bkCtXE/edit?usp=sharing

