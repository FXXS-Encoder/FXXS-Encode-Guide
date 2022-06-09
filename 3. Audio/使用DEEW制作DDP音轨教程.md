# 使用DEEW制作DDP/EAC3音轨教程

摆脱搭建MacOS环境困难以及Dolby Encode Suite单线程制作缓慢的烦恼，在Windows/Linux下通过命令行直接制作。

本文主要讲解Windows下的搭建，Linux下流程类似，自行摸索。

> 本文跟随上游更新至Ver 2.0@[972afbe](https://github.com/pcroland/deew/commit/9dad62d12bfa1786180763f6125a77b3df021d24)，可能因其更新本教程内容会有所滞后，遇到区别时请以上游的[README](https://github.com/pcroland/deew#readme)为准。

## 制作前准备

#### 环境准备

以下方案二选一，视个人习惯选择

- pyinstaller打包版

  无需环境准备，跳过此步。

- Python脚本版

  - [Python](https://www.python.org/downloads/windows/)

    下载 *Installer* 版，推荐使用**Install Now**，注意勾选 ***Add Python 3.x to PATH***

    ![PythonPATH](https://www.techruzz.com/images/How_to_Download_and_Install_Python_3_on_windows_10.png)
    打开命令行，分别输入 `python -V` 及 `pip --version`，若有返回则说明安装成功。

    ```
    C:\Users\FXXS>python -V
    Python 3.10.4
    
    C:\Users\FXXS>pip --version
    pip 22.0.4 from C:\Program Files\Python\lib\site-packages\pip (python 3.10)
    ```

  - FFmpeg](https://ffmpeg.org/about.html)：[从 gyan.dev 下载](https://www.gyan.dev/ffmpeg/builds/) | [从 Github 下载](https://github.com/BtbN/FFmpeg-Builds/releases)

    若**从 gyan.dev 下载**，请选择 *[ffmpeg-git-essentials.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z)* 版本；**从 Github 下载**则选择 *ffmpeg-master-latest-win64-lgpl* 版本即可，足够制作使用。

    解压并记录解压位置。

#### 工具下载

- Dolby Encoding Engine 5.2.0 with Dolby AC-4 v5.2.0 x64 (+license)

  解压 *dewi.rar*，得到如下内容：

  ![dewi install](/Picture/DDP-pics/deew-0install1.png)

  双击 *dolby_encoding_engine_install*，根据提示按下Enter同意两次，而后根据提示输入`accept`同意，根据自己喜好输入安装路径，安装完毕。

  打开上图中 *Crack* 文件夹，将其中两个文件(*dee.exe* 及 *license.lic*)复制，找到刚才安装 *dolby_encoding_engine* 的位置并粘贴，提示是否覆盖时点是即可。

- [Dolby Encoding Engine Wrapper](https://github.com/pcroland/deew)

  - pyinstaller打包版

    进入[发布页](https://github.com/pcroland/deew/releases)，下载压缩包并解压，内有一个可执行文件及配置文件范例。

    如果你使用的是 Windows Defender，此时可能已经将其删除（猜测打包时缺少签名导致误报），请将其弄回来并添加白名单。

    打开 Windows Defender，依次找到 `“病毒和威胁防护”设置 - 排除项 - 添加或删除排除项“ - 添加排除项`，将整个解压文件夹或仅`deew.exe`加入即可。
  
  - Python脚本版

    已安装 *Github Desktop* 的可以使用 `git clone` 命令下载项目，没有的可以点击右上角`Code` - `Download ZIP`来下载并解压，得到如下内容：

    ![deew install](/Picture/DDP-pics/deew-0install2.png)

    按住`Shift`键并右键空白区域，选择 **在 Windows终端 中打开** / **在此处打开 Powershell 窗口**，输入
  
    ```
    pip install -r requirements.txt
    ```
  
    安装完成后即可关闭窗口。
  
  之后打开 *config.toml.example*，修改各依赖软件的位置。
  
  ```toml
  ffmpeg_path = 'D:\DDP\ffmpeg\bin\ffmpeg.exe' # ffmpeg的解压位置
  ffprobe_path = 'D:\DDP\ffmpeg\bin\ffprobe.exe' # ffprobe的解压位置
  dee_path = 'D:\DDP\dolby_encoding_engine\dee.exe' # dolby_encoding_engine的安装位置
  temp_path = '' # 制作过程中临时未见存放位置（需要搭配相应参数才能保留临时文件
  # empty: next to the script
  # relative path: from your current directory
  # You can also use fullpath too.
  # In any case the folder will be created automatically if it doesn't exist already.
  wsl = false # Set this to true if you run the script in Linux but use the Windows version of DEE.
  logo = 1 # Set between 1 and 10, use the -pl/--printlogos option to see the available logos, set to 0 to disable logo.
  show_summary = true # 显示总结
  threads = 6 # 线程数 只能设置在单线程至所有线程数-2之间。你可以使用 -t/--threads 覆盖这里的设置。
  ```
  
  修改完毕后请将文件名从 *config.toml.example* 改为 *config.toml*。

## 开始工作

~~使用eac3to提取音轨(不推荐,见issue)~~

~~点击**Input File**导入原盘文件，找到原盘中需要提取多声道的音轨序号，例如图中为序号3的TrueHD 5.1声道的音轨，**输出为thd**，**Add**并**Run CL**，等待输出。~~

由于每个盘其音轨制作方式不同，格式也有所不同，请选择**输出时不要转换格式，即输出源格式。** 例如源为DTS，那么输出时也选择该格式。

### 使用DGDemux提取音轨

点击**Browse**导入原盘文件，找到原盘中需要提取多声道的音轨序号，例如图中为序号3的TrueHD 5.1声道的音轨，勾选后点击**Demux**。

![DGDemux](/Picture/DDP-pics/deew-1dgdemux.png)

~~若原盘音轨格式为THD，请勾选右侧 ***Do not split THD***，本流程无需其ac3兼容内核。~~（新版本已取消该选项）

### (可选)直接将带有音频的视频输入

适合于Remux文件，无需任何提取，直接将`REMUX.mkv`作为输入源，默认将第一个音轨进行转换。

### Dolby Encoding Engine Wrapper使用

找到先前解压的*deew-main*，按住`Shift`键并右键空白区域，选择 **在 Windows终端 中打开** / **在此处打开 Powershell 窗口**，输入

```shell
python deew.py -v
```

如果是使用pyinstaller版，则应将命令中的 `python deew.py` 替换为 `.\deew.exe`，下同

```shell
.\deew.exe -v
```

确认正常返回版本号即可开始制作。

**参数解析**

> ./deew.py
> deew 2.0
>
> USAGE: deew.py [-h] [-v] [-i [INPUT ...]] [-o OUTPUT] [-f FORMAT] [-b BITRATE] [-dm DOWNMIX] [-d DELAY] [-drc DRC] [-dn DIALNORM] [-t THREADS]
>                [-k] [-mo] [-la] [-pl] [-cl]


```ruby
可选参数:
  -h, --help            显示帮助信息
  -v, --version         显示版本信息
  -i [INPUT ...], --input [INPUT ...]
                        输入的文件/文件夹路径
  -o OUTPUT, --output OUTPUT
                        输入的文件路径
                        默认为程序所在文件夹
  -f FORMAT, --format   输出格式
                        dd/ddp/thd (默认为 ddp)
  -b BITRATE, --bitrate 输出比特率
                        默认值:
                        DD:  1.0: 128 kbps, 2.0: 256 kbps, 5.1: 640 kbps
                        DDP: 1.0: 128 kbps, 2.0: 256 kbps, 5.1: 1024 kbps, 7.1: 1536 kbps
  -dm DOWNMIX, --downmix DOWNMIX 1 / 2 / 6
						指定降低/升高声道, 仅对DDP有效
                        DD格式无论是否7.1声道都将自动降至5.1声道
  -d DELAY, --delay DELAY
						指定延迟单位为ms、s或帧率
						帧率可以是数字、除法算式或ntsc/pal
						+/- 亦可使用 p/m 替代
						例如：-5.1ms, +1,52s, p5s, m5@pal, +10@24000/1001
						默认值：0ms
  -drc DRC              动态范围控制
                        film_light/film_standard/music_light/music_standard/speech drc profile
                        默认值: film_light
  -dn DIALNORM, --dialnorm DIALNORM    
						设置-31到0之间的响度值
                        0代表软件自动（将会使用DEE进行计算）
                        默认值: 0
  -t THREADS, --threads 使用的线程数
                        仅在多任务同时编码时有效，单任务编码无法提速
                        默认值：所有线程数-1
  -k, --keeptemp        保留临时文件
  -mo, --measure-only   仅使用DEE计算响度并显示于进度条上
                        overwrites format with ddp if specified
  -la, --long-argument  展示为每次输入的 ffmpeg 与 DEE 参数
  -pl, --printlogos     show all logo variants you can set in the config
  -cl, --changelog      show changelog
```

**举例**

以我们需要制作的DDP5.1及DDP7.1举例

- 以THD5.1为输入源 制作DDP5.1@1024kbps

  ```shell
  python deew.py -i '4588 PID 1100 48000 6ch eng DELAY 0ms.thd'
  ```

- 以DTS7.1为输入源 制作DDP7.1@1536kbps

  ```shell
  python deew.py -i 00001.mpls_3eng.dts
  ```

![DEEW encoding](https://camo.githubusercontent.com/c5f401d6aec11b6f742d43f75f002ec7b44b7d010af07ce36036e835dc28f8e7/68747470733a2f2f74656c656772612e70682f66696c652f3730633830306231353362396665396138383530392e676966)

完成后将在 *deew-main* 下找到与输入名称相同的`.ec3`文件，制作完成。

补充范例拓展，有需要的类推
- 以REMUX为输入源 将第一条音轨按默认设置制作

  ```shell
  python deew.py -i 'REMUX.mkv'
  ```

- 以 `D:\DDP\demux` 内所有 `.flac` 音频为输入源 批量生成动态范围为 *film_standard* 的DDP 并输出至 `D:\DDP\done` 

  ```shell
  python deew.py -i 'D:\DDP\demux\*flac' -o 'D:\DDP\done' -drc film_standard
  ```
  
  完成后将在 *D:\DDP\done*  下找到与输入名称相同的`.ec3`文件，制作完成。

- 以w64为输入源 制作DD2.0@448kbps

  ```shell
  python deew.py -i 'abcdefghijk.w64' -f dd -b 448
  ```

  完成后将在 *deew-main* 下找到与输入名称相同的`.ac3`文件，制作完成。

## 特别感谢

[pcroland](https://github.com/pcroland)/**[deew](https://github.com/pcroland/deew)**

所有对DEE无限制使用做出贡献的人

## Credit

教程遵守[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)，使用到的项目各自遵守其规范，转载请指明出处！
