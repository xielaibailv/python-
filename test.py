import requests
import urllib.request

# 批量下载多页图片
class BatchDownload:
    # 主函数
    def main(self):
        # 定义访问地址
        self.get_html()
        self.get_current_page()

    # 打开页面，获取html
    def get_html(self):  # 返回处理后的HTML对象
        pass

    # 获取当前页数
    def get_current_page(self):  # 返回当前页码int
        pass

    # 找到图片
    def get_pictures(self):  # 返回图片list
        pass

    # 下载图片
    def download_pic(self, ):  # 返回图片内容list
        pass

    # 保存图片
    def save_pic(self, file, pictures):
        for each in pictures:
            with open(file, "wb") as f:
                f.write(each)
