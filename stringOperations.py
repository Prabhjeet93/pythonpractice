import re

txt = "snow in canada today"
txt1 = "snow in canada today"
x = re.search('a',txt)
print(x)

print("The first character is located in the position : ",x.start())
y = x.start()
print(y)

print("Replace all white-space characters with digit 9")
x = re.sub("\s","", txt)
print(x)
p = re.sub("a","1", txt1)
print(p)

print("Return a list containing every occurrance  of /")
txt = "/snow in /canada /today"
print(txt)
x = re.findall('/',txt)
print(x)
print(x[2])
txt = re.sub('today','yesterday',txt)
print(txt)

##split
txt = "snow in canada today"
t = re.split('c',txt)
print(t)
q = re.split('|',txt) ## character wise split just put pipe
print(q)
w = re.split('\s',txt)
print(w)
x[1] = re.sub('anada today','canadatoday',x[1])
print(x[1])


txt = 'It is snow in Canada'  ## find the index of a char or substring
y = txt.index('C')
print(y)
print(txt[0:y-1])
print(txt[y:len(txt)])

w[1] = w[1] + ' test'  ## string concatnation
print(w[1])

try:
    x = 3 + 'test'
except:
    print('Can not add integer to a string')
else:
  print("Nothing went wrong")  ## if it goes into except then else will be skipped otherwise it will run else part
finally:
    print('try except block completed') # always runs
