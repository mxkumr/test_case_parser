# 1/5 Comments: This code contains variables in 3 languages
class தமிழ்_வகுப்பு:
    """A class with 10 Tamil variables"""
    def __init__(self):
        # 2/5 Comments: Tamil variables
        self.எண் = 10                  # Number
        self.பெயர் = "ரமணி"           # Name
        self.பட்டியல் = [1, 2, 3]     # List
        self.அகராதி = {"திறப்பு": "மதிப்பு"}  # Dictionary
        self.மெய்ப்புப்படுத்து = True  # Boolean
        self.எடை = 68.5               # Weight (float)
        self.உயரம் = 175               # Height
        self.முகவரி = ("தெரு", 25)     # Tuple
        self.வண்ணம் = "சிவப்பு"        # Color
        self.பட்டம் = None             # Degree

    def தமிழ்_செயல்பாடு(self):
        """Prints Tamil variables"""
        print(f"பெயர்: {self.பெயர்}, எண்: {self.எண்}")

class 中文类:
    """A class with 6 Chinese variables"""
    def __init__(self):
        # 3/5 Comments: Chinese variables
        self.数字 = 二十                # Number (20)
        self.名字 = "张三"             # Name
        self.列表 = ["苹果", "香蕉"]    # List with Chinese literals
        self.字典 = {"键": "值"}       # Dictionary
        self.价格 = 99.99             # Price
        self.有效 = True              # Valid

    def 中文方法(self, 参数):
        """Prints Chinese variables"""
        print(f"欢迎{self.名字}！参数: {参数}")

# 4/5 Comments: German variables
deutsche_variable1 = "Hallo"       # German variable 1
deutsche_variable2 = 3.1415926535  # German variable 2 (Pi)
deutsche_variable3 = ["a", "b"]    # German variable 3

def deutsche_funktion():
    """Prints German variables"""
    print(f"{deutsche_variable1} Welt! π ≈ {deutsche_variable2}")

# 5/5 Comments: Main execution
if __name__ == "__main__":
    t = தமிழ்_வகுப்பு()
    c = 中文类()
    
    t.தமிழ்_செயல்பாடு()
    c.中文方法("测试参数")  # Chinese literal argument
    deutsche_funktion()
    
    # Additional Chinese literals to reach 10
    额外字面量 = ["北京", "上海", "广州", "深圳", "重庆", 
              "天津", "武汉", "成都", "西安", "杭州"]