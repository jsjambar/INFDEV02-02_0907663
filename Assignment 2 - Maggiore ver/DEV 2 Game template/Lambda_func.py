from Node import *
from Car import *

def fold(list, func, base):
    if(list.IsEmpty):
        return base
    else:
        return func(list.Head, fold(list.Tail, func, base))


def filter(list, p):
    if(list.IsEmpty):
        return Empty
    else:
        if p(list.Value):
            return Node(list.Value, filter(list.Tail, p))
        else:
            return filter(list.Tail, p)

def map(list, func):
    if(list.IsEmpty):
        return Empty
    else:
        return Node(func(list.Value), map(list.Tail, func))