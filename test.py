import os



count_size()


def search_file():
    per_dir = input('请输入待查找的初始目录：')
    file = input('请输入需要查找的目标文件：')

    if os.path.exists(per_dir):
        pass
    else:
        print('输入的路径错误，找不到该目录')


