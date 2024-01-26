file = open("python_aprentice\sample.txt")
print(file)
print(file.read())
file.seek(0)

print(file.read(5))
print(file.tell())
file.seek(0)

file.close()
print(file.closed)

######################################

with open("python_aprentice\sample.txt") as f:
    line = f.readline()

    while line:
        print(line)
        line = f.readline()

######################################

with open('python_aprentice\sample.txt', 'w') as f:
    f.write('Let\'s check the file write op')
    print(f.tell())
    f.truncate(10)

with open('python_aprentice\sample.txt', 'r') as f: 
    print(f.read())

######################################
