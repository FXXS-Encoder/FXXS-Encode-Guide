# -*- coding:utf-8 -*-
import os, sys
import json
import subprocess
import random
import os
# encoding="utf-8",
print(os.getcwd())

OUT_DIR = os.getcwd() + "/../out"
VIDEO_DIR = os.getcwd() +"/../video"

BIN_DIR = os.getcwd() +"/../bin"

BIN_SHELL_DIR = {
    "ffmpeg": "ffmpeg.exe",
    "ffprobe": "ffprobe.exe"
}

def pathApply(value):
    value = value.replace("/", "\\")
    return value
    

def runShell(shell):
    print(shell)
    ret = subprocess.run(shell, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8",
                         timeout=3)
    if ret.returncode == 0:
        return ret.stdout
    else:
        return ""

# 1:2 => 2.0
def scaleToFloat(scale):
    data = scale.split(":")
    return float(data[1]) / float(data[0])

# 获取截图实际尺寸。。。貌似sar没啥用。。
def getPicSize(mediaInfo, videoStreamIndex):
    width = mediaInfo["streams"][videoStreamIndex]["width"]
    height = mediaInfo["streams"][videoStreamIndex]["height"]
    sar = scaleToFloat(mediaInfo["streams"][videoStreamIndex]["sample_aspect_ratio"])
    dar = scaleToFloat(mediaInfo["streams"][videoStreamIndex]["display_aspect_ratio"])
    width = height / dar

    return [width, height]

# 判断是否是HDR
def isHdr(mediaInfo, videoStreamIndex):
    try:
        return "2020" in mediaInfo["streams"][videoStreamIndex]["color_primaries"]
    except:
        return False

# 格式化时间作为文件名的一部分
def sfomat(value):
    _value = int(float(value))

    _s = float(value) - _value
    res = ""
    h = 0
    m = 0

    if _value > 3600:
        h = _value // 3600

        _value = _value - h * 3600
        res = res + str(h) + "_"

    if _value > 60:
        m = _value // 60
        _value = _value - m * 60
        res = res + str(m) + "_"

    res = res + str(_value) + str(round(_s, 3))[1:]

    return res

# 随机某个时间生成截图
def cutPicture(url, isHdr, time, width, height, filename, index):
    print("正在生成第%d个截图" % (index + 1))
    print(BIN_SHELL_DIR["ffmpeg"] +  " -v quiet -ss " + time + " -i \"" + url + "\" -vcodec png -vframes 1 -pix_fmt rgb24 -y -vf scale=" + width + ":" + height + " " + filename + "-" + sfomat(
        time) + ".png")
    shell = pathApply(BIN_SHELL_DIR["ffmpeg"] +  " -v quiet -ss " + time + " -i \"" + url + "\" -vcodec png -vframes 1 -pix_fmt rgb24 -y -vf scale=" + width + ":" + height + " " + filename + "-" + sfomat(
        time) + ".png");
    if isHdr:
        shell = pathApply(BIN_SHELL_DIR["ffmpeg"] + " -v quiet -ss " + time + " -i \"" + url + "\" -vcodec png -vframes 1 -pix_fmt rgb24 -y -vf zscale=tin=smpte2084:min=bt2020nc:pin=bt2020:rin=tv:t=smpte2084:m=bt2020nc:p=bt2020:r=tv,zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,scale=" + width + ":" + height + " " + filename + "-" + sfomat(
            time) + ".png");

    # print(shell)
    os.system(shell)
    print("第%d个截图生成结束" % (index + 1))

# 获取视频信息
def getMediaInfo(url):
    print("开始获取信息:")
    shell = pathApply(BIN_SHELL_DIR["ffprobe"] + " -i \"%s\" -v quiet -of json -show_format -show_streams" % url)
    print(shell)
    res = runShell(shell)
    print(res)
    print("获取信息结束")
    return json.loads(res)

# 获取文件名
def getFileName(mediaInfo):
    filename = mediaInfo["format"]["filename"].split("\\")[-1]
    lastlen = len(filename.split(".")[-1]) + 1
    filename = filename[0:len(filename) - lastlen]
    return filename

# 获取视频信息中视频index
def getvideoStreamIndex(mediaInfo):
    for i in range(len(mediaInfo["streams"])):
        print(mediaInfo["streams"][i]["codec_type"])
        if mediaInfo["streams"][i]["codec_type"] == "video":
            return i;
            break


def main(url, times):
    mediaInfo = getMediaInfo(url)
    videoStreamIndex = getvideoStreamIndex(mediaInfo)
    print("videoStreamIndex 是:%d" % (videoStreamIndex))
    picSize = getPicSize(mediaInfo, videoStreamIndex)
    endTime = float(mediaInfo["format"]["duration"])
    filename = getFileName(mediaInfo)

    for index in range(times):
        cutPicture(url,
                   isHdr(mediaInfo, videoStreamIndex),
                   str(round(endTime * random.random(), 3)),
                   str(picSize[0]),
                   str(picSize[1]),
                   filename,
                   index,
                   )
    # print(mediaInfo)


if __name__ == "__main__":
    main("\\\\192.168.70.69\\Happy.Endings.S01.2011.Bluray.1080p.MNHD-FRDS\\Happy.Endings.S01E01.Pilot.1080p.Bluray.x265.10bit.DDP.5.1.MNHD-FRDS.mkv", 6)
