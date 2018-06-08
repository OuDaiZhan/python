# __all__ = ['c_to_f', 'f_to_c']

import math
# import sting
import random

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


def squ(x):
    """return squteror of given number"""
    return x ** 2


def good_one():
    str1 = 'you are good'
    return str1


def outer_one():
    outer_var = 'outer variable'

    def inner():
        return outer_var
    return inner()


def f(x):
    return x ** 2


def power1(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = x * n
        return s


def enroll1(name, gender):
    print('name:', name)
    print('gender:', gender)


def enrool11(name, gender, age=0, city=''):
    return {'name':name,
    'gender':gender,
    'age:': age,
    'city':city}


# def ran_capta():
#     capta = ''
#     words = ''.join((string.ascii_letters, string.digits))
#     for i in range(6):
#         capta += random.choice(words)
#     print(capta)


class A:
    def funX(self):
        print('funy()')

    def funY(self):
        print('funY()')

if __name__ == '__main__':
    a = A()
    a.funX()
    a.funY()


def compareNum(num1, num2):
    if num1 < num2:
        return str(num1) + "<" + str(num2)
    elif num1 > num2:
        return str(num1) + ">" + str(num2)
    elif num1 == num2:
        return str(num1) + '=' + str(num2)
    else:
        return ''


def pow_in(num):
    """
    input a number and return num **　２

    """
    num = int(num)
    return num ** 2


def min_in(somenumber):
   return min(list(somenumber))


class Student(object):
    count = 0
    books = []

    def __init__(self, name, age):    #  初始化函数
        self.name = name
        self.age = age
    pass


Student.books.append(['python', 'javascript'])
print('Student book list:{}'.format(Student.books))

Student.hobbies = ['reading', 'jobbing', 'swimming']
print('student hobby list:{}'.format(Student.hobbies))
print(dir(Student))

Student.name = ['oufaizhan', 'oudaizhan', 'weiyahui']
print(Student.name)
print(Student.count)
print(Student.books)

wilber = Student('Wilber', 28)
wilber.english_score = 60
wilber.chinese_score = 100
print(wilber.english_score)
print(wilber.chinese_score)
print('{} is {} years old'.format(wilber.name, wilber.age))

wilber.gender = 'male'
print("{} is {}".format(wilber.name, wilber.gender))

will = Student('Will', 27)
print('{} is {} years old'.format(will.name, will.age))
print(dir(will))
print(will.books)

print(Student.__name__)
print(Student.__doc__)


class Student():
    'this is a Student class'
    count = 0
    books = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
    pass

print(Student.__name__)
print(Student.__doc__)
print(Student.__bases__)
print(Student.__dict__)
print(Student.__class__)


def my_abs(x):
    """

    :param x:
    :return:
    """
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


def my_abs(x):
    if not isinstance(x, (int, float)):    # 数据类型判断
        raise TypeError('Bad operand type')   # 返回错误类型
    if x >= 0:
        return x
    else:
        return -x


def my_info(name, age):
    if not isinstance(name, str):
        raise TypeError('Bad type please input string')

    if not isinstance(age, int):
        raise TypeError('Type Eroll, input int')

    return 'your name is {} and your age is {}'.format(name, age)


def add_end(l=[]):
    l.append('end')
    return l


def add_end2(l=None):
    if l in None:
        l = []
    l.append('end')
    return l


def calc(*number):    # *接收多个参数  可接收0个或者任意参数
    """
    返回a**2, b**2,c**2.....的和
    """
    sum = 0
    for n in number:
        sum += n ** n
    return sum


# 关键字参数
def person(name, age, *args, **kwargs):
    print('name:', name, 'age:', age, args, kwargs)


#
# def average(num1, num2, **arge):
#     return eval((num1 + num2 + arge) / )


# 计算N天以后是星期几
def n_day_is_week(theday, days):
    result = (int(theday) + int(days)) % 7
    return r'日一二三四五六'[result]


def computeLoan(annual_rate, principal, year):
    """

    :param annual_rate: 年利率
    :param principal: 贷款总额
    :param year:贷款年数
    ：month_interest: 月利率
    ：month_payment: 月供
    :月付利息 = 本金 * 月利率
    ：月付= 本金* 月利率/(1+月利率）**（总还款月-1）
    ：每月还款额 = 月付利息 + 月付
    ：全部利息 = 总还款月数 * 每月还款额 - 本金
    :return:
    """

    total_month = int(year) * 12
    month_interest = float(annual_rate) / 12
    # 月供本金
    month_payment = float(principal) * month_interest + float(principal) * month_interest/((1 + month_interest) ** (total_month - 1))
    # 月利息
    month_rate = float(principal) * month_interest
    # 月供
    total_month_pay = month_payment + month_rate
    # 全部利息
    total_rate = (int(year) * 12) * total_month_pay - float(principal)

    return '月付利息：{:.2f}\n月付本金：{:.2f}\n每月还款额：{:.2f}\n总利息：{:.2f}'.format(month_rate, month_payment, total_month_pay, total_rate)


def compute_distance(x1, y1, x2, y2):

    distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.25
    return distance


def c_to_f(num, str1):
    if str1 in ('f', 'F'):
        c = (num-32) / 1.8
    return c


def f_to_c(num, str1):
    if str1 in ('c', 'C'):
        f = num * 1.8 + 32
    return f


def cylinder_vol(radius, lenght):
    import math
    volume = radius ** 2 * math.pi * lenght
    return volume


def feet_to_miter(feet):
    miter = float(feet) * 0.305
    return miter


def miter_to_feet(miter):
    feet = float(miter) / 0.305
    return feet


def pon_to_kg(pon):
    return float(pon) * 0.454


def tips(rate, payment):
    tip = rate * payment
    total = tip + payment
    return 'tips：', tip, '共消费：', total


def total_sum(num):
    '返回一个整数中的各个数位求和'
    c = [int(i) for i in num]
    return sum(c)


def year_and_day(minutes):
    '根据输入的分钟数 返回天数和年数'
    m = minutes % 60
    # 剩下多少分钟
    h = (minutes // 60) % 24
    d = (minutes // 60) // 24
    y = d // 365
    return d, h, m, y


def air_length(a, v):
    '根据给出的加速度a，和起飞速度v ，求出飞机起飞所需要的最短跑道长度'
    length = (v ** 2) / (a * 2)
    return length


def message():
    info = """For most , a movie to the city usually
                mean better jobs and greater opportunities.
            """
    print(info)


def total(num1, num2, num3):
    result = 0
    for items in range(num1, num2 + 1, num3):
        result += items
    return result


import math

vol = (4/3)*math.pi * 5 ** 3
print(vol)


def do_twice(f):
    print(f)
    print(f)


print(do_twice('ou'))


def table():
    print('+----+----+')
    print('|    |    |')
    print('|    |    |')
    print('|    |    |')
    print('|    |    |')
    print('+----+----+')
    print('|    |    |')
    print('|    |    |')
    print('|    |    |')
    print('|    |    |')
    print('+----+----+')


# print("int('23.5'\t)", int(23.9) )
# print("int(23.001):\n", int(23.001))
# print("int('23'):\t", int('23'))
# print("float(3):\t", float(3))
# print("float('3'):\t", float('3'))
# print("float(3.2):\t", float('3.2'))
# print("str(23):\t", str(23))
# print("str(23.3):\t", str(23.3))
# print("int(23.3):\t", int('23.1'))
#
# aint = input('Please input a int:')
# print(aint)
# print(int(float(aint)))
# print(float(aint))


def encode(s):
    """将字符串转换为二进制"""
    return ' '.join([bin(ord(c)).replace('ob', '') for c in s])


def decode(s):
    """将二进制转换为字符串"""
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


def personal_income_tax(income):
    ys = income - 3500
    if income <= 3500:
        return '你不用交税'
    elif ys <= 1500:
        return ys * 0.03
    elif (ys >= 1500) or (ys < 4500):
        return ys * 0.1 - 105
    elif (ys >= 4500) or (ys < 9000):
        return ys * 0.2 - 555
    elif (ys >= 9000) or (ys < 35000):
        return ys * 0.25 - 1005
    elif (ys >= 35000) or (ys < 55000):
        return ys * 0.3 - 2755
    elif (ys >= 55000) or (ys < 80000):
        return ys * 0.35 - 5505
    elif ys >= 80000:
        return ys * 0.45 - 13505


def greet_user(username):
    """

    :param username: 输入用户姓名
    :return: 向用户打招呼
    """
    print("Hello!", username.title(), '.')


square = []
for i in range(11):
    square.append(i ** 2)
print(square)


def f(x):
    return x ** 2


r = map(f, list(range(11)))

l = []
for n in list(range(10)):
    l.append(f(n))
print(l)


from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, list(range(11))))


try:
    fh = open('testfile', 'w')
    fh.write('这是一个测试文件， 用于测试异常')
except IOError:
    print('Error:没有找到文件或读取文件失败！')
else:
    print('内容写入成功')

s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print(e)
    print('错误')