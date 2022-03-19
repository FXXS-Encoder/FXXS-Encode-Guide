# 使用DEEW制作DDP/EAC3音轨教程

摆脱搭建MacOS环境困难以及Dolby Encode Suite单线程制作缓慢的烦恼，在Windows/Linux下通过命令行直接制作。

本文主要讲解Windows下的搭建，Linux下流程类似，自行摸索。

> 本文跟随上游更新至Ver 1.2@[34437f3](https://github.com/pcroland/deew/commit/34437f3d365d5564743543ff42e89f698447d258)，可能因其更新本教程内容会有所滞后，遇到区别时请以上游的[README](https://github.com/pcroland/deew#readme)为准。

## 制作前准备

#### 环境准备

- [Python](https://www.python.org/downloads/windows/)

  下载 *Installer* 版，推荐使用**Install Now**，注意勾选 ***Add Python 3.x to PATH***

  ![PythonPATH](https://www.techruzz.com/images/How_to_Download_and_Install_Python_3_on_windows_10.png)
  打开命令行，分别输入 `python -V` 及 `pip --version`，若有返回则说明安装成功。

  ```shell
  C:\Users\FXXS>python -V
  Python 3.9.10
  
  C:\Users\FXXS>pip --version
  pip 21.2.4 from C:\Program Files\Python\lib\site-packages\pip (python 3.9)
  ```

- [FFmpeg](https://ffmpeg.org/about.html)：[从 gyan.dev 下载](https://www.gyan.dev/ffmpeg/builds/) | [从 Github 下载](https://github.com/BtbN/FFmpeg-Builds/releases)

  若**从 gyan.dev 下载**，请选择 *[ffmpeg-git-essentials.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z)* 版本；**从 Github 下载**则选择 *ffmpeg-master-latest-win64-lgpl* 版本即可，足够制作使用。
  
  解压并记录解压位置。

#### 工具下载

- Dolby Encoding Engine 5.1.0 (+license)

  解压 *dewi.rar*，得到如下内容：

  ![dewi install](/Picture/DDP-pics/deew-0install1.png)

  双击 *dolby_encoding_engine_install*，根据提示按下Enter同意两次，而后根据提示输入`accept`同意，根据自己喜好输入安装路径，安装完毕。

  打开上图中 *Crack* 文件夹，将其中两个文件(*dee.exe* 及 *license.lic*)复制，找到刚才安装 *dolby_encoding_engine* 的位置并粘贴，提示是否覆盖时点是即可。

- [Dolby Encoding Engine Wrapper](https://github.com/pcroland/deew)

  已安装 *Github Desktop* 的可以使用 `git clone` 命令下载项目，没有的可以点击右上角`Code` - `Download ZIP`来下载并解压，得到如下内容：

  ![deew install](/Picture/DDP-pics/deew-0install2.png)

  按住`Shift`键并右键空白区域，选择 **在 Windows终端 中打开** / **在此处打开 Powershell 窗口**，输入

  ```shell
  pip install -r requirements.txt
  ```

  安装完成后即可关闭窗口。

  之后打开 *config.toml.example*，修改各依赖软件的位置。

  ```toml
  ffmpeg_path = 'D:\DDP\ffmpeg\bin\ffmpeg.exe' # ffmpeg的解压位置
  dee_path = 'D:\DDP\dolby_encoding_engine\dee.exe' # dolby_encoding_engine的安装位置
  temp_path = 'D:\DDP\Temp' # 临时路径 可以留空不设置
  # empty: next to the script
  # relative path: from your current directory
  # you can also use fullpath
  # in any case will be created automatically if it doesn't exist already
  wsl = false # set this to true if you run the script in Linux but use the Windows version of DEE
  logo = 1 # set between 1 and 10, use the -pl/--printlogos option to see the available logos, set to 0 to disable logo
  ```
  
  修改完毕后请将文件名从 *config.toml.example* 改为 *config.toml*。

## 开始工作

~~使用eac3to提取音轨(不推荐,见issue)~~

~~点击**Input File**导入原盘文件，找到原盘中需要提取多声道的音轨序号，例如图中为序号3的TrueHD 5.1声道的音轨，**输出为thd**，**Add**并**Run CL**，等待输出。~~

~~/Picture/DDP-pics/deew-1eac3to.png~~

由于每个盘其音轨制作方式不同，格式也有所不同，请选择输出时不要转换格式，即输出源格式。例如源为DTS，那么输出时也选择该格式。

### 使用DGDemux提取音轨

点击**Browse**导入原盘文件，找到原盘中需要提取多声道的音轨序号，例如图中为序号3的TrueHD 5.1声道的音轨，勾选后点击**Demux**。

![DGDemux](/Picture/DDP-pics/deew-1dgdemux.png)

若原盘音轨格式为THD，请勾选右侧 ***Do not split THD***，本流程无需其ac3兼容内核。

### (可选)直接将带有音频的视频输入

适合于Remux文件，将`Remux.mkv`作为输入源，默认将第一个音轨进行转换。

### Dolby Encoding Engine Wrapper使用

找到先前解压的*deew-main*，按住`Shift`键并右键空白区域，选择 **在 Windows终端 中打开** / **在此处打开 Powershell 窗口**，输入

```shell
python deew.py -v
```

确认正常返回版本号即可开始制作。

**参数解析**

>./deew.py
>usage: deew.py [-h] [-v] [-i [INPUT ...]] [-o OUTPUT] [-f FORMAT] [-b BITRATE] [-m MIX] [-drc DRC] [-t THREADS] [-k] [-pl]
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
                        DD5.1: 640
                        DDP5.1: 1024
                        DDP7.1: 1536
  -m MIX, --mix MIX 6/8 指定降低/升高声道, 仅对DDP有效
                        DD格式无论是否7.1声道都将自动降至5.1声道
  -drc DRC              动态范围控制
                        film_light/film_standard/music_light/music_standard/speech drc profile
                        默认值: film_light
  -t THREADS, --threads 使用的线程数
                        仅在多任务同时编码时有效，单任务编码无法提速
                        默认使用所有线程数-1
  -k, --keeptemp        保留临时文件
  -pl, --printlogos     show all logo variants you can set in the config
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

![DEEW encoding](/Picture/DDP-pics/deew-3encoding.webp)

完成后将在 *deew-main* 下找到与输入名称相同的`.ec3`文件，制作完成。

补充范例拓展，有需要的类推

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

HLW大佬搬运的deei

[响度的计算](https://0bin.net/paste/7fhDvcxF#dcWxrUkGRoUmSCg6EMkJBIpNNNz-+uvYzYwcb1UZMDe)（其附有更多命令范例）

## Credit

教程遵守[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)，使用到的项目各自遵守其规范，转载请指明出处！
