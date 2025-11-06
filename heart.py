import tkinter as tk
import random
import threading
import time
import sys
import os

# 全局退出标志
exit_program = False

def show_warm_tip():
    # 检查是否应该退出
    if exit_program:
        return

    # 创建主窗口
    window = tk.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 220
    window_height = 50
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)
    window.title('温馨提示')
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    tips = [
        "多喝水哦~", "保持微笑呀", "元气满满",
        "记得吃水果", "保持好心情", "好好爱自己", "我想你了",
        "梦想成真", "期待下一次见面", "金榜题名",
        "顺顺利利", "早点休息", "愿烦恼都消失",
        "别熬夜", "今天开心嘛", "天冷加衣"
    ]
    tip = random.choice(tips)
    bg_colors = [
        'lightpink', 'skyblue', 'lightblue', 'lightsteelblue', 'powderblue',
        'lightcyan', 'aliceblue', 'azure', 'lightgreen', 'lavender',
        'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine',
        'mistyrose', 'honeydew', 'lavenderblush', 'oldlace'
    ]
    bg = random.choice(bg_colors)

    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('微软雅黑', 16),
        width=30,
        height=3
    ).pack()
    window.attributes('-topmost', True)

    def on_space(event):
        """空格键事件处理函数：立即退出整个程序"""
        global exit_program
        exit_program = True
        # 强制退出程序
        os._exit(0)

    window.bind('<space>', on_space)
    window.mainloop()

threads = []
if __name__ == '__main__':
    for i in range(250):
        # 检查退出标志，如果已设置则不再创建新窗口
        if exit_program:
            break

        t = threading.Thread(target=show_warm_tip)
        threads.append(t)
        time.sleep(0.000001)
        t.start()