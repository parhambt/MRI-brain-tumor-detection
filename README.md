# این پروژه به هدف  تشخیص تومور مغزی و برای جشنواره جوان خوارزمی ساخته شده

در گام اول ما کتابخانه های مورد نظر را دانلود و سپس import میکنیم



- tensorflow
- opencv
- skleran
- numpy
- keras
- matplotlib


دیتا لود شده از فایل های yes , no برای train کردن مدل هست ( فایل های اصلی yes , no  هر کدام 1500 عکس داشتند اما به دلیل محدودیت گیت هاب در اپلود نشد تمام عکس ها اپلود شود )
و بعد دیتا را لود میکنیم و pre proccess های رایج مانند resize کردن و ... انجام میدهیم 
بعد از لود کردن دیتا باید برویم به سراغ ساخت مدل Convolutional neural network که تصاویر زیر به خوبی مدل هوش مصنوعی ساخته شده را تشریح میکنند 


![CNN map](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/57111c59-2eef-4e2d-ba7a-8da76b4ddcc5)
![neural network map](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/5b7fbde9-8c13-4232-a674-751beabea482)
![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/48566f99-2eee-449e-9bda-4570ad26f3da)

و بعد از ساخت مدل باید مدل را روی اطلاعات مخصوص train کردن train کنیم و بعد از ان باید به سراغ evaluate کردن مدل ساخته شده برویم تا بدانیم مدل ساخته شده تا چه حد قابل اتکا است


![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/6c3fcc9d-25e8-44d9-94c0-2d005eab9bf8)
![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/a7b71955-acdb-4ae5-a2d2-20b863d8c4c5)


خب همانطور که میبینید مدل ساخته شده با دقت بالای 90 درصد است و این یعنی کار ما خوب بوده است 
ما برای اینکه افراد غیر متخصص در کار با کامپیوتر بتوانند از این هوش مصنوعی train شده استفاده ببرند یک اپلیکیشن گرافیکی که بدون هیچ دانش فنی قبلی قابل استفاده هست هم درست کردیم که در فایل interface AI اس
موجود هست میتوانید فولدر inteface AI را دانلود کنید و بعد فایل main_app_interface.py را اجرا کنید برنامه ای مانند برنامه زیر برای شما باز خواهد شد :



![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/494a91ff-2f87-4701-b5b8-7b2e6fb841d1)
![image](https://github.com/parhambt/MRI-brain-tumor-detection/assets/124530126/85c7f16d-4dd2-4709-97ec-cdbea6897859)






## برای دیدن توضیحات تخصصی تر به 2 مقاله زیر مراجعه کنید 



https://docs.google.com/document/d/1-h8tFb-UcmNRq1bDEgR_p85YqujXjNzDqkKvziCaB5Q/edit?usp=sharing

https://docs.google.com/document/d/1NSXaa76TmP0o9osXxUlGiU-O8tC8RSA7hDvqFKz-1XM/edit?usp=sharing



پیغام tumor has been detected به معنای این است که عکس ورودی دارای تومور است و پیغام tumor has not been detected به معنای این است که عکس ورودی تومور مغزی ندارد 
