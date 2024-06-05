## 乘法口诀表
i = 1
print("这是while循环的9×9乘法口诀表")
while i <= 9:
    j = 1
    while j <= i:
        # end=' '  用空格改变了原本换行的结尾
        print(f"{j}*{i}={j * i}", end=', ')
        j += 1
    print()
    i += 1

print("\n这是for循环的9×9乘法口诀表")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}\t", end='')
    print()