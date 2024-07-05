# FXXS新手压制流程 V1.5

## 前言

越来越多新人加入了压制行列，但新人上手对教程不理解，不熟悉流程，容易踩到许多坑；且大佬们不是24小时在线，新人可能遇到的坑是前人踩过，反复回复相同问题增加了大佬的负担。故写下此~~指南~~流程（想了很久还是流程比较贴切），进一步降低教程门槛，使新人更易~~做鸭~~上手。

**必须阅读一遍 [官方教程](https://github.com/FXXS-Encoder/FXXS-Encode-Guide/blob/main/%E5%8E%8B%E5%88%B6%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B.md) 还有[基础知识](https://github.com/ted423/FXXS-Encode-Guide/tree/main/1.%20%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86) 了解原理，再阅读本流程，可能对整个压制流程能有一个大致的认识，帮助新人压出第一部作品。**

本文因编者水平有限，仅作为新人上手指导，其中不乏有疏漏，还望各位大佬指正，若有本文中没有提到的情况或其他不解之处，欢迎加群咨询大佬，在此对大佬的无私指导和指正**表示感谢！**



## 目录

![压制流程](/Picture/EnocdeFlow-pics/encodeflow.png)



## Let's Do This!

本文主要讲解```Windows10/11 x64```下压制环境的配置与使用，其他环境的用户可以选择性阅读。

```Linux```环境需要一定的程序员基础，参考这里[Linux工具](https://github.com/ted423/FXXS-Encode-Guide/blob/main/2.%20Tools/Linux.md)；```MacOS```环境中Intel架构的环境配置推荐[这篇文章](https://forum.doom9.org/showthread.php?p=1907899)，Arm架构(M1 Series)因架构因素依赖环境及插件均无法配置。

### 环境配置

- 压制部署包 (站内搜索 *压制部署包* )

  压制环境及工具打包，可以直接下载解压使用，省去了新人寻找压制工具的烦恼。有能力的可以手动部署相关工具。

  相关工具：[Vapoursynth](https://github.com/vapoursynth/vapoursynth/releases)、[Simple-x264-Launcher](https://github.com/lordmulder/Simple-x264-Launcher)、[eac3to](https://www.videohelp.com/software/eac3to)、[mkvtoolnix](https://mkvtoolnix.download/)

- [Python 3.9.x](https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe) (使用 *压制部署包* 无需安装)

  Python环境，手动部署的必须安装，使用压制部署包的可以不安装。

  安装时注意勾选 ***Add Python 3.9 PATH*** 以及 ***安装pip***

  ![PythonPATH](https://studyopedia.com/wp-content/uploads/2020/10/4.-Python-3.9-installation-started.png)

- (可选)[Mediainfo](https://mediaarea.net/download/binary/mediainfo-gui/21.03/MediaInfo_GUI_21.03_Windows.exe)/[PotPlayer](https://potplayer.daum.net/)/[k-lite](http://codecguide.com/download_kl.htm)

  用于生成媒体文件的信息。

- (可选)DEE+[DEEW](https://github.com/pcroland/deew)

  用于将DTS/TrueHD等无损音频转换为DDP的工具。

- (可选)[BDinfo](https://www.videohelp.com/software/BDInfo)

  用于查看蓝光原盘中的mpls信息。

- (可选)PowerDVD/DVDFab Player 5/[VLC](https://www.videolan.org/vlc/download-windows.html)

  用于原盘的观看和查看菜单信息，比较推荐DVDFab Player 5，大部分DIY原盘都可以用其打开。

- ~~(可选)~~[DGremux](http://rationalqm.us/dgdemux/dgdemux.html) (已在压制部署包20211204版内置)

  用于原盘的内容提取，类似于eac3to但对[音频时间戳友好](https://t.me/c/1467204597/39592)，避免可能出现的音画不同步问题。
  
- (可选)[SubtitleEdit](https://github.com/SubtitleEdit/subtitleedit/releases)/[Aegisub](http://aegi.vmoe.info/)

  用于字幕的查看和编辑。
  
- (可选)[noMacs](https://nomacs.org/download/)

  用于切换查看对比截图。
  
- (可选)[ChapterTool](https://github.com/tautcony/ChapterTool/releases/tag/2.33.33.332)

  用于在原盘中没有章节信息时手动生成。

本文主要以压制部署包为使用基础，对应其进行压制工作，若自行部署的可主要关注操作部分。

以上工具解压(路径请勿带中文)/安装、配置后，建议使用脚本生成快捷方式方便寻找各软件。双击运行`CreatLnk.bat`，所有工具的快捷方式将会在__Lnk_中生成。

开始之前，需要对 VapourSynth 的插件进行升级，打开_Lnk下的 ***VSRepoGUI***，按步骤更新插件并检查。

如果在使用其他软件时提示更新，请更新！

![VSGUI](/Picture/EnocdeFlow-pics/0_VSGUI.png)



### 选择片源

这里引用基础教程的话语。

> 要想做一个较为高质量作品，应采用最好的来源进行压制。HDR电影来源较为单一，4k的原盘和Remux资源为主，版本较少能选择不多。SDR目前可用压制版本较多，各个发行商的在不同时期也发行过不同蓝光版本，随着web的兴起，AZ和NF也都发布了较高码率的4k的SDR版本，所以在SDR压制时，需要对于来源进行对比，选取最为高质量的来源进行压制。对于蓝光原盘与remux两者相同时候，推荐使用Remux的更为方便。

总的说来，建议选择SDR的电影1080p**原盘**或**Remux**，新上手不推荐压制电视剧和演唱会或4K分辨率电影或DoVi/HDR视频源，电视剧大多为WEB-DL，不便确定其源质量；演唱会可能会遇到去交错、音源选择以及字幕问题，略有复杂不便上手；HDR需要另行计算亮度值，增加劝退可能性。

对于Remux，下载时可优先Hybrid 或 Remaster版本。

**选定资源前请务必确认是否有禁转、禁止二次压制等提示语！**



### 源预处理

> **使用Remux做为源的可以忽略此步骤。**

#### 原盘信息判断

- 从种子页面判断原盘中主要部分

  对于原盘来说，发布时BDInfo（可以认为是原盘的Mediainfo）是必须的。找到 **PLAYLIST REPORT**下的**Name**，即为目标```MPLS```。

  某些原盘因其版本原因，可能在BDInfo内展示多个MPLS，请按需选择。

  ![read BDInfo](/Picture/EnocdeFlow-pics/2_readInfo.png)

- 使用***BDInfo***判断原盘中主要部分

  > 对于原盘使用BDInfo检查原盘信息，查看原盘主要视频对应播放列表。对于复杂原盘，可能出现多版本混合的情况，需要确定所需要版本对应的MPLS，并确定原盘的主要码率 。

  ![BDInfo](/Picture/EnocdeFlow-pics/2_BDInfo.png)

  **一般**时长最长且文件最大的```.mpls```为目标播放列表（若为多版本请按需选择)，记下其名称，后续会用到。本文以```00001.mpls```举例。

#### 预混流

> 使用**eac3to**/**DGremux**提取视频流的可以忽略此步骤。

使用 ***MKVtoolnix*** 将原盘进行混流，打包为一个完整的影片(可以仅选择视频以节省体积)，方便作为VS的输入源。同时该操作有效防止肉酱盘中多m2ts文件致使压制输入源不便。

右键输入处空白-添加文件，选择之前确定的`00001.mpls`，随后的提示框选择"不扫描，仅添加文件"，命名输出，本文将`fxxsnb.mkv`举例，点击开始混流。

![mpls](/Picture/EnocdeFlow-pics/2_mkvmpls-g.png)



### 压制测试

以下均以 ***VapourSynth Editor*** 为使用范例，若想使用 ***AviSynth*** 请回看[官方教程](/%E5%8E%8B%E5%88%B6%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86.md)。

插入一段零基础代码小课堂，有Python基础的同学可以跳过。

**代码小课堂**

**注释就是对代码的解释和说明。** 目的是为了让别人和自己很容易看懂，一看就知道这段代码是做什么用的。

```python
# 在Python中,#是一个注释符号
```

注释虽然出现在代码中，但机器在运行这段代码时并不会运行注释，而是跳过它。所以不必担心它会对我们的使用造成影响，同时也因为这个特性，我们可以利用它来屏蔽掉一些我们不想运行的内容。

--------------------------------------------------

```python
import vapoursynth as vs
core = vs.get_core()
```

这段代码的意思是，导入```vapoursynth``` 组件并将```vs```作为别名，并调用了`get_core`这个方法。

有的函数还会在括号内填写内容，这称之为传递参数，将参数传递至函数，函数进行处理，反馈处理后的内容。

#### 压制脚本调整

打开_Link下***vsedit***，粘贴以下代码

```python
#导入相关函数
import vapoursynth as vs
import kagefunc as kgf
import fvsfunc as fvf
import havsfunc as haf
import vsTAAmbk as taa
import mvsfunc as mvf
import muvsfunc as muf
import nnedi3_resample as nnrs
import nnedi3_rpow2 as nnrp

##性能配置
#获取vs核心功能
core = vs.get_core()
#请依据自己实际内存调整(单位MB)
core.max_cache_size = 10240

##片源载入
#填写片源路径
source = r"J:\fxxsnb.mkv"
#加载片源，输入即为16bit色深
src = core.lsmas.LWLibavSource(source,format="yuv420p16")
#另一种加载片源方法，并调整为16bit色深
#src = core.ffms2.Source(source)
#src = fvf.Depth(src, 16)

##处理工具
#切边
src= core.std.Crop(src, left=0, right=0, top=20, bottom=20) #数值必须为偶数
#脏边处理相关
#src = core.fb.FillBorders(src, 0, 1, 0, 0, mode="fillmargins")
#src = core.edgefixer.Continuity(src, left=4, right=4, top=0, bottom=0)
#src = haf.FixRowBrightnessProtect2(src, 1, +34)

#反交错(正常不需要使用，多用于DVD及1080i等)
#src  = haf.QTGMC(src, Preset="slow", TFF=True)
#抗锯齿
#src = taa.TAAmbk(src, aatype=-3, preaa=-1, strength=0, mtype=2, opencl=True)

##Output Mode
#设置为1时脚本将抽取片段进行处理，并用于压制与源的对比
#设置为其他数值时(建议为0)，将正常处理全片
Output = 1
#以下为Output Mode的实现，请不要更改
if Output == 1:
	select = core.std.SelectEvery(src[8000:-8000],cycle=6000,offsets=range(60))
	clip = core.std.AssumeFPS(select, fpsnum=src.fps.numerator, fpsden=src.fps.denominator)
	clip = fvf.Depth(select, 10).set_output()
else:
	final = fvf.Depth(src, 10).set_output()
```

新手上路，建议只修改**内存调整**、**加载片源**、**切边**这三部分代码。**但不排除**还需要添加其他代码进一步调整。

内存调整：内存尽可能地给大，例如分配6G，即改为6144 (6*1024)。

加载片源：将路径替换为自己的片源路径。

切边：切除片源中带有的黑边(如图红框处)，可以将右下角的```No Zoom```改为```Fixed Ratio```，放大观察黑边是否切除干净。

![crop](/Picture/EnocdeFlow-pics/3_VSedit.png)

除了通过肉眼估算像素值，也可以使用 ***VSedit*** 的切边助手(如图蓝框处)，点击图标激活Crop assistant。在下方更改Left、Top、Right与Bottom数值，而后将参数回填至``core.std.Crop``函数中，或使用右侧的```Paste crop snippet into script```，并修改脚本（需要一定代码基础）。

```python
#Crop方法中，参数必须为偶数，黑边通常只出现在上下，即修改top与bottom参数
src = core.std.Crop(src, left=0, right=0, top=20, bottom=20)
#若遇到存在1像素这样的奇数边无法去除，可以补充一行脏边再切边。假设在底部有1行像素需要处理
src = core.fb.FillBorders(src, left=0, right=0, top=0, bottom=1, mode="fillmargins") 
src = core.std.Crop(src, left=0, right=0, top=0, bottom=2)
#若遇到存在1像素这样的奇数边无法很好的修复
src = core.resize.Spline36(src, 1920, 1038 src_left=0 , src_top=2 , src_width=1920 , src_height=1038)
```

在编辑器内保存代码（本文举例为```encode.vpy```），并且选择```Script```-```Preview```进行预览。第一次预览时需要创建```.ffindex/.lwi```索引文件用于预览使用，此时**界面将会卡死无响应属于正常现象**，耐性等待Preview窗口出现。

#### 压制参数配置

打开_Lnk下的 ***x264_launcher_portable***，选择`Application `- `Create New Job`。

Source选择刚才保存的```encode.vpy```，Output会自动输出```hevc```至与脚本相同的路径下，推荐使用预设模板```FRDS rd 4 pmode crf 21```。（具体参数[详见](https://github.com/ted423/FXXS-Encode-Guide/blob/main/%E5%8E%8B%E5%88%B6%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B.md#1%E5%B8%B8%E7%94%A8%E5%9F%BA%E7%A1%80%E5%8F%82%E6%95%B0)）

![Simple-x264 Launcher](/Picture/EnocdeFlow-pics/3_simplex264.png)

正式压制前使用脚本内的压制抽取，通过生成的``.hevc``可以大致判断全片的码率及体积。通过调整CRF数值，在17-23范围内以0.5步进（如果机器性能较差可以以1为步进，找到差距较小的两个值(*例如18与19*)再取其中间值(*例如18.5*)）进行测试，观察与原片在细节（*纹理、边缘等*）上是否有明显丢失，找到一个质量与体积最佳平衡的CRF数值用于正式压制。**一般**推荐码率不超过源码率(原盘为输入源时)的50~75%，过高的码率将会使HEVC编码优势丧失。

这里引用进阶教程的测试流程，这里涉及到更多参数的调整，视自身情况操作。

>通常情况下，你会想先测试一下码率。只要在几个不同的CRF下编码，并与源画面进行比较，找到与源码视觉上无差别的最高CRF值。现在，将该值四舍五入，最好是向下，然后切换到2-pass。对于标准测试，测 试 `qcomp` （步进为0.05）、 `aq-modes` 、 `aq-strength` （步进为0.05） `merange`（32、48或64）、`psy-rd`（步进为0.05）、 `ipratio` / `pbratio` （步进为0.05，并保持两者间0.10的差值），然后 `deblock` （步进为1）。如果你认为 mbtree 有帮助（即你在对动画进行编码），在打开 mbtree 的情况下重新进 行这个过程。你可能不会想太多地改变顺序，但当然也可以这样做。 
>
>对于x265，测试调整顺序应该是 qcomp 、 aq-mode 、 aq-strength 、 psy-rd 、 psy-rdoq 、 ipratio 和 pbratio ，最后 deblock 。
>
> 如果你想要提高一点额外的效率，你可以在你最终决定的每个设置的数值周围用较小的步进再次进行测试。建议在你已经对每个设置做了一次测试之后再做，因为它们都会对彼此产生轻微的影响。 一旦你完成了对2-pass设置的测试，就切换回 CRF，重复寻找视觉无损的 CRF 值过程。

建议在测试后生成一组对比图进行对比。

制作对比图需要使用到一些代码，打开***VapourSynth Editor***，粘贴以下代码

```python
import vapoursynth as vs
import kagefunc as kgf
import fvsfunc as fvf
import havsfunc as haf
import vsTAAmbk as taa
import mvsfunc as mvf
import muvsfunc as muf
import nnedi3_resample as nnrs
import nnedi3_rpow2 as nnrp
import awsmfunc as awf
#API3不能使用vs.core，请手动换回
#core = vs.get_core()
core = vs.core


# 生成带信息的截图 （如有需要请更改截图帧数值）
def createSnap(clip, title):
    clip = awf.FrameInfo(clip,title)
    for i in [63222,3279,31811,58944,60514,93062]:
        snap = core.imwri.Write(clip.resize.Spline36(format=vs.RGB24, matrix_in_s="709", dither_type="error_diffusion"),"PNG", '%d-' + title + '.png', overwrite=True).get_frame(i)
    return snap

# VS editor输出显示bug，对于压制后的文件需要进行，进行处理。
def outfix(clip):
	encode = core.std.SetFrameProp(clip,prop="_Matrix",delete=True)
	encode = core.std.SetFrameProp(encode,prop="_Transfer",delete=True)
	encode = core.std.SetFrameProp(encode,prop="_Primaries",delete=True)
	return encode

#载入源
source=r"J:\fxxsnb.mkv"
encode=r"J:\encode.mkv"
#-------------source文件-------------------------#
video=core.lsmas.LWLibavSource(source) # 载入源
#···同步压制脚本处理视频部分代码···#
video=core.std.Crop(video,64,64, 0, 0)
#···同步结束···#
video=fvf.Depth(video, 10)
#png=createSnap(video,"source") #生成截图
video=awf.FrameInfo(video,"source") # 标记信息
#-------------encode文件-------------------------#
encode=core.lsmas.LWLibavSource(encode) # 载入编码后视频
encode=awf.FrameInfo(encode,"encode") # 标记信息
#png=createSnap(encode,"encode") #生成截图
encode=outfix(encode)# 输入修复
#-------------输出交错预览------------------------#
out = core.std.Interleave([video,encode]) # 交叉帧
out.set_output()
```

在编辑器内进行相应修改并保存代码（本文举例为```compare.vpy```），并且选择`Script` - `Preview`进行预览及对比。

![sendsnapshot](/Picture/EnocdeFlow-pics/3_savesnap.png)

生成用于正式发布的对比图时，请将 `createSnap()` 函数取消注释，并选择`Script` - `Preview`，出现Preview框前，会在其文件夹下生成截图。

~~PS：保存截图时可能出现同一数值帧两个源画面相差一帧的情况，属于正常现象，可以尝试调整压制源(video)为与encode源相同的输入函数，若依然无法调整可忽略。~~

PPS：很多人初次使用脚本时可能遇到```the 'clip' dimensions doesn't match...```的报错，原因是对比图脚本中没有对source做相应的同步修改，导致“画幅”不同无法生成。

例如压制时进行了切边操作，相应地在对比脚本中也需要对source文件进行切边操作。

![compare](/Picture/EnocdeFlow-pics/3_compare.png)



###  正式压制

确定脚本处理以及压制参数后即可开始正式压制。但正式压制前，还需要修改之前使用的```encode.vpy```，将代码中**Output**数值改为0。

```Add Job```后，就是漫长的等待，并且电脑不能关机或睡眠,但可以暂停。。。~~无聊时可以打开任务管理器看看满载的CPU~~

如果出现跑不满的情况，不必怀疑，是你的CPU太强了！需要多个任务同时方可吃满所有性能。

如需观看压制后的视频流(```.hevc```)，请使用VS载入并预览或者封装为mkv后播放，播放器无法直接播放```.hevc```。



### 音视频字幕混流

#### 音频处理

尽管源中的音轨形式多种多样，但主要使用```UsEac3To```进行音轨的提取，若源音轨符合要求可以直接输出。

打开_Lnk下的 ***UsEac3To***，点击```Settings```，检查辅助工具的路径是否正确。如果需要设置输出文件夹(Output Folder)，其路径不要带有中文/特殊符号。

点击```Input File```，选择之前确定的```00001.mpls```，随后会有一个命令行黑框出现，等待其读取结束，出现如图信息。

![useac3to](/Picture/EnocdeFlow-pics/4_useac3to.png)

在**Track Input and Output**处选择需要提取的内容序号及输出格式，点击```Add```，*Command Line*会出现刚才添加的任务，而后点击```RUN CL```，即可开始提取。

以下简单列举可能会遇到的音频情况：

- 影片产地母语

  - **(推荐)** 输出为DD+(EAC3)，有损格式，适用于音轨为5.1/7.1声道的TrueHD / DTS / DTS-MA

    环境搭建以及制作流程请参考[使用DEEW制作DDP音轨教程](/Audio/%E4%BD%BF%E7%94%A8Dolby%20Encoder%20Suite%E5%88%B6%E4%BD%9CDDP%E9%9F%B3%E8%BD%A8%E6%95%99%E7%A8%8B.md)

  - 输出为AC3，有损格式，适用于音轨为DTS/TrueHD或原本已是AC3

  - 输出为FLAC，无损格式，适用于音轨为2.0及以下声道的 PCM 或者 DTS-HD MA

- 影片非产地语言

  - (可选) 输出为DD+(EAC3)，适用于音轨为非产地语言但为原盘版本的音轨或国配音轨

  - 输出为AC3，适用于音轨为非产地语言但为原盘版本的音轨或国配音轨

- 解说/评论音轨

  - 输出为AC3，适用于音轨为TrueHD/DTS-*的解说/评论音轨
  - 输出为AAC，有损格式，输出时添加码率参数为128，兼容性优于opus
  - 输出为opus，有损格式，输出时添加码率参数为128

- 演唱会

  ***情况复杂以下仅供参考***

  - **(推荐)** 输出为DDP5.1/FLAC 5.1/TrueHD 5.1，尽可能地在音质与体积下权衡

  - FLAC/AAC 5.1，适用于音轨为PCM2.0


#### 字幕获取

混流过程中不免遇到没有中文字幕的情况，虽然可以生肉发布，但还是建议添加中文字幕，推荐几个字幕网站

[SubHD](http://subhd.tv)   [字幕库](https://zmk.pw)   [伪射手](https://assrt.net/)

找到字幕后请在播放器中载入字幕以核对其是否匹配源，如不匹配请进行调轴等工作。

#### 混流

![mkvtoolnix1](/Picture/EnocdeFlow-pics/4_mkv-g.png)

- 添加文件

  推荐将原盘作为输入源之一，方便直接导出其中的字幕轨以及章节信息。

  若原盘若没有章节信息，推荐使用[ChapterTool](https://github.com/tautcony/ChapterTool/releases/tag/2.33.33.332)以5-10min间隔生成章节点。

- 修改

  源中可能预置了简体/繁体/听障友好字幕或普通话/粤语/导评音轨，都需要进行相应标注。

  - 简体/繁体字幕

    选中字幕，将简体中文字幕名称修改为CHS，繁體中文字幕名称修改为CHT。简中字幕名称建议修改为CHS&ENG，以此类推。

    ![chs/t](/Picture/EnocdeFlow-pics/4_subtitle-CHST.jpg)

  - 听障友好字幕SDH

    选中字幕，将右侧```"Hearing impaired" flag```改为是。

  - 导评音轨

    选中导评，将右侧```"Commentary" flag```改为是，并且修改其名称为**Comment By XXX**(XXX为导评人)。

    ![comment](/Picture/EnocdeFlow-pics/4_audio-commentary.jpg)

  - 普通话/粤语音轨

    选中音轨，将普通话音轨名称```Mandarin```，粤语音轨名称标注为```Cantonese```。

- 检查

  确保视频、音轨、字幕和章节四者都有并保证顺序为 **视频 -> 音轨 -> 字幕 -> 章节**，以及需要时各自名称/Flag有相应标注。

  音轨推荐以 **原产地音轨 - 非原产地音轨 - 解说/评论音轨** 顺序排列

  字幕推荐以 **简体 - 繁体 - 英语 - 其他语言** 顺序排列。

- 命名规范

  输出时，请按以下格式进行命名。

  - 初级命名推荐复制源名再按以下范例修改。```<>```为必填，任何情况都必须有。

    ```The.Thomas.Crown.Affair.1999.BluRay.1080p.x265.10bit.DD2.0.MNHD-FRDS```

    即为 ```<影片名>.<年份>.<来源>.<分辨率>.<编码格式>.<位深>.<音轨格式>.<压制组>```

    ```
    <音频格式>：若为ac3格式则写为DDx.0(x为声道数)
    ```
  
  - 进阶命名范例如下，适用于更加复杂的情况。```()```为可选，视情况添加。
  
    `Adore.AKA.Perfect.Mothers.2017.GBR.Extended.Cut.1080p.BluRay.HDR.x265.10bit.DDP5.1.mUHD-FRDS`
  
    即为 ```(别名/欧洲/罗马音).(AKA).<影片名>.<年份>.(原盘版本).(版本信息).<来源>.<分辨率>.(视频效果).<编码格式>.<位深>.<音轨格式>.<压制组>```
  
    ```
    (别名/欧洲/罗马音).(AKA)：在影片拥有(例别名、欧洲、罗马音)时建议填写。必须要与 AKA 连用
    (版本信息)：在原片存在多种官方版本(例导演剪辑、加长版、CC版)时建议填写。
    (视频效果)：在视频带有HDR/DOVI(杜比视界)效果时建议填写。
    (原盘版本)：原盘标注在不同国家发行的版本(例GBR、GER)时建议填写。
    ```
  
  命名时字母与符号的使用需遵守以下：
  
  >允许的字符：
  >abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-
  >
  >严格禁止的字符：
  >'!"$%^&*()
  
  

### 发布工作

1. #### 获取mediainfo信息

   打开***Mediainfo***，点击`File` - `Open`，选择你要读取的文件，并点击`View` - `Text`，保存所有显示的内容。

   ![mediainfo-app](/Picture/EnocdeFlow-pics/5_mediainfo-app.png)

   也可以使用[Mediainfo的网页版](https://mediaarea.net/MediaInfoOnline)，拖动要读取的文件到虚线框或点击红框处找到要读取的文件，稍等片刻即可显示。

   （文件并不会上传到服务器，所以并不会很慢）

   ![mediainfo-ol](/Picture/EnocdeFlow-pics/5_mediainfo-ol.png)

   或者使用 [mtn.ccp.ovh](https://mtn.ccp.ovh/#mediainfo) 拖动要读取的文件到虚线框或点击虚线框处找到要读取的文件，稍等片刻即可显示，而后点击 *Copy as bbcode* ，即可自动生成bbcode格式信息。

   ![mediainfo-mtn](/Picture/EnocdeFlow-pics/5_mediainfo-mtn.png)

   又或使用***PotPlayer***播放视频，在画面中右键，`属性` - `文件信息`，并点击左下角“复制到剪贴板”，保存剪贴板内容。

2. #### 上传

   上传对比图需要使用到图床，可以使用自己曾经使用过的图床或选择下方图床

    (建议使用代理访问)[imgbox](https://imgbox.com/)   **(推荐)**[up.ccp.ovh](http://up.ccp.ovh)

   上传完成后，保存返回的直链，即 `https://abc.dfe.com/hgklmn.png`

3. #### 压制记录

   回复 论坛 --> 压制问题反馈及建议 --> 【FXXS压制组】新人作品作品交流与检查，记录压制相关内容，格式如下：

   ```bbcode
   [quote]
   压制片源：
   <压制使用的片源名称>
   [/quote]
   
   [mediainfo]
   <压制成品的mediainfo信息>
   [/mediainfo]
   
   [comparison=Source,FRDS]
   <对比图脚本截取的图片>
   https://xxxxxx.png
   [/comparison]
   
   [quote]
   <压制时使用的参数，可以在simple x264压制结束生成的log中找到>
   --crf 22 -D 10 --preset veryslow --high-tier --ctu 32 --rd 4 --subme 7 --ref 6 --merange=57 --me 3 --qg-size 8 --weightb --pmode --no-rect --no-amp --rskip 0 --tu-intra-depth 4 --tu-inter-depth 4 --range limited --no-open-gop --no-sao --no-early-skip --min-keyint=1 --rc-lookahead 100 --cutree --bframes 8 --vbv-bufsize 160000 --vbv-maxrate 160000 --colorprim bt709 --transfer bt709 --colormatrix bt709 --deblock -3:-3 --ipratio 1.3 --pbratio 1.2 --qcomp 0.65 --aq-mode 1 --aq-strength 1 --psy-rd 1.50 --psy-rdoq 1.00 --cbqpoffs -2 --crqpoffs -2
   [/quote]
   ```

4. #### 制作种子

   如果你正在使用的客户端支持做种，例如qBittorrent、utorrent，则可以直接制作种子，具体流程请[百度](https://cn.bing.com/search?q=qbittorrent%E5%A6%82%E4%BD%95%E5%88%B6%E4%BD%9C%E7%A7%8D%E5%AD%90)。

   如果并不使用上述客户端，可以[dottorrent gui](https://github.com/kz26/dottorrent-gui)、tranmission-create、[mktorrent](https://github.com/pobrn/mktorrent)等工具制作，具体教程请百度。

   使用到的tracker地址可以在`种子` - `发布`页面中看到。

5. #### 发布种子

   在网站中点击`种子` - `发布`，根据提示填写内容。实在不会填写，可以参考其他种子。

   注意检查副标题内是否存在不必要的标点符号。

   PT-gen们：[Rhilip](https://ptgen.rhilip.workers.dev/) / [BFDZ](https://www.bfdz.ink/tools/ptgen/) / [IYUU](https://api.iyuu.cn/ptgen/) / [自建](https://github.com/Rhilip/pt-gen-cfworker) / [电影信息查询脚本](https://greasyfork.org/zh-CN/scripts/38878-%E7%94%B5%E5%BD%B1%E4%BF%A1%E6%81%AF%E6%9F%A5%E8%AF%A2%E8%84%9A%E6%9C%AC) 
   
   简介如下格式：
   
   ```
   <影片信息（一般自动生成，未生成时通过ptgen手动生成）>
   [quote]
   压制片源：<压制使用的片源名称>
   感谢源发布者
   [color=blue][size=4]
   <源中的人为补充内容或压制时的其他修改例如字幕等
   例：字幕来源于abc@YYeTs>
   [/size][/color]
   [/quote]
   
   [mediainfo]
   <压制成品的mediainfo信息>
   [/mediainfo]
   
   [comparison=Source,FRDS]
   <对比图脚本截取的图片>
   https://xxxxxx.png
   [/comparison]
   ```
   
   点击**发布**！并在你的客户端上添加发布后的种子，校验后即可开始做种。

至此，你已经完成了一次压制工作！



## 结语

很高兴这个教程陪你完成了一次~~做鸭~~压制工作，但压制还有很多东西要学，在此推荐阅读以下**进阶教程**

压制插件、参数讲解：[压制高阶教程](https://github.com/ted423/FXXS-Encode-Guide/blob/main/%E9%AB%98%E6%B8%85%E8%A7%86%E9%A2%91%E8%BD%AC%E7%A0%81%E8%BF%9B%E9%98%B6%E6%8C%87%E5%8D%97.md) / [VCB压制组出品教程](https://vcb-s.nmm-hd.org/) / [Encode Mystery](https://guide.geeking.moe/)

HDR参数计算：[计算方法1](https://ted423.github.io/Document/HDR/) / [计算方法2](/x265%2520HDR%2520%25E5%258F%2582%25E6%2595%25B0%25E8%25AE%25A1%25E7%25AE%2597%25E6%2596%25B9%25E6%25B3%2595.md)

x264/x265参数讲解：[iAvoe](https://github.com/iAvoe/x264-x265-QAAC-ffprobe-Ultimatetutorial/blob/master/%E6%95%99%E7%A8%8B.md)

[脏线修复的各种方法](https://blog.cfandora.com/archives/118/)

[How to User eac3to](https://en.wikibooks.org/wiki/Eac3to/How_to_Use) / [eac3to使用教程](https://blog.cfandora.com/archives/189/)

还有这些工具网站

[VSDB](https://vsdb.top/) VS插件库

[blu-ray](https://www.blu-ray.com/) [dvdcompare](https://www.dvdcompare.net/) 蓝光发行查询

别忘了感谢过程中帮助过你的人~



## 引用

- [FXXS官方压制基本教程](/%E5%8E%8B%E5%88%B6%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86.md)
- FXXS小组守则V0.2
- [VapourSynth documentation](http://www.vapoursynth.com/doc/functions.html)
- [0day命名中字符规范](https://t.me/c/1467204597/43529)



## 更新日志

**2021.7.30 V1**

第一版，并于出版后几个小时后修正了导评音轨及非产地音轨的处理

**2021.8.18 V1.1**

感谢 @enjoypdd 指正，抽取代码有误。经测试，SelectEvery产生的结果必须由一个新变量保存，再对其进行调用，否则会导致压制出错。

补充转码为FLAC的情况以及混流时音频字幕的顺序。

**2021.9.15 V1.2**

修正在VSedit中切边的操作及AC3音轨时的命名错误

修正在0day命名中对国别的解释错误

添加1080p下通过resize切除奇数边的操作

压制抽取中画质的初级判断

若干细节补充和易化

**2021.12.11 V1.3**

感谢 @jrongbin 指正，对比图代码有误。经核查，缺少一条使video转换位置为10bit的代码导致片段不匹配，无法进行对比。

更改音轨输出判断

修正AC3音轨的命名

移动对比生成教程至测试压制

若干细节补充与纠正

**2022.1.14 V1.4**

Rename to FXXS新手压制流程 & Pulish in Github

修正及补充影片文件命名规范

修正压制脚本的错误注释

增加MediaInfo网页版

更换dottorrent-gui的链接

若干细节补充与纠正

**2022.2.27 V1.5**

增加remux的片源选择

压制脚本与对比脚本的代码及注释优化

增加mediainfo中的mtn （感谢胖哥的工具）

若干细节补充与纠正
