num1 = 0
num2 = 1

file = open("fibonacci2.txt", "w")

for i in range(2,514):
  product = (num1 + num2)
  file.write("{} {}\n".format(i,product))
  num1 = num2
  num2 = product

for i in range(514,1002):
  product = (num1 + num2)
  file.write("{}\n{}\n".format(i,product))
  num1 = num2
  num2 = product

file.close()