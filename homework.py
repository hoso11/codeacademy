###  1. Գրել ծրագիր որը վերադարձնում ա String-ի երկարությունը
a = "barev"
print(len(a))

### 2. Գրել ծրագիր, որը վերցնում ա 4 integer, ու իրանց միացնում ստանալով տարևթիվ (էլի integer տիպի)
b = "1"
c = "2"
d = "3"
e = "4"
print(b+c+d+e)

###  3. Գրել ծրագիր, որը նախադասության մեջ բոլոր իրար հաջորդող 2 հատ "0"-ն կփոխարինի 1 հատ 0-ով։

import re

f = "In year 1800, the population of Africa reached to 107,006,500"
x = re.sub("00", "0", f)
print(x)

###4. Գրել ծրագիր, որը տրված String-ը կսարքի ամբողջությամբ մեծատառ, բացի "a" տառից։
g = "I'm gonna make him an offer he can't refuse"
h = g.upper()
y = re.sub("A", "a", h)
print(y)
###5. Գրել ծրագիր, որը floating տիպի թվերի մեջ կետը կփոխարինի 0-ով, ու կվերադարձնի որպես integer
i = "16.58"
print(i.replace(".","0",1))
