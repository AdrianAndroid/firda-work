# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
# 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', ' import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
import sys

print("Hello, Python！")

if False:
    print("Answer")
    print("True")
else:
    print("Anser")
    print("False")

print("---------")
print(r"this is ar line\n")
print("---------")
print("this " "is " "string")

x = 'noob'
sys.stdout.write(x + '\n')
sys.stdout.write("  hi  ")

"""
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
"""
x = "a"
y = "b"
# 换行输出
print(x)
print(y)
print("-----------")
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()
