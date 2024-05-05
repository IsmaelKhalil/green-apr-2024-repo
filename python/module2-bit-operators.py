first_bit = 1
second_bit = 0

print(first_bit & second_bit)
#both need to equal 1, otherwise it will be 0'


print(first_bit | second_bit)
#either of them needs to equal 1


print(first_bit ^ second_bit)
#both of them must be exclusive/unique, if both are 0 or 1, then it will be 0

print(~1)
print(~0)
#~x = -x - 1

print(12 << 1)
# right shift, times 2^1

print(12 << 2)
# right shift, times 2^2

print(12 << 0)

print(12 >> 1)
# left shift, divided by 2^1

print(12 >> 2)
# left shift, divided by 2^2