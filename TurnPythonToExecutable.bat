@ECHO OFF

cd ..\..\PySystem\Python3\Scripts
pyinstaller.exe --onefile --noconsole --noupx ..\..\..\Programs\RandomKeyPress\JesusTakeTheWheel.pyw
Pause
