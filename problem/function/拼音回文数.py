# 只要文字的拼音构成前后回文
# 用xpinyin模块实现汉字转换成对应的拼音
# 将各个功能封装成函数
from xpinyin import Pinyin

# 功能：读取输入并判断字数
# 输出：符合大于一的奇数个字的字符串 不必奇数
def str_in():
    str_word = input("请输入一段话：(输入exit退出)")
    while len(str_word) <= 1: # 简化代码
        str_word = input("字数太少, 请重新输入: ")

    return str_word

# 功能：汉字转换成拼音
# 输出：字符串首字母构成的序列
def py_transf(str_words):
    P = Pinyin()
    pinyin_list = list(P.get_initials(str_words, '')) # 提取首字母

    return pinyin_list

# 功能：判断回文数
# 输出：True/False
def hui(_list):
    r_list = list(reversed(_list))
    if r_list == _list:
        return True
    else:
        return False
    

# 主程序
str_word = str_in()
while str_word != 'exit':
    py = py_transf(str_word)
    if hui(py):
        print(f"[{str_word}]是回文。")
    else:
        print(f"[{str_word}]不是回文。")
    print()

    str_word = str_in()

print("退出成功~")
