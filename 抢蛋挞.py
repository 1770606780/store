'''
    1、蛋挞篮子最多500个，一个两块
    2、3个厨师做蛋挞，当篮子满了，停三秒，继续是否已满
    3、6个用户每人3000，同时抢，抢到3000用完为止，篮子没了等三秒等厨师继续做
'''

from threading import Thread
import time

lanz = 0


class Cs(Thread):
    csname = ""

    def run(self) -> None:
        global lanz
        global money
        while True :
            if lanz < 500:
                lanz = lanz + 1
                print(self.csname,"正在制作蛋挞，有",lanz,"个")
                time.sleep(0.1)
            else:
                print("请稍后蛋挞正在制作中")
                time.sleep(3)
                break

class Yh(Thread):

    username = ""
    eggtar = 0
    money = ""

    def run(self) -> None:
        global lanz
        global money
        while True:
            if self.money > 0 :
                self.money = self.money - 2
                self.eggtar = self.eggtar + 1
                print(self.username,"已抢到蛋挞",self.eggtar,"还剩",lanz,"个蛋挞,还剩",self.money,"元钱")
                time.sleep(1)
            else:
                print("请稍等三秒")
                time.sleep(3)
                print(self.username, "总共抢了", self.eggtar, "个蛋挞，还剩",self.money,"元钱")
                break

p1 = Yh()
p2 = Yh()
p3 = Yh()
p4 = Yh()
p5 = Yh()
p6 = Yh()

p7 = Cs()
p8 = Cs()
p9 = Cs()

p1.username = "刘浩"
p2.username = "孙老头"
p3.username = "胖子"
p4.username = "非凡"
p5.username = "猴子"
p6.username = "后豆子"

p1.money = 3000
p2.money = 3000
p3.money = 3000
p4.money = 3000
p5.money = 3000
p6.money = 3000


p7.csname = "孙老头"
p8.csname = "孙二头"
p9.csname = "孙猴豆子"

p7.start()
p8.start()
p9.start()

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()






































