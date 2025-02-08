try:
    print("10"/0)
except ZeroDivisionError:
    print("نمیتوان عددی را تقسیم بر صفر کرد")
except ValueError:
    print("مقدار متغیر اشتباه است")
except TypeError:
    print("نوع متغیر اشتباه است")

try:
    print(n)
except NameError:
    print("متغیر غیر مجاز است")

try:
    pass
except ZeroDivisionError:
    print("نمیتوان عددی را تقسیم بر صفر کرد")
except Exception as e:
    print(e)
else:
    print("finish")

try:
    pass
except Exception as e:
    print(e)
else:
    print("finish3")
finally:
    print("finish2")