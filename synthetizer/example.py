size = len(A)
if size == 0:
    return

while size > 1:
    if A[0] == 0:
        A.pop(0)
    else: break


size = len(A)
end = size - 1
overflow = True
while end >= 0:
    new_val = A[end]
    if overflow:
        new_val += 1
        overflow = False
    if new_val <= 9:
        A[end] = new_val
        break
    else:
        A[end] = new_val % 10
        overflow = True
    end -= 1
if overflow:
    A.insert(0, 1)
print(A)