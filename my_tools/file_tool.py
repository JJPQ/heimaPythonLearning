def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="utf-8")
        print(f.read())
    except:
        print("文件不存在")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="utf-8")
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    print_file_info("D:/word.txt")
    append_to_file("D:/word.txt", "hahaha")
