from functools import reduce
import operator

def every(pred, seq):
    return reduce(operator.and_, map(pred, seq))
def any(pred, seq):
    return reduce(operator.or_, map(pred, seq))

