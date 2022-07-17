@echo off
if "%~x1" ==".mkv" (
  ffmpeg -i "%~f1" -map 0:1 -c:a flac -compression_level 8 "%~p1%~n1.flac"
)
else (
  ffmpeg -i "%~f1" -c:a flac -compression_level 8 "%~p1%~n1.flac"
)
pause
