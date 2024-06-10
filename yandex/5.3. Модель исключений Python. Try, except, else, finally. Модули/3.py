# def func(a):
#     return str(a)
#
#
class Bug:
    def __repr__(self):
        raise Exception

    def __str__(self):
        raise Exception


func(Bug())
