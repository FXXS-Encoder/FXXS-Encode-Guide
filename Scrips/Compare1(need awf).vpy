import vapoursynth as vs
import kagefunc as kgf
import fvsfunc as fvf
import mvsfunc as mvf
import havsfunc as haf
import awsmfunc as awf
import adptvgrnMod as agm


core = vs.core
#对比图需要帧率也保持，一致，一些老x264的帧率写成23.976会存在问题，跟24000/1001不匹配
#可以这么加载 encode = core.lsmas.LWLibavSource(source=r'',fpsnum = 24000,fpsden = 1001,format="yuv420p10")
 
#1引入
encode1 = core.lsmas.LWLibavSource(source=r".mkv",format="yuv420p10")
#2引入

encode2 = core.lsmas.LWLibavSource(source=r".mkv",format="yuv420p10")


#添加名字
encode1 = awf.FrameInfo(encode1,'encode1')
encode2 = awf.FrameInfo(encode2,'encode2')
out = core.std.Interleave([encode1,encode2])
out.set_output()