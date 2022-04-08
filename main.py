from time import sleep
import cv2 as cv
from PIL import ImageGrab
from pyautogui import click, moveTo


# 检测是否能访问网络
def check_network():
    import urllib.request
    try:
        urllib.request.urlopen("https://www.baidu.com")
        return True
    except:
        return False


# 停止程序
def stop_program():
    import os
    os.system("taskkill /f /im ESurfingNetClient.exe")


# 运行程序
def run_app(app_path):
    """
    打开指定程序
    """
    import subprocess
    subprocess.Popen(app_path)


# 获取当前目录所有jpg格式图片路径
def get_jpg_path():
    import os
    jpg_path = []
    for root, dirs, files in os.walk(get_current_path()):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                jpg_path.append(os.path.join(root, file))
    print("图片路径" + jpg_path[0])
    return jpg_path


# 获取当前目录
def get_current_path():
    import os
    path = os.path.dirname(os.path.realpath(__file__))
    print("当前目录" + path)
    return path


# 屏幕截图中查找指定图片坐标matchTemplate

def coordinate(original, part):
    img1 = cv.imread(original)
    img_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    template = cv.imread(part, 0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    # 最小匹配度，最大匹配度，最小匹配度的坐标，最大匹配度的坐标
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # print(min_val+max_val)
    if max_val > 0.8:  # 0到1可定义精度
        top_left = max_loc
        pos1 = [top_left[0] + w / 2, top_left[1] + h / 2]
        return pos1
    else:
        return -1


# 根据句柄编号后台点击指定位置
def Dclick(pos1):
    print(pos1)
    x = int(pos1[0])
    y = int(pos1[1])
    print(x, y)
    moveTo(x, y)
    click(x, y)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    while True:
        if check_network():
            print("网络连接正常")
        else:
            print("网络连接异常")
            stop_program()
            sleep(5)
            run_app("D:\ESurfingNet\ESurfingNetClient.exe")
            img = ImageGrab.grab()
            img.save('A.png')
            pos = coordinate('A.png', get_jpg_path()[0])
            print(pos)
            Dclick(pos)
    sleep(300)
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
