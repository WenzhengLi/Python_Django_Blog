import sys
from pathlib import Path


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
    fh = open("testfile.txt", "w")
    try:
        # 命令参数个数为1，生成当前目录的目录树
        if len(sys.argv) == 1:
            dirtree.set_path(Path.cwd())
            dirtree.generate_tree()
            # print(dirtree.tree)
            fh.write(dirtree.tree)
        # 命令参数个数为2并且目录存在存在
        elif len(sys.argv) == 2 and Path(sys.argv[1]).exists():
            dirtree.set_path(sys.argv[1])
            dirtree.generate_tree()
            # print(dirtree.tree)
            fh.write(dirtree.tree)
        # 命令参数个数为3并且目录存在存在
        elif len(sys.argv) == 3 and Path(sys.argv[1]).exists():
            dirtree.set_path(sys.argv[1])
            dirtree.generate_tree()
            dirtree.set_filename(sys.argv[2])
            dirtree.save_file()
        else:  # 参数个数太多，无法解析
            # print('命令行参数太多，请检查！')
            fh.write('命令行参数太多，请检查！')
    finally:
        print("目录树 写入文件成功")
    fh.close()
# ----Python_Django_Blog\
#     |----.idea\
#     |    |----.gitignore
#     |    |----inspectionProfiles\
#     |    |    |----profiles_settings.xml
#     |    |----misc.xml
#     |    |----modules.xml
#     |    |----Python_Django_Blog.iml
#     |    |----workspace.xml
#     |----manage.py
#     |----Python_Django_Blog\
#     |    |----asgi.py
#     |    |----settings.py	——项目配置文件
#     |    |----urls.py			——路由文件
#     |    |----wsgi.py
#     |    |----__init__.py
#     |----README.md

# ----Python_Django_Blog\
#     |----blog\
#     |    |----admin.py
#     |    |----apps.py
#     |    |----migrations\
#     |    |    |----__init__.py
#     |    |----models.py
#     |    |----tests.py
#     |    |----views.py
#     |    |----__init__.py