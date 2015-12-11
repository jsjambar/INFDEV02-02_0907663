from Node import *
def fold(list, func, base):
    if(list.IsEmpty):
        return base
    else:
        return func(list.Head, fold(list.Tail, func, base))


def filter(list, p):
    if(list.IsEmpty):
        return Empty
    else:
        if p(list.Head):
            return Node(list.Head, list.Tail)
        else:
            return filter(list.Tail, p)

def map(list, func):
    if(list.IsEmpty):
        return Empty
    else:
        return Node(func(list.Head), map(list.Tail, func))