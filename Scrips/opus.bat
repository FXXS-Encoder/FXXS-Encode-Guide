@echo off
ffmpeg -i "%~f1" -c:a libopus -b:a 65k "%~p1%~n1.opus"
pause
