import vapoursynth as vs
import kagefunc as kgf
import fvsfunc as fvf
import mvsfunc as mvf
import havsfunc as haf
import awsmfunc as awf
import adptvgrnMod as agm


core = vs.core
core.max_cache_size = 16384
#1引入
encode1 = core.lsmas.LWLibavSource(source=r".mkv",format="yuv420p10")
#2引入

encode2 = core.lsmas.LWLibavSource(source=r".mkv",format="yuv420p10")


#添加名字
encode1 = awf.FrameInfo(encode1,'encode1')
encode2 = awf.FrameInfo(encode2,'encode2')
out = core.std.Interleave([encode1,encode2])
out.set_output()