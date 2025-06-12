# 定义变量和函数 (Defining variables and functions)
数字 = 10
名称 = "张三"
列表 = [1, 2, 3]
字典 = {"键": "值"}

def 打印信息(参数):
    print(参数)

class 学生:
    def __init__(self, 名字):
        self.名字 = 名字
    
    def 显示名字(self):
        print(self.名字)

# 使用标识符 (Using identifiers)
if 数字 > 5:
    打印信息(名称)

学生实例 = 学生("李四")
学生实例.显示名字()