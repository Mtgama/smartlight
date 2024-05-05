from cx_Freeze import setup, Executable
import sys

# تنظیمات برنامه
options = {
    'build_exe': {
        'includes': ['sys', 'PyQt5.QtWidgets', 'PyQt5.QtGui', 'PyQt5.QtCore', 'cv2'],  # بسته‌های مورد نیاز به برنامه
        'include_files': ['E:\پروژه های برنامه نویسی\چراغ راهنمایی\main\light.ico'],  # اضافه کردن فایل آیکون به بسته اجرایی
    }
}

# ایجاد فایل exe
setup(
    name='SmartLight',
    version='1.0',
    description='توضیحات برنامه',
    options=options,
    executables=[Executable('main.py', base='Win32GUI')]  # افزودن پارامتر base برای GUI
)
