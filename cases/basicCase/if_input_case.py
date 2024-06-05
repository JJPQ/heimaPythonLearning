import random

# 猜数字游戏
num = random.randint(1, 100)
guess_num = int(input("请猜数字\n"))
i = 1
while guess_num != num:
    if guess_num > num:
        guess_num = int(input("大了，请再猜一次\n"))
        i += 1
    else:
        guess_num = int(input("小了，请再猜一次\n"))
        i += 1
print("恭喜你! 猜中了! 一共猜了 %d 次" % i)