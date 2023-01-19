import subprocess

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
subprocess.run(["py", "-3.9", "/logger.pyw"], startupinfo=startupinfo)




