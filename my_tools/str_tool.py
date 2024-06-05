def str_reverse(s):
    s = s[::-1]
    print(s)

def substr(s, x, y):
    """
    对字符串 s 进行切片
    :param s:
    :param x:切片起点
    :param y:切片终点
    :return:
    """
    s = s[x:y]
    print(s)


if __name__ == '__main__':
    print(str_reverse("wjjnb"))
    print(substr("wjjnb", 1, 3))
