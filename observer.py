# _*_ coding=utf-8 _*_


"""
内容：定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时, 
    所有依赖于它的对象都得到通知并被自动更新。观察者模式又称“发布-订阅”模式
角色：
    抽象主题（Subject）
    具体主题（ConcreteSubject）——发布者
    抽象观察者（Observer）
    具体观察者（ConcreteObserver）——订阅者

适用场景：
    当一个抽象模型有两方面，其中一个方面依赖于另一个方面。将这两者封装在独立对象中以使它们可以各自独立地改变和复用。
    当对一个对象的改变需要同时改变其它对象，而不知道具体有多少对象有待改变。
    当一个对象必须通知其它对象，而它又不能假定其它对象是谁。换言之，你不希望这些对象是紧密耦合的。
优点：
    目标和观察者之间的抽象耦合最小
    支持广播通信

"""
from abc import ABCMeta, abstractmethod


class Publisher:
    """抽象发布者"""

    def __init__(self):
        self.subscribers = []

    def attach(self, sub):
        self.subscribers.append(sub)

    def detach(self, sub):
        self.subscribers.remove(sub)

    def notify(self):
        for sub in self.subscribers:
            sub.update(self)


class Subscriber(metaclass=ABCMeta):
    """抽象订阅者"""

    @abstractmethod
    def update(self, notice):
        pass


class StaffNotify(Publisher):
    """具体发布者"""

    def __init__(self, info=None):
        super().__init__()
        self.__info = info

    @property
    def company_info(self):
        return self.__info

    @company_info.setter
    def company_info(self, info):
        self.__info = info
        self.notify()  # 推送


class Staff(Subscriber):
    """具体订阅者"""

    def __init__(self):
        self.info = None

    def update(self, notice):
        self.info = notice.company_info


# 高层代码
publish = StaffNotify('公司信息')
s1 = Staff()
s2 = Staff()
# 添加绑定
publish.attach(s1)
publish.attach(s2)
# 推送信息
publish.company_info = "明天放假"
print(s1.info)
print(s2.info)
# 解除绑定
publish.detach(s2)
publish.company_info = "国庆放假十天"
print(s1.info)
print(s2.info)

