#!/usr/bin/env python

from timeit import Timer

setup = """
from random import randrange
from operator import attrgetter
class Foo:
    def __init__(self, prioridade):
        self.prioridade = prioridade
N = %d
bar_list = [Foo(randrange(N)) for i in xrange(N)]
"""

cmd1 = """bar_list.sort(key=attrgetter('prioridade'))"""
cmd2 = """bar_list.sort(key=lambda x: x.prioridade)"""

N = 10**6

for cmd in (cmd1, cmd2):
    print cmd
    print Timer(cmd, setup%N).timeit(10)

