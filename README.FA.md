# این پروژه به هدف  تشخیص تومور مغزی و مشخص کردن تومور مغزی در MRI ساخته شده 


## نحوه استفاده از اپلیکیشن تشخیص تومور 

در گام اول اخرین نسخه منتشر شده در بخش release گیت هاب را دانلود کنید و از حالت فشرده خارج کنید سپس وارد فایل اصلی شوید و در فایل دنبال فایل اجرایی(exe) با نام app_interface_5 بگردید و فایل را اجرا کنید کمی منتظر بمانید تا برنامه اجرا شود و سپس میتوانید از برنامه استفاده کنید 

### برای ران کردن کد ها حتما Anaconda را نصب کنید 
کدهای بخش parham_tumor_detection_1.ipunb در محیط jupyter notebook  نوشته شده و  بخش interface AI در محیط vscode نوشته شده برای اینکه بتوانید همزمان هم vscode و هم jupyter notebook را داشته باشید پیشنهاد می شود از Anaconda استفاده کنید که می توانید آن را از لینک زیر دانلود کنید :

https://docs.anaconda.com/free/anaconda/install/windows/

برای نصب پکیج ها در  Anaconda به توضیحات زیر توجه کنید  :

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/f8e823bb-fe05-423b-8bd0-ca934fd3aed6)



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/41d1127b-48c2-4537-b754-c950316b428b)



برای مثال برای نصب scikit-learn باید اینگونه عمل کرد : 


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/51b17bb6-dd01-4886-85ef-df3373ab482c)


و بعد باید enter زد 

### نحوه دانلود کردن فایل های گیت هاب
روی دکمه code که سبز رنگ نوشته شده کلیک می کنیم سپس روی گزینه Download zip کلیک کرده و بعد از دانلود، فایل را اکسترکت می کنیم

حتما دقت کنید پایتون 3.7 به بالا روی سیستم خود نصب داشته باشید این پروژه با پایتون 3.10.2 و 3.11.0 نوشته شده است.(البته اگر Anaconda که بالا پیشنهاد کردیم استفاده میکنید به صورت اتوماتیک همه چیز درست میشود )

راه های دانلود کردن کتابخانه های مورد نیاز 

- راه اول برای دانلود کردن کتابخانه های مورد نیاز: فایل Requierments.txt را دانلود کنید
 و در ترمینال pip install -r Requierments.txt را بزنید دقت کنید که ابتدا باید با استفاده از command line دایرکتوری خود را با استفاده از دستور cd به دایرکتوری ای ببرید که فایل Requierments.txt در آن وجود دارد.
- راه دوم: همچنین می توانید نام کتابخانه هایی که در زیر آمده است را تک به تک با دستور pip install نصب کنید به طور مثال برای نصب numpy باید از دستور pip install numpy و یا برای نصب opencv باید از دستور pip install opencv-contrib-python استفاده کنید.

  
در گام اول ما کتابخانه های مورد نظر را دانلود و سپس import می کنیم:



- numpy
- opencv-contrib-python
- tensorflow
- scikit-learn
- pillow
- pandas
- keras
- matplotlib


دیتا لود شده از فایل های yes , no برای train کردن مدل هست ( فایل های اصلی yes , no  هر کدام 1500 عکس داشتند اما به دلیل محدودیت گیت هاب ، تمام عکس ها  اپلود نشد )
و بعد دیتا را لود می کنیم و pre proccess های رایج مانند resize کردن و غیره را انجام می دهیم. بعد از لود کردن دیتا باید برویم سراغ ساخت مدل Convolutional neural network که تصاویر زیر به خوبی مدل هوش مصنوعی ساخته شده را تشریح می کنند:


![CNN map](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/d0ecb921-5afe-48a0-b4ba-932eaf0c9776)

![neural network map](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/9f178897-88a9-4b66-9055-365bcdbd9ad9)

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/75ef7ce4-8207-4f68-8b88-872dcd663f94)

و بعد از ساخت مدل باید مدل را روی اطلاعات مخصوص train کردن، train کنیم و بعد از آن باید به سراغ evaluate کردن مدل ساخته شده برویم تا بدانیم مدل ساخته شده تا چه حد قابل اتکا است.

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/e0c0749c-1694-4ddf-88aa-033d31fdb411)
![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/dcba4755-928c-4263-9938-5eb464c4998f)



خب همانطور که میبینید مدل ساخته شده با دقت بالای 90 درصد است و این یعنی کار ما خوب بوده است 
### فایل های مهم 
شما برای دیدن کد مدل هوش مصنوعی و ... می توانید فایل parham_tumor_detection_1 را باز کنید و برای دسترسی به مدل آموزش دیده می توانید از فایل pickel که به نام tumor_trained_model_by_parham ذخیره شده است استفاده کنید.


### محیط گرافیکی برای راحتی استفاده 



ما برای اینکه افراد غیر متخصص در کار با کامپیوتر بتوانند از این هوش مصنوعی train شده استفاده کنند، یک اپلیکیشن گرافیکی که بدون هیچ دانش فنی قبلی قابل استفاده هست هم درست کردیم که در فایل interface AI موجود می باشد. شما می توانید فولدر inteface AI را دانلود کنید و بعد فایل main_app_interface.py را اجرا کنید. برنامه ای مانند برنامه زیر برای شما باز خواهد شد :

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/c9eca128-9ad8-410b-84cb-96da2c02d9cc)


پیغام tumor has been detected به معنای این است که عکس ورودی دارای تومور است و پیغام tumor has not been detected به معنای این است که عکس ورودی تومور مغزی ندارد.


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/5f87f43c-552f-477f-92a1-8adcaacfb679)

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/7ee1289f-b6e7-4e09-9a2d-aa76002b0c5e)


## برای دیدن توضیحات تخصصی تر در مورد این کد ها به لینک های زیر مراجعه کنید 

https://docs.google.com/document/d/1Ks_FQasrY04Yzl6VKujV9JxzLBfAXbLxyykMz2dH51I/edit

