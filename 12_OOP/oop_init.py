#!/usr/bin/env python3


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('My name is', self.name)

    def bye(self):
        print('Bye bye', self.name)


p = Person('Fabio')
p.say_hi()
p.bye()