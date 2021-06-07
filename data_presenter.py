open_file = open("CupcakeInvoices.csv")

for line in open_file:
  line = line.strip()
  values = line.split(",")

  print(line) #problem 2

  print(values[2]) # problem 3

  print(values[4]) # problem 4

    total = float(values[3]) * float(values[4]) #problem 5

    result = total(values) + total(values)


print(round(total, 2))
open_file.close()

