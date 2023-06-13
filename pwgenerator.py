import random as rdm

a = 'abcdefghijklmnopqrstuvwxyz'
a2 = 'ABCDEFGHIJKLMNOPQRTSUVWXYZ'
b = '0123456789'
b2 = '#*%&.?@$-+'

use = a+a2+b+b2

pw = "".join(rdm.sample(use,8))

print("Password Created: "+pw)

