# 使用DEEW制作DDP/EAC3音轨教程

摆脱搭建MacOS环境困难以及Dolby Encode Suite单线程制作缓慢的烦恼，在Windows/Linux下通过命令行直接制作。

本文主要讲解Windows下的搭建，Linux下流程类似，自行摸索。

> 可能因其更新本教程内容会有所滞后，遇到区别时请以上游的[README](https://github.com/pcroland/deew#readme)为准。


## 环境准备
* [DEEW](https://github.com/pcroland/deew)
* [FFmpeg](https://ffmpeg.org/about.html)：[从 gyan.dev 下载](https://www.gyan.dev/ffmpeg/builds/) | [从 Github 下载](https://github.com/BtbN/FFmpeg-Builds/releases)

    若 **从 gyan.dev 下载**，请选择 *[ffmpeg-git-essentials.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z)* 版本；**从 Github 下载**则选择 *ffmpeg-master-latest-win64-lgpl* 版本即可，足够制作使用。

    解压并记录解压位置。
* Dolby Encoding Engine with Dolby AC-4 x64 (+license)



## 开始工作
使用DGDemux提取音轨


或直接将带有音频的视频输入

适合于Remux文件，无需任何提取，直接将`REMUX.mkv`作为输入源，默认将第一个音轨进行转换。

## Dolby Encoding Engine Wrapper使用

按住`Shift`键并右键空白区域，选择 **在 Windows终端 中打开** / **在此处打开 Powershell 窗口**，输入


```shell
.\deew.exe -v
```

确认正常返回版本号即可开始制作。

**参数解析**

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

- 以THD5.1为输入源 制作DDP5.1@1024kbps / 768kbps

  ```shell
  deew.exe -i '4588 PID 1100 48000 6ch eng DELAY 0ms.thd'
  ```

- 以DTS7.1为输入源 制作DDP7.1@1536kbps

  ```shell
  deew.exe -i 00001.mpls_3eng.dts
  ```

![DEEW encoding](https://camo.githubusercontent.com/c5f401d6aec11b6f742d43f75f002ec7b44b7d010af07ce36036e835dc28f8e7/68747470733a2f2f74656c656772612e70682f66696c652f3730633830306231353362396665396138383530392e676966)

完成后将在运行目录下找到与输入名称相同的`.ec3`文件，制作完成。

补充范例拓展，有需要的类推
- 以REMUX为输入源 将第一条音轨按默认设置制作

  ```shell
  deew.exe -i 'REMUX.mkv'
  ```

- 以 `D:\DDP\demux` 内所有 `.flac` 音频为输入源 批量生成动态范围为 *film_standard* 的DDP 并输出至 `D:\DDP\done` 

  ```shell
  deew.exe -i 'D:\DDP\demux\*flac' -o 'D:\DDP\done' -drc film_standard
  ```
  
  完成后将在 *D:\DDP\done*  下找到与输入名称相同的`.ec3`文件，制作完成。

- 以w64为输入源 制作DD2.0@448kbps

  ```shell
  deew.exe -i 'abcdefghijk.w64' -f dd -b 448
  ```

  完成后将在 *deew-main* 下找到与输入名称相同的`.ac3`文件，制作完成。

## 特别感谢

[pcroland](https://github.com/pcroland)/

所有对DEE无限制使用做出贡献的人

## Credit

教程遵守[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)，使用到的项目各自遵守其规范，转载请指明出处！
