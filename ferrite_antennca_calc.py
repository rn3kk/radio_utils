"""
см книгу В.И. Хомич Приемные ферритовые антенны
стр. 37
"""

dser = 8.0 #диам сердечника
dl = 10.0 #диам катушки

Fmaks = 0.15 # в МГц
Cmin = 1000 # pF
Lk = (2.53*(10**4))/(Fmaks**2 * Cmin)

ml = 0.7
pl = 0.8
ql = dser**2 / dl**2
md =


print('Lk', Lk)
