def natural_int_validation(_func):
    def _inner(_number):
        if not isinstance(_number, int) or _number <= 0:
            raise ValueError("Wrong parameter, must be natural integer value")
        return _func(_number)
    _inner.__doc__ = _func.__doc__
    return _inner
