#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 18-12-12
@Author  : leemiracle
"""
import sys
import os
from collections import defaultdict
sys.path.append("{}".format(os.path.sep).join(os.path.abspath(__file__).split(os.path.sep)[:-2]))
print(sys.path)

from src.config import ConfigAttribute, Config

def with_test():
    _count = 0

    _sentinel = object()

    class A(object):
        def __init__(self):
            self.v = set()

        def push(self):
            self.v.add(_count)
            print("push: {}".format(self.v))

        def __enter__(self):
            self.push()
            return self

        def pop(self, exc=_sentinel):
            print("pop: {}".format(exc))
            if exc is _sentinel:
                exc = sys.exc_info()[1]
                print("exc: {}".format(sys.exc_info()))
            self.v.pop()

        def __exit__(self, exc_type, exc_val, exc_tb):
            # self.pop(exc_val)
            self.pop()
    # with statement
    with A() as a:
        print("with....")
        pass
    print("a:{}".format(a.v))


def function_annotation():
    def sum_two_numbers(a: int, b: int) -> int:
        return a+b
    print(sum_two_numbers(1.1, 1.2))  # 编译器会提示


def instance_access_attribute():
    class B(object):
        a = ConfigAttribute("b")
        config = Config(".")
    b = B()
    # b.config.haha = "hehe"  # error set
    b.a = "hehe"  # 调用__set__ 方法
    print(b.a)  # 调用 __get__,  方法
    del b.a  # 调用 __delete__,  方法
    # __set_name__: 设置name


def main():
    class C(object):
        def __init__(self):
            self.v = dict()  # 没用
            pass

        def __getattribute__(self, item):
            print("__getattribute__:{}".format(item))
            # if item in super(C, self).__dict__:
            #     print("not in:{}".format(super(C, self).__dict__))
            #     super(C, self).__setattr__(item, 5)

            # self.__setattr__(item, 1)
            return super(C, self).__getattribute__(item)

        def __getattr__(self, item):  # 利用__getattribute__，__getattr__先后顺序，设置属性默认值
            print("__getattr__:{}".format(item))
            super(C, self).__setattr__(item, 0)
            return super(C, self).__getattribute__(item)  # 会从 self.__dict__ 中取值

        def __setattr__(self, attr, value):
            print("__setattr__:{}-->{}, {}".format(attr, type(attr), value))
            # self.v.update({attr: value})
            super(C, self).__setattr__(attr, value)
    c = C()
    # print(c.a)
    c.a = 10
    print(c.b)
    print(c.a)
    print(c.__dict__)

if __name__ == '__main__':
    main()
