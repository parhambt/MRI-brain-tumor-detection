# این پروژه به هدف  تشخیص تومور مغزی و برای جشنواره جوان خوارزمی ساخته شده
### برای ران کردن کد ها حتما Anaconda را نصب کنید 
کدهای بخش parham_tumor_detection_1.ipunb در محیط jupyter notebook  نوشته شده و برای نصب این محیط کافی است pip install notebook را در ترمینال خود وارد کنید و بخش interface AI در محیط vscode نوشته شده برای اینکه بتوانید همزمان هم vscode , jupyter notebook  داشته باشید پیشنهاد میشود از Anaconda استفاده کنید میتوانید ان را از لینک زیر دانلود کنید 

https://docs.anaconda.com/free/anaconda/install/windows/

برای نصب پکیج ها در  Anaconda به توضیحات زیر توجه کنید 

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/f8e823bb-fe05-423b-8bd0-ca934fd3aed6)



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/41d1127b-48c2-4537-b754-c950316b428b)



برای مثال برای نصب scikit-learn باید اینگونه عمل کرد : 


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/51b17bb6-dd01-4886-85ef-df3373ab482c)


و بعد باید enter زد 

### نحوه دانلود کردن فایل های گیت هاب
روی دکمه code که سبز رنگ نوشته شده کلیک میکنیم روی گزینه Download zip میزنیم و بعد از دانلود فایل را اکسترکت میکنیم 


حتما دقت کنید پایتون 3.7 به بالا روی سیستم خود نصب داشته باشید 
این پروژه با پایتون 3.10.2 و 3.11.0 نوشته شده 

راه های دانلود کردن کتابخانه های مورد نیاز 

- راه اول برای دانلود کردن کتابخانه های مورد نیاز فایل Requierments.txt را دانلود کنید و در ترمینال pip install -r Requiermentes.txt را بزنید دقت کنید که با استفاده از command line اول باید دایرکتوری خود را با استفاده از دستوری cd به دایرکتوری ببرید که فایل Requierments.txt وجود دارد
- راه دوم: همچنین میتوانید نام کتابخانه هایی که در زیر امده است تک به تک با دستور pip install نصب کنید به طور مثال برای نصب numpy باید از دستور pip install numpy و یا برای نصب opencv باید از دستور  pip install opencv-contrib-python باید استفاده کنیم

  
در گام اول ما کتابخانه های مورد نظر را دانلود و سپس import میکنیم



- numpy
- opencv-contrib-python
- tensorflow
- scikit-learn
- pillow
- pandas
- keras
- matplotlib


دیتا لود شده از فایل های yes , no برای train کردن مدل هست ( فایل های اصلی yes , no  هر کدام 1500 عکس داشتند اما به دلیل محدودیت گیت هاب در اپلود نشد تمام عکس ها اپلود شود )
و بعد دیتا را لود میکنیم و pre proccess های رایج مانند resize کردن و ... انجام میدهیم 
بعد از لود کردن دیتا باید برویم به سراغ ساخت مدل Convolutional neural network که تصاویر زیر به خوبی مدل هوش مصنوعی ساخته شده را تشریح میکنند 


![CNN map](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/d0ecb921-5afe-48a0-b4ba-932eaf0c9776)

![neural network map](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/9f178897-88a9-4b66-9055-365bcdbd9ad9)

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/75ef7ce4-8207-4f68-8b88-872dcd663f94)


و بعد از ساخت مدل باید مدل را روی اطلاعات مخصوص train کردن train کنیم و بعد از ان باید به سراغ evaluate کردن مدل ساخته شده برویم تا بدانیم مدل ساخته شده تا چه حد قابل اتکا است

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/e0c0749c-1694-4ddf-88aa-033d31fdb411)
![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/dcba4755-928c-4263-9938-5eb464c4998f)



خب همانطور که میبینید مدل ساخته شده با دقت بالای 90 درصد است و این یعنی کار ما خوب بوده است 
### فایل های مهم 

شما برای دیدن کد مدل هوش مصنوعی و ... میتوانید فایل parham_tumor_detection_1 را باز کنید و برای دسترسی به مدل اموزش دیده میتوانید از فایل pickel  که به نام tumor_trained_model_by_parham ذخیره شده است استفاده کنید 


### محیط گرافیکی برای راحتی استفاده 


ما برای اینکه افراد غیر متخصص در کار با کامپیوتر بتوانند از این هوش مصنوعی train شده استفاده ببرند یک اپلیکیشن گرافیکی که بدون هیچ دانش فنی قبلی قابل استفاده هست هم درست کردیم که در فایل interface AI اس
موجود هست میتوانید فولدر inteface AI را دانلود کنید و بعد فایل main_app_interface.py را اجرا کنید برنامه ای مانند برنامه زیر برای شما باز خواهد شد :

![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/494a91ff-2f87-4701-b5b8-7b2e6fb841d1)
![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/85c7f16d-4dd2-4709-97ec-cdbea6897859)


پیغام tumor has been detected به معنای این است که عکس ورودی دارای تومور است و پیغام tumor has not been detected به معنای این است که عکس ورودی تومور مغزی ندارد 

## برای دیدن توضیحات تخصصی تر در مورد این کد ها به لینک های زیر مراجعه کنید 

https://docs.google.com/document/d/1-h8tFb-UcmNRq1bDEgR_p85YqujXjNzDqkKvziCaB5Q/edit?usp=sharing


https://docs.google.com/document/d/1NSXaa76TmP0o9osXxUlGiU-O8tC8RSA7hDvqFKz-1XM/edit?usp=sharing

