# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/6/9 18:03
#   email : youyou.xu@enesource.com
#   project_name :  python-study
#   file_name :  统计代码量
#   function： 统计自己的代码量


import easygui
import os


# 基本功能已经实现，但是只有一个统计总数的功能，没有显示出各个文件夹下所有文件的代码量
class CountCodeLines1:
    def __init__(self):  # 代码目标
        self.code_target = 100000
        self.code_lines = 0  # 存放代码文件名：行数

    # 展示结果
    def showresult(self):
        file_path = easygui.diropenbox("请选择想要统计的代码库：", "代码行数统计")
        # code_lines = self.countcodelines(file_path)
        self.countcodelines(file_path)

        rate_progress = (self.code_lines / self.code_target) * 100
        gap = self.code_target - self.code_lines
        if gap > 0:
            msg = "您目前共累计编写了%d 行代码，完成进度：% 0.2f %%\n离 %d 行代码还差了 %d 行，请继续努力" % (
            self.code_lines, rate_progress, self.code_target, gap)
            title = "统计结果"
            easygui.msgbox(msg, title)
        else:
            gap = abs(gap)
            msg = "恭喜你！你已经完成了{}行代码的目标！\n目前共累计编写了{}行代码，比目标超出{}行，请继续保持哟".format(self.code_target, self.code_lines, gap)
            title = "统计结果"
            easygui.msgbox(msg, title)

    # 计算每个文件的行数并加总
    def countcodelines(self, file_path):

        os.chdir(file_path)  # 进入到该目录
        dir_list = os.listdir(os.curdir)  # 获取该目录下所有文件
        # code_lines = 0  # 存放代码文件名：行数
        for each in dir_list:
            if os.path.isdir(each):  # 如果是目录，则递归查找
                self.countcodelines(each)
                os.chdir(os.pardir)  # 查找完后返回上一目录
            else:  # 如果是文件，则判断是否是py文件，是则统计
                if os.path.splitext(each)[1] == ".py":
                    with open(each, encoding='utf-8') as f:
                        for each_line in f:
                            self.code_lines += 1
                else:
                    pass


if __name__ == "__main__":
    game = CountCodeLines1()
    game.showresult()