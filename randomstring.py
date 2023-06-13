import random as rdm

a2 = 'ABCDEFGHIJKLMNOPQRTSUVWXYZ'
b = '0123456789'

use = a2+b

pw = "".join(rdm.sample(use,8))
print(pw)
