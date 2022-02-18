# -*- coding: UTF-8 -*-
import codecs
from pathlib import Path
import sys

class DirectionTree(object):
   """生成目录树
   @ pathname: 目标目录
   @ filename: 要保存成文件的名称
   """

   def __init__(self, pathname='.', filename='tree.txt'):
       super(DirectionTree, self).__init__()
       self.pathname = Path(pathname)
       self.filename = filename
       self.tree = ''

   def set_path(self, pathname):
       self.pathname = Path(pathname)

   def set_filename(self, filename):
       self.filename = filename

   def generate_tree(self, n=0):
       if self.pathname.is_file():
           self.tree += '    |' * n + '-' * 4 + self.pathname.name + '\n'
           if self.pathname.name.endswith('.mkv'):
               title = self.pathname.name.replace(".mkv", "")
               f = codecs.open("%s.json" % title, "w", "utf-8")
               f.write('[\n  "--ui-language",\n  "zh_CN",\n  "--output",\n  "D:\\\\IT\\\\Rip\\\\Done\\\\'+title+'.mkv",\n  "--language",\n  "0:und",\n  "(",\n  "D:\\\\IT\\\\Rip\\\\Remux\\\\'+title+'.hevc",\n  ")",\n  "--no-video",\n  "--language",\n  "1:en",\n  "--language",\n  "2:zh",\n  "--track-name",\n  "2:Mandarin",\n  "--language",\n  "3:zh",\n  "--language",\n  "4:en",\n  "(",\n  "D:\\\\IT\\\\Rip\\\\Remux\\\\'+title+'.mkv",\n  ")",\n  "--track-order",\n  "0:0,1:1,1:2,1:3,1:4"\n]')
               f.close()
       elif self.pathname.is_dir():
           self.tree += '    |' * n + '-' * 4 + \
               str(self.pathname.relative_to(self.pathname.parent)) + '\\' + '\n'

           for cp in self.pathname.iterdir():
               self.pathname = Path(cp)
               self.generate_tree(n + 1)

   def save_file(self):
       with open(self.filename, 'w', encoding='utf-8') as f:
           f.write(self.tree)


if __name__ == '__main__':
   dirtree = DirectionTree()
   # 命令参数个数为1，生成当前目录的目录树
   if len(sys.argv) == 1:
       dirtree.set_path(Path.cwd())
       dirtree.generate_tree()
       print(dirtree.tree)
   # 命令参数个数为2并且目录存在存在
   elif len(sys.argv) == 2 and Path(sys.argv[1]).exists():
       dirtree.set_path(sys.argv[1])
       dirtree.generate_tree()
       print(dirtree.tree)
   # 命令参数个数为3并且目录存在存在
   elif len(sys.argv) == 3 and Path(sys.argv[1]).exists():
       dirtree.set_path(sys.argv[1])
       dirtree.generate_tree()
       dirtree.set_filename(sys.argv[2])
       dirtree.save_file()
   else:  # 参数个数太多，无法解析
       print('命令行参数太多，请检查！')