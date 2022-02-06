# 使用DEEW制作DDP/EAC3音轨教程

摆脱搭建MacOS环境困难以及Dolby Encode Suite单线程制作缓慢的烦恼，在Windows/Linux下通过命令行直接制作。

本文主要讲解Windows下的搭建，Linux下流程类似，自行摸索。

## 制作前准备

#### 环境准备

- [Python](https://www.python.org/downloads/windows/)

  下载 *Installer* 版，推荐使用**Install Now**，注意勾选 ***Add Python 3.x PATH***

  ![PythonPATH](https://camo.githubusercontent.com/300953e0e128187dc9bb48ab3418435bbf21b4093a8dc77a02e555a013b35bdf/68747470733a2f2f73747564796f70656469612e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032302f31302f342e2d507974686f6e2d332e392d696e7374616c6c6174696f6e2d737461727465642e706e67)
  打开命令行，分别输入 `python -V` 及 `pip --version`，若有返回则说明安装成功。

  ```shell
  C:\Users\FXXS>python -V
  Python 3.9.9
  
  C:\Users\FXXS>pip --version
  pip 21.2.4 from C:\Program Files\Python\lib\site-packages\pip (python 3.9)
  ```

- [FFmpeg](https://ffmpeg.org/about.html)：[从 gyan.dev 下载](https://www.gyan.dev/ffmpeg/builds/) | [从 Github 下载](https://github.com/BtbN/FFmpeg-Builds/releases)

  若**从 gyan.dev 下载**，请选择 *[ffmpeg-git-essentials.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z)* 版本；**从 Github 下载**则选择 *ffmpeg-master-latest-win64-lgpl* 版本即可，足够制作使用。
  
  解压并记录解压位置。

#### 工具下载

- [Dolby Encoding Engine 5.1.0 (+license)](https://mega.nz/file/dFIkyR6I#l4uxUdvgQM0lc1E24tppx9jDeEbDAhA-DwqGf0q2NTc)（mega网盘推荐使用代理下载）

  解压 *dewi.rar*，得到如下内容：

  ![dewi install](/Picture/DDP-pics/deew-0install1.png)

  双击 *dolby_encoding_engine_install*，根据提示按下Enter同意两次，而后根据提示输入`accept`同意，根据自己喜好输入安装路径，安装完毕。

  打开上图中 *Crack* 文件夹，将其中两个文件(*dee.exe* 及 *license.lic*)复制，找到刚才安装 *dolby_encoding_engine* 的位置并粘贴，提示是否覆盖点是即可。

- [Dolby Encoding Engine Wrapper](https://github.com/pcroland/deew)

  安装Github客户端的可以使用 `git clone` 下载项目，没有的可以点击右上角`Code` - `Download ZIP`来下载并解压，得到如下内容：

  ![deew install](/Picture/DDP-pics/deew-0install2.png)

  按住`Shift`键并右键空白区域，选择 **在 Windows终端 中打开** / **在此处打开 Powershell 窗口**，输入

  ```shell
  pip install -r requirements.txt
  ```

  安装完成后即可关闭窗口。

  之后打开 *config.toml*，修改各依赖软件的位置。

  ```
  ffmpeg_path = 'D:\DDP\ffmpeg\bin\ffmpeg.exe' # ffmpeg的解压位置
  dee_path = 'D:\DDP\dolby_encoding_engine\dee.exe' # dolby_encoding_engine的安装位置
  temp_path = 'D:\DDP\Temp' # 临时路径（请确保路径存在） 
  logo = 1 # which logo (1-8) to display at start (0 to disable) ./deew.py --printlogos
  ```

  本文以 `D:\DDP\Temp` 作为临时路径，后续将会用到。请按需要自行选择路径并在后续教程中注意替换。

## 开始工作

### 使用eac3to提取音轨

点击**Input File**导入原盘文件，找到原盘中需要提取多声道的音轨序号，例如图中为序号3的TrueHD 5.1声道的音轨，**输出为thd**，**Add**并**Run CL**，等待输出。

![eac3to](/Picture/DDP-pics/deew-1eac3to.png)

由于每个盘其音轨制作方式不同，格式也有所不同，请选择输出时不要转换格式，即输出源格式。例如源为DTS，那么输出时也选择该格式。

### (可选)使用DGDemux提取音轨

点击**Browse**导入原盘文件，找到原盘中需要提取多声道的音轨序号，例如图中为序号3的TrueHD 5.1声道的音轨，勾选后点击**Demux**。

![DGDemux](/Picture/DDP-pics/deew-1dgdemux.png)

若原盘音轨格式为THD，请勾选右侧 ***Do not split THD***，本流程无需其ac3兼容内核。

### Dolby Encoding Engine Wrapper使用

找到先前解压的*deew-main*，按住`Shift`键并右键空白区域，选择 **在 Windows终端 中打开** / **在此处打开 Powershell 窗口**，输入

```shell
python deew.py -v
```

确认正常返回版本号即可开始制作。

**参数解析**

>./deew.py
>usage: deew.py [-h] [-v] [-i [INPUT ...]] [-f FORMAT] [-b BITRATE] [-c CHANNELS] [-d DIALNORM] [-t THREADS] [-k] [-p] [--printlogos]
```ruby
可选参数:
  -h, --help            显示帮助信息
  -v, --version         显示版本信息
  -i [INPUT ...], --input [INPUT ...]
                        输入的文件/文件夹路径
  -f FORMAT, --format 输出格式
                        dd/ddp/thd (默认为 ddp)
  -b BITRATE, --bitrate 输出比特率
                        默认值:
                        DD5.1: 640
                        DDP5.1: 1024
                        DDP7.1: 1536
  -c CHANNELS, --channels 声道数
                        默认值: 6
  -d DIALNORM, --dialnorm 响度补偿
                        默认值: 0  (由软件自动依照计算值设置)
  -t THREADS, --threads 线程数 【似乎只有在多文件同时处理时有明显占用
                         默认使用所有线程数-1
  -k, --keeptemp        保留临时文件
  -p, --progress        使用进度条替代命令行显示
  --printlogos          show all logo variants you can set in the config
```

**响度补偿的计算** 已在此[commit](https://github.com/pcroland/deew/commit/9680c2b5e09db57b1bd160bfdb0bb9c9c2c361c2)后自动计算，不再需要。

~~[参考原文](https://0bin.net/paste/7fhDvcxF#dcWxrUkGRoUmSCg6EMkJBIpNNNz-+uvYzYwcb1UZMDe)~~

~~首先进行格式转换，找到 *ffmpeg* 的解压位置，在此打开终端，输入以下命令，生成音频过渡文件*intermediate.wav*。~~

```
.\ffmpeg -i "00001.mpls_3eng.dts" -c:a pcm_s24le -rf64 always D:\DDP\Temp\intermediate.wav
```

~~而后计算响度补偿，找到 *dolby_encoding_engine* 的安装位置，在此打开终端，输入以下命令。~~

```
.\dee -x .\xml_templates\measure_loudness\wav_measure_loudness_wav_manifest.xml -a "D:\DDP\Temp\intermediate.wav" -o "D:\DDP\Temp\MyWav_measured.wav" -o "D:\DDP\Temp\MyWav_loudness.xml" --temp "D:\DDP\Temp"
```

~~计算结束后回看过程，找到 **[Source loudness] dialogue_loudness=-xx.xx**，忽略小数只取整数位即为所求，本例即为28。在最终制作时，使用 `-d` 参数指定。~~

**举例**

以我们需要制作的DDP5.1及DDP7.1举例

- 以DTS为输入源 制作DDP5.1@1024kbps

  ```shell
  python deew.py -i 00001.mpls_3eng.dts -p
  ```

- 以THD为输入源 制作DDP7.1@1536kbps

  ```shell
  python deew.py -i '4588 PID 1100 48000 6ch eng DELAY 0ms.thd' -c 8 -p
  ```

![DEEW encoding](/Picture/DDP-pics/deew-3deew.png)

完成后将在 *deew-main* 下找到与输入名称相同的`.ec3`文件，制作完成。

补充DD2.0的例子，有需要的类推

- 以w64为输入源 制作DD2.0@448kbps

  ```shell
  python deew.py -i 'abcdefghijk.w64' -c 2 -b 448 -p
  ```

完成后将在*deew-main*下找到与输入名称相同的`.ac3`文件，制作完成。

## 特别感谢

[pcroland](https://github.com/pcroland)/**[deew](https://github.com/pcroland/deew)**

[响度的计算](https://0bin.net/paste/7fhDvcxF#dcWxrUkGRoUmSCg6EMkJBIpNNNz-+uvYzYwcb1UZMDe)（其附有更多命令范例）

## Credit

教程遵守[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)，使用到的项目各自遵守其规范，转载请指明出处！
