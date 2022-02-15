# Linux工具

## Docker
<https://github.com/gzycode39/docker-vapoursynth-yuuno/>

## Info
### BDInfoCLI-ng
<https://github.com/zoffline/BDInfoCLI-ng>

`docker run --rm -it -v <BD_PATH>:/mnt/bd -v <REPORT_DEST>:/mnt/report zoffline/bdinfocli-ng /mnt/bd /mnt/report` (iso需要挂载后再扫)

## Demux/Remux
### tsMuxer
<https://github.com/justdan96/tsMuxer>
### mkvtoolnix
<https://mkvtoolnix.download/downloads.html>
注意章节编辑器名称模板改成英文 `Chapter <NUM:2>`

### DGDemux
<http://rationalqm.us/dgdemux/dgdemux.html>

## Encode 
### FFmpeg
<https://ffmpeg.org/ffmpeg-all.html>

范例

`ffmpeg -i 1.dts -c:a flac -compression_level 8 1.flac`

`ffmpeg -i 1.mkv -map 0:1  -c:a flac -compression_level 8 chi.flac`