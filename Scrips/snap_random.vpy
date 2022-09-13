import vapoursynth as vs
import kagefunc as kgf
import fvsfunc as fvf
import havsfunc as haf
import vsTAAmbk as taa
import mvsfunc as mvf
import muvsfunc as muf
import nnedi3_resample as nnrs
import nnedi3_rpow2 as nnrp
import random
import awsmfunc as awf
#API3不能使用vs.core，请手动换回
#core = vs.get_core()
core = vs.core

# 信息写入图片

def createSnap(clip, title, numbers, fix):
    clip = awf.FrameInfo(clip,title)
    for i in numbers:
        o=i+fix;
        snap = core.imwri.Write(clip.resize.Spline36(format=vs.RGB24, matrix_in_s="709", dither_type="error_diffusion"),"PNG", str(i)+'-' + title + '(fix'+ str(fix) +').png', overwrite=True).get_frame(o)
    return snap

#载入源
#-------------source文件-------------------------#
video=core.lsmas.LWLibavSource(source=r'D:\Seed\Short Of Love 2009 Blu-ray 1080p AVC DTS-HD MA 7.1\BDMV\STREAM\00000.m2ts',format="yuv420p10") # 载入源


encode1 = core.lsmas.LWLibavSource(source=r'D:\Seed\Short Of Love 2009 Blu-ray 1080p AVC DTS-HD MA 7.1\BDMV\STREAM\Short Of Love - Blu-ray.hevc',format="yuv420p10")
#2引入


encode2 = core.lsmas.LWLibavSource(source=r'D:\Seed\Short Of Love 2009 Blu-ray 1080p AVC DTS-HD MA 7.1\BDMV\STREAM\Short Of Love - Blu-ray -knl - 24.hevc',format="yuv420p10")


encode3 = core.lsmas.LWLibavSource(source=r'D:\Seed\矮仔多情.Short.of.Love.2009.BluRay.1080p.x265.10bit.2Audio.MNHD-FRDS\Short.of.Love.2009.BluRay.1080p.x265.10bit.2Audio.MNHD-FRDS.mkv',format="yuv420p10")

#encode4 = core.lsmas.LWLibavSource(source=r"Short Of Love - Blu-ray -knl.hevc",format="yuv420p10")
#···同步压制脚本处理视频部分代码···#
#video=core.std.Crop(video,64,64, 0, 0)
#video=fvf.Depth(video, 10)
#···同步结束···#
i=1
numbers = []
while i < 6:
    numbers.append(random.randint(600,video.num_frames))
    i+=1

png=createSnap(video,"1.Source",numbers,0) #生成截图
png=createSnap(encode1,"2.High",numbers,0)
png=createSnap(encode2,"3.New Low",numbers,0)
png=createSnap(encode3,"4.old",numbers,-7)
encode3.set_output()