# pip install windows-curses (dùng cho terminal trên máy)
### dung cho terminal chung khi dã cài dặt python về máy 
### sau dó , tại folder này , mở terminal lên và nhập python main.py
### ---> game chạy trên terminal




### (dùng cho terminal tích hợp trong VSCode )
### (base) PS C:\Users\MSI> & C:/Users/MSI/AppData/Local/Programs/Python/Python313/python.exe c:/Users/MSI/Downloads/CodeSnake/main.py
### Traceback (most recent call last):
###   File "c:\Users\MSI\Downloads\CodeSnake\main.py", line 3, in <module>
###     import curses
###   File "C:\Users\MSI\AppData\Local\Programs\Python\Python313\Lib\curses\__init__.py", line 13, in <module>
###     from _curses import *
### ModuleNotFoundError: No module named '_curses'
### (base) PS C:\Users\MSI> C:/Users/MSI/AppData/Local/Programs/Python/Python313/python.exe -m pip install windows-curses
### Collecting windows-curses
###   Downloading windows_curses-2.4.1-cp313-cp313-win_amd64.whl.metadata (2.9 kB)
### Downloading windows_curses-2.4.1-cp313-cp313-win_amd64.whl (81 kB)
### Installing collected packages: windows-curses
### Successfully installed windows-curses-2.4.1

### [notice] A new release of pip is available: 25.0.1 -> 25.1.1
### [notice] To update, run: C:\Users\MSI\AppData\Local\Programs\Python\Python313\python.exe -m pip install --upgrade pip

### (base) PS C:\Users\MSI> C:/Users/MSI/AppData/Local/Programs/Python/Python313/python.exe c:/Users/MSI/Downloads/CodeSnake/main.py
# ---> game chạy trên terminal VSCode

