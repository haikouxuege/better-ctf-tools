#_*_ coding:UTF-8 _*_
num =0
def fac(num):
  for i in range(2,num):
    if num % i == 0 : 
      print(i),
      fac(num//i)
      return
  print(num)
  return 

fac(num)

