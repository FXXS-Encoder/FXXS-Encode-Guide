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

```
>deew -h
deew 2.9.5

USAGE: deew [-h] [-v] [-i [INPUT ...]] [-ti INDEX] [-o DIRECTORY] [-f FORMAT]
            [-b BITRATE] [-dm CHANNELS] [-d DELAY] [-r DRC] [-dn DIALNORM]
            [-in INSTANCES] [-k] [-mo] [-fs] [-fb] [-lb] [-la] [-np] [-pl]
            [-cl] [-c] [-gc]

FLAGS:
  -h, --help                  show this help message.
  -v, --version               show version.
  -i, --input [INPUT ...]     audio file(s) or folder(s)
  -ti, --track-index INDEX    default: 0
                              select audio track index of input(s)
  -o, --output DIRECTORY      default: current directory
                              specifies output directory
  -f, --format FORMAT         options: dd / ddp / thd
                              default: ddp
  -b, --bitrate BITRATE       options: run -lb/--list-bitrates
                              default: run -c/--config
  -dm, --downmix CHANNELS     options: 1 / 2 / 6
                              specifies downmix, only works for DD/DDP
                              DD will be automatically downmixed to 5.1 in case of a 7.1 source
  -d, --delay DELAY           examples: -5.1ms, +1,52s, -24@pal, +10@24000/1001
                              default: 0ms or parsed from filename
                              specifies delay as ms, s or frame@FPS
                              FPS can be a number, division or ntsc / pal
                              you have to specify negative values as -d=-0ms
  -r, --drc DRC               options: film_light / film_standard / music_light / music_standard / speech
                              default: music_light (this is the closest to the missing none preset)
                              specifies drc profile
  -dn, --dialnorm DIALNORM    options: between -31 and 0 (in case of 0 DEE's measurement will be used)
                              default: 0
                              applied dialnorm value between
  -in, --instances INSTANCES  examples: 1, 4, 50%
                              default: 50%
                              specifies how many encodes can run at the same time
                              50% means 4 on a cpu with 8 threads
                              one DEE can use 2 threads so 50% can utilize all threads
                              (this option overrides the config's number)
  -k, --keeptemp              keep temp files
  -mo, --measure-only         kills DEE when the dialnorm gets written to the progress bar
                              this option overrides format with ddp
  -fs, --force-standard       force standard profile for 7.1 DDP encoding (384-1024 kbps)
  -fb, --force-bluray         force bluray profile for 7.1 DDP encoding (768-1664 kbps)
  -lb, --list-bitrates        list bitrates that DEE can do for DD and DDP encoding
  -la, --long-argument        print ffmpeg and DEE arguments for each input
  -np, --no-prompt            disables prompt
  -pl, --print-logos          show all logo variants you can set in the config
  -cl, --changelog            show changelog
  -c, --config                show config and config location(s)
  -gc, --generate-config      generate a new config
```

**举例**

以我们需要制作的DDP5.1及DDP7.1举例

- 以THD5.1为输入源 制作DDP5.1@1024kbps / 768kbps

  ```shell
  deew.exe -i '4588 PID 1100 48000 6ch eng DELAY 0ms.thd'
  deew.exe -b 768 -i '4588 PID 1100 48000 6ch eng DELAY 0ms.thd'
  ```

- 以DTS7.1为输入源 制作DDP7.1@1536kbps / 1024kbps

  ```shell
  deew.exe -i 00001.mpls_3eng.dts
  deew.exe -b 1024 -i 00001.mpls_3eng.dts
  ```

![DEEW encoding](https://camo.githubusercontent.com/b93af93ef2097658248d07c9dd6ea979bff23aa910e6d70382fa88ba03ee0ccc/68747470733a2f2f74656c656772612e70682f66696c652f6566643261316433353139626466383766636130332e676966)

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
