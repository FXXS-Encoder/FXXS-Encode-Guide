# 使用Dolby Encoder Suite制作DDP音轨教程

##  制作前准备

- MacOS 10.15及以下

  无物理MacOS环境请使用VMware+[VM Unlocker](https://github.com/DrDonk/unlocker)搭建虚拟机环境

  - VMware16Player [下载](https://www.vmware.com/go/downloadplayer) (非商业用途无需激活但无快照功能)
  - VMware15Workstation 15.5.0 [下载](https://download3.vmware.com/software/wkst/file/VMware-workstation-full-15.5.0-14665864.exe) (请自备激活码)

- Dolby Media Producer Suite

- [eac3to](http://madshi.net/eac3to.zip)

### 环境依赖

VMware与MacOS的安装不再赘述，[推荐阅读](https://zhuanlan.zhihu.com/p/337036027)，主要介绍虚拟机解锁MacOS流程，以Windows为例：

![vm-unlocker](/Picture/DDP-pics/ddp-0vm.png)

将压缩包解压至任意位置并进入windows文件夹，**按住Shift并右键空白位置**，选择**Windows Powershell/Windows终端中打开**。

在Powershell终端中输入 ```/Picture/DDP-pics/unlocker.exe install```

![poweshell](/Picture/DDP-pics/ddp-0shell.png)

稍等片刻，会有UAC提示（如果开启的话），点击**是**，随后跳出CMD命令行

![done](/Picture/DDP-pics/ddp-0done.png)

出现**Press any key to continue...** 即为成功，可以关闭窗口，解锁MacOS完成，可以打开VMware安装MacOS。

## 开始工作

#### 使用eac3to提取音轨

导入原盘文件，找到原盘中需要提取多声道的音轨序号，例如图中为序号3的DTS-MA 5.1声道的音轨

![eac3to read](/Picture/DDP-pics/ddp-1eac3to.png)

**输出为wavs**，**Add**并**Run CL**，等待输出，之后会得到六个wav文件，如图。假若提取的是7.1声道音轨，获得到八个wav文件，相比5.1声道音轨多出BL、BR两个文件。由于Dolby Media Producer Suite音轨命名与eac3to分轨命名略有差异，为方便软件自动匹配，需要更改文件名以适用于DDP，具体为**“SL=Ls、SR=Rs、BL=Lrs、BR=Rrs”**。

![eac3to output](/Picture/DDP-pics/ddp-1eac3.png)

#### Dolby Media Encoder SE使用

1. 新建Job

   ![New Job](/Picture/DDP-pics/ddp-2job.png)

2. 导入音频

   勾选**Dolby Digital Plus**，制作5.1时选**Standard** / 7.1时选**Blu-ray Disc**，点击```Destination Path```右侧的 **···** 选择输出路径，再选择任意音轨右侧的 **···** 选择对应音轨文件。

   若在输出音轨之后没有手动更改过文件名，则会出现匹配不上的情况，此时需要手动选择剩余未匹配到音轨的文件。

   制作**5.1**音轨时选择```5.1 EX-L,R,C,LFE,Ls,Rs```；制作**7.1**音轨时选择```7.1-L,R,C,LFE,Ls,Rs,Lrs,Rrs```

   之后任选一个音轨进行导入对应文件，如果在提取音轨后没有改名，则需要手动选择缺失的音轨其对应文件，最终填满所有音轨。

   ![Format & Target](/Picture/DDP-pics/ddp-2format.png)

   此页设置完成时如图。

   ![Channel Config](/Picture/DDP-pics/ddp-2wavs.png)

3. 参数设置

   填充完音轨，还需要设置一些参数，如图。

   Data Rate根据声道而变，**5.1**音轨时选择**1024 kbps**，**7.1**音轨时选择**1536 kbps**。

   ![Encode Settings](/Picture/DDP-pics/ddp-3settings.png)

   ![Encode Settings](/Picture/DDP-pics/ddp-3processing.png)

   参数设置完毕，点击右上角的**Encode**开始压制。

4. 文件输出

   由于我们没有新建Project，故此处不再新建，点击**No**。稍等片刻，左侧的窗口中Status将会发生变化。

   ![Encode Settings](/Picture/DDP-pics/ddp-4encode1.png)
   
   由于该软件为单线程应用，其压制过程会非常缓慢，耐心等待。
   
   最后得到后缀为```.ec3```(7.1时为```.eb3```)的文件，即为DDP音轨文件。

## 特别感谢

- [韩小王大佬提供的参数设置](https://t.me/c/1467204597/42995) | [备份](/Picture/DDP-pics/ddp-5refer.png)
- [MJ大佬的纠错及7.1声道制作](https://t.me/c/1467204597/63052)

## Credit

转载请指明出处！