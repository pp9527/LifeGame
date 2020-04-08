import sys


def check_int(date):
    # 输入的地图长宽的合法性检测, int
    try:
        int(date)
    except ValueError:
        print("你输入的不是数字！")
        sys.exit(0)
    date = int(date)
    if date < 1:
        print("请输入大于一的数：")
        sys.exit(0)
    else:
        return date
