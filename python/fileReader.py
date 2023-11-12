file = input("File name: ")
f = open(file)
lines = f.readlines()
res = []
for sub in lines:
	  res.append(sub.replace("\n", ""))
print(res) # Contents of file
