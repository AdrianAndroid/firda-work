#!/usr/bin/python3

import _thread
import time


# # 为线程定义一个函数
# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#
#
# # 创建两个线程
# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 2,))
#     _thread.start_new_thread(print_time, ("Thread-2", 4,))
# except:
#     print("Error: 无法启动线程")
#
# while 1:
#     pass


print("""
线程模块
Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。

_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。

threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：

threading. current_thread(): 返回当前的线程变量。
threading.enumerate(): 返回一个包含正在运行的线程的列表。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.active_count(): 返回正在运行的线程数量，与 len(threading.enumerate()) 有相同的结果。
threading.Thread(target, args=(), kwargs={}, daemon=None)：
创建Thread类的实例。
target：线程将要执行的目标函数。
args：目标函数的参数，以元组形式传递。
kwargs：目标函数的关键字参数，以字典形式传递。
daemon：指定线程是否为守护线程。
threading.Thread 类提供了以下方法与属性:

__init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)：

初始化Thread对象。
group：线程组，暂时未使用，保留为将来的扩展。
target：线程将要执行的目标函数。
name：线程的名称。
args：目标函数的参数，以元组形式传递。
kwargs：目标函数的关键字参数，以字典形式传递。
daemon：指定线程是否为守护线程。
start(self)：

启动线程。将调用线程的run()方法。
run(self)：

线程在此方法中定义要执行的代码。
join(self, timeout=None)：

等待线程终止。默认情况下，join()会一直阻塞，直到被调用线程终止。如果指定了timeout参数，则最多等待timeout秒。
is_alive(self)：

返回线程是否在运行。如果线程已经启动且尚未终止，则返回True，否则返回False。
getName(self)：

返回线程的名称。
setName(self, name)：

设置线程的名称。
ident属性：

线程的唯一标识符。
daemon属性：

线程的守护标志，用于指示是否是守护线程。
isDaemon()方法：
""")