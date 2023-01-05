@echo off
ffmpeg -i "%~f1" -c:a libopus -b:a 65k "%~p1%~n1.opus"
if "%~x2" == "" (
  goto end
) else (
  ffmpeg -i "%~f2" -c:a libopus -b:a 65k "%~p2%~n2.opus"
)
:end
pause
