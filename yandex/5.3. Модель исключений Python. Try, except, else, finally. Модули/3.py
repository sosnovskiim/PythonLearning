# def func(a):
#     return str(a)
#
#
class Bug:
    def __repr__(self):
        raise BaseException

    def __str__(self):
        raise BaseException


func(Bug())
