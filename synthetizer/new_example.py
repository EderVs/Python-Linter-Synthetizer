_size_ = len(_A_)
if _size_ == 0:
    return

while _size_ > 1:
    if _A_[0] == 0:
        _A_.pop(0)
    else: break


_size_ = len(_A_)
_end_ = _size_ - 1
_overflow_ = True
while _end_ >= 0:
    _new_val_ = _A_[_end_]
    if _overflow_:
        _new_val_ += 1
        _overflow_ = False
    if _new_val_ <= 9:
        _A_[_end_] = _new_val_
        break
    else:
        _A_[_end_] = _new_val_ % 10
        _overflow_ = True
    _end_ -= 1
if _overflow_:
    _A_.insert(0, 1)
print(_A_)
