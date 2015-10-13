f=open("data.dat","w")
f.write("HELLO WORLD\n")
f.close()

f = open("data.dat","r")

s=f.read()
print s


import shelve

f = shelve.open("s.dat")

print f
print "\n"


f['one'] = "hello"
f['two'] = "goodbye"

print f
