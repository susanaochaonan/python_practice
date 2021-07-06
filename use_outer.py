import os
import win32process
import time

#os
# os.system("notepad")

#win32process 通过进程的方式
handle = win32process.CreateProcess(r'C:\Windows\notepad.exe', '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None, win32process.STARTUPINFO())
time.sleep(4)

win32process.TerminateProcess(handle[0], 0)
import win32event