# -*- coding: utf-8 -*-
"""
__slots__ 

クラスの属性情報を保存している __dict__ を生成しないことでメモリを節約する

* http://docs.python.jp/3/reference/datamodel.html#slots
"""
import memory_profiler


class A(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


if __name__ == "__main__":
    instance_num = 10000
    initial = memory_profiler.memory_usage()[0]
    print "RAM at start {:0.1f}MiB".format(initial)

    data_non_slots = [A(1, 2, 3) for _ in range(instance_num)]
    after_create_non_slots = memory_profiler.memory_usage()[0]

    increase_mem = after_create_non_slots - initial
    print "RAM after creating instance without __slots__ {:0.1f}MiB, "\
          "increased {:0.1f}MiB".format(after_create_non_slots, increase_mem)
