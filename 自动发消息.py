import pyautogui
import pyperclip
import time
import os
import base64
dic = {
    '好友列表.txt': '6Ieq5Yqo5YyW5rWL6K+VMw0K6Ieq5Yqo5YyW5rWL6K+VMA0K6Ieq5Yqo5YyW5rWL6K+VMg0K6Ieq5Yqo5YyW5rWL6K+VMQ==',
    '发送内容.txt': '6Ieq5Yqo5Y+R6YCB5raI5oGv77yM6K+35b+955Wl'
}

def write_file(data, route):
    get_file = base64.b64decode(data)		# 将base64数据进行解析
    with open(route, 'wb') as a:		# 输出文件到指定位置
        a.write(get_file)


def send():
    # 复制需要发送的内容到粘贴板
    fopen = open('发送内容.txt', 'r', encoding='utf-8')  # 注释:获取需要发送的内容
    lines = fopen.readlines()  # 注释:读取需要发送的内容
    p = []
    for i in lines:
        p.append(i)  # 注释:获取需要发送的内容每一列
        p = " ".join(p)  # 注释:将发送的内容转换生字符串
        pyperclip.copy(p)  # 注释:把内容复制到剪贴板
        # 模拟键盘 ctrl + v粘贴内容
        pyautogui.hotkey('ctrl', 'v')
        # 发送消息
        pyautogui.press('enter')


def send_msg(friend):
    # 搜索好友
    pyautogui.hotkey('ctrl', 'f')
    # 复制好友昵称到粘贴板
    pyperclip.copy(friend)
    # 模拟键盘 ctrl + v粘贴
    pyautogui.hotkey('ctrl', 'v')
    # 注释:暂停一秒,不然容易出现无法选择好友的情况
    time.sleep(1)
    # 回车进入好友消息界面
    pyautogui.press('enter')
    # 暂停两秒,不然容易出现消息无法输入
    time.sleep(2)
    # 注释:调用发送消息模块
    send()
    # 注释:发送
    pyautogui.hotkey('alt', 's')


if __name__ == '__main__':
    # for i in dic:
    #     try:
    #         path = os.path.split(os.path.realpath(i))[0]
    #         os.makedirs(path)
    #         print(path)
    #     except Exception as e:
    #         print(e)
    #         None
    #     write_file('%s' % dic[i], i)
    # 注释:获取客户群名字
    friend_name = []
    fopen = open('好友列表.txt', 'r', encoding='utf-8')
    friends_name = fopen.readlines()
    i = 0
    # 注释:打开微信
    pyautogui.hotkey('ctrl', 'alt', 'w')
    for name in friends_name:
        print(name)
        name = name.strip('\n')  # 去掉换行符
        friend_name.append(name)
        print(f"即将给{name}客户发送消息,输入1即刻发送")
        # shuru = 1  # int(input("请输入是否发送? 1即为发送"))
        # if shuru == 1:
            # 注释:循环给每个微信群发送消息
        for i in friend_name:
            print(f'发送给{i}')
            send_msg(i)
            friend_name.remove(i)
            time.sleep(0.5)
        # 注释:关闭微信
        pyautogui.hotkey('alt', 'f4')
