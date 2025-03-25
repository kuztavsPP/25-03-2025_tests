import random
s = [random.randint(-20,20) for _ in range(20)]
slen = len(s)
vid = sum(s)/len(s)

poz = len([i for i in s if i > 0])
neg = len([i for i in s if i < 0])

pozneg = (f" pozitīvo: {poz}", f" negatīvo: {neg}")
if poz > neg: pozneg = pozneg + (True,)
else: pozneg = pozneg + (False,)

div = len([i for i in s if len(str(abs(i))) == 2])
vien = len([i for i in s if len(str(abs(i))) == 1])

cip = (f" divciparu: {div}", f" vienciparu: {vien}")
if div > vien: cip = cip + (True,)
else: cip = cip + (False,)

vvid = len([i for i in s if i > vid])
zvid = len([i for i in s if i < vid])

vidi = (f" virs vidējā: {vvid}", f" zem vidējā: {zvid}")
if vvid > zvid: vidi = vidi + (True,)
else: vidi = vidi + (False,)

dalas_3 = max([i for i in s if i%3 == 0 and i != 0]) if not ValueError else 0
dalas_13 = min([i for i in s if i%13 == 0 and i != 0]) if not ValueError else 0

dalas = (f" ar 3: {dalas_3}", f" ar 13: {dalas_13}")
if dalas_3 > dalas_13: dalas = dalas + (True,)
else: dalas = dalas + (False,)
mazaki = len([i for i in s if i < s[-1]])
lielaki = len([i for i in s if i > s[-1]])

kuri = (f"mazāki par pēdējo: {mazaki}", f" lielāki par pēdējo: {lielaki}")
if mazaki > lielaki: kuri = kuri + (True,)
else:
    kuri = kuri + (False,)

print(s)
print(f"""Sarakstā ir vairāk{pozneg[0 if pozneg[2] is True else 1]}
Sarakstā ir vairāk{cip[0 if cip[2] is True else 1]}
Sarakstā ir vairāk{vidi[0 if vidi[2] is True else 1]}
Sarakstā lielākais, kas dalās{dalas[0 if dalas[2] is True else 1]}
Sarakstā vairāk ir {kuri[0 if kuri[2] is True else 1]}
""")
