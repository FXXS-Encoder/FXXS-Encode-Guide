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
               f = codecs.open("%s.vpy" % title, "w", "utf-8")
               f.write('import vapoursynth as vs\nimport kagefunc as kgf\nimport fvsfunc as fvf\nimport havsfunc as haf\nimport vsTAAmbk as taa\nimport havsfunc as haf\nimport mvsfunc as mvf\nimport muvsfunc as muf\nimport nnedi3_resample as nnrs\nimport nnedi3_rpow2 as nnrp\n\ncore = vs.core\ncore.max_cache_size = 27384\n\nsrc = core.lsmas.LWLibavSource(source=r"'+title+'.mkv",format="yuv420p16")\n#src=core.std.Crop(src, left=240, right=242, top=0, bottom=0)\n#src = core.edgefixer.Continuity(src,left=3, right=3, top=0, bottom=0)\nsrc = fvf.Depth(src, 10)\n\nsrc.set_output()')
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