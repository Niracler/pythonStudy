# 汉诺塔的移动可以用递归函数非常简单地实现。
# 请编写move(n, a, b, c)函数，
# 它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，
# 例如：
def move(n, a, b, c):
    # 假如是一个的情况，直接a到c
    if n != 0:
        # 将上面n-1个放到b
        move(n - 1, a, c, b)
        # 将最下面一个放到c
        print(a, '-->', c)
        # 将上面n-1个放到c
        move(n - 1, b, a, c)


# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(10, 'A', 'B', 'C')