#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.buffer = list()

    def add(self, *a):
        # добавить следующую часть последовательности
        for i in a:
            self.buffer.append(i)
            if len(self.buffer) >= 5:
                tmp = list()
                for bi in range(5):
                    tmp.append(self.buffer.pop(0))
                print(str(sum(tmp)))

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке,
        # в котором они были добавлены
        return self.buffer
