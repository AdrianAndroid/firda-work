# !/usr/bin/python3

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

print("多个变量赋值", end="\n")
a = b = c = 1
print(a)
print(b)
print(c)

print("Number（数字）", end="\n")
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d), isinstance(a, int), end="\n")
class A:
    pass
class B:
    pass
print(isinstance(A(), A), isinstance(B(), B), type(A()), type(B()))
print(issubclass(bool, int))
print()

print("String（字符串）", end="\n")
print("bool（布尔类型）", end="\n")
print("List（列表）", end="\n")
print("Tuple（元组）", end="\n")
print("Set（集合）", end="\n")
print("Dictionary（字典）", end="\n")
print("""不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。""", end="\n")

x = bytes("hello", encoding="utf-8")
print(x)
x = b"Hello"
y = x[1:3]
z = x + b"world"
print(z)
print("ord('h')", ord("h"))
print("""函数	描述
int(x [,base]) 将x转换为一个整数
float(x)       将x转换到一个浮点数
complex(real [,imag]) 创建一个复数
str(x)       将对象 x 转换为字符串
repr(x)      将对象 x 转换为表达式字符串
eval(str)    用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)     将序列 s 转换为一个元组
list(s)      将序列 s 转换为一个列表
set(s)       转换为可变集合
dict(d)      创建一个字典。d 必须是一个 (key, value)元组序列。
frozenset(s) 转换为不可变集合
chr(x)       将一个整数转换为一个字符
ord(x)       将一个字符转换为它的整数值
hex(x)       将一个整数转换为一个十六进制字符串 
oct(x)       将一个整数转换为一个八进制字符串""")