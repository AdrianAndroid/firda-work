import os
import sys
import frida
import codecs


class Process:
    apkName = ''
    jsPath = ''

    def __init__(self, apkName, jsPath):
        self.apkName = apkName
        self.jsPath = jsPath

    def readJsCode(self):
        if not os.path.isfile(self.jsPath):
            raise TypeError(self.jsPath + ' does not exists')
        with codecs.open(self.jsPath, 'r', 'UTF-8') as file:
            js_code = file.read()
        return js_code

    def messageCallback(self):
        def message(msg, data):
            if msg["type"] == 'send':
                print("[*] {0}".format(msg['payload']))
            else:
                print(msg)
        return message

    def start(self):
        print(self.apkName, self.jsPath)
        process = frida.get_remote_device().attach(self.apkName)
        js_code = self.readJsCode()
        # if not os.path.isfile(self.jsPath):
        #     raise TypeError(self.jsPath + ' does not exists')
        # with codecs.open(self.jsPath, 'r', 'UTF-8') as file:
        #     js_code = file.read()
        script = process.create_script(js_code)

        # def message(msg, data):
        #     if msg["type"] == 'send':
        #         print("[*] {0}".format(msg['payload']))
        #     else:
        #         print(msg)

        script.on('message', self.messageCallback())
        script.load()
        sys.stdin.read()


# frida使用非标准端口
# /data/local/tmp # ./fs_12.7.22_arm64 -l 127.0.0.1:31928  默认端口: 27046
# process = frida.get_device_manager().add_remote_device('127.0.0.1:31928').attach('FridaApp')
# if not os.path.isfile('./JavaHook.js'):
#     raise TypeError("./JavaHook.js does not exist")
# with codecs.open('./JavaHook.js', 'r', 'UTF-8') as file:
#     js_code = file.read()
# script = process.create_script(js_code)
# script.on("message", message)
# script.load()
# sys.stdin.read()

# adb forward tcp:31928 tcp:31928
class IPProcess(Process):
    __remoteIp = ''

    def __init__(self, apkName, jsPath, remoteIp):
        Process.__init__(self, apkName, jsPath)
        self.__remoteIp = remoteIp

    def start(self):
        print(self.apkName, self.jsPath, self.__remoteIp)
        process = frida.get_device_manager().add_remote_device(self.__remoteIp).attach(self.apkName)
        # if not os.path.isfile(self.jsPath):
        #     raise TypeError(self.jsPath + ' does not exists')
        # with codecs.open(self.jsPath, 'r', 'UTF-8') as file:
        #     js_code = file.read()
        js_code = self.readJsCode()
        script = process.create_script(js_code)
        # def message(msg, data):
        #     if msg["type"] == 'send':
        #         print("[*] {0}".format(msg['payload']))
        #     else:
        #         print(msg)
        script.on('message', self.messageCallback())
        script.load()
        sys.stdin.read()

# class USBProcess:
#     def start(self):
#         def message(msg, data):
#             if msg["type"] == 'send':
#                 print("[*] {0}".format(msg['payload']))
#             else:
#                 print(msg)
#         process = frida.get_usb_device().attach('com.example.xxx')
#         script = process.create_script