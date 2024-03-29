# coding=utf-8
print("Hello, World!")

#Numbers
sayac = 100          # An integer assignment
kilometre = 1000.0       # A floating point

print(sayac)
print kilometre

#Bool
x = True
y = not x
print
print x
print y

print(10 > 9)       #True
print(10 == 9)      #False
print(10 < 9)       #False

#Strings
str = 'Hello World!'
print
print(len(str))
print str          # String yazdırır
print str[0]       # String ilk elemanını yazdırır
print str[2:5]     # 3. karakterden 5. karaktere kadar olan elemanları yazdırır
print str[2:]      # 3. karakterden itibaren tum elemanlari yazdirir.
print str * 2      # Stringi iki defa basar
print str + "TEST" # Stringi yeni ifade ile birleştirir.
print(str.split(",")) # returns ['Hello', ' World!']
print

m = "awesome"
print("Python " + m)

txt = "T3 IOT Egitimi Gungoren"
x = "ungor" in txt
print(x)

#Lists
list = [ 'Ece', 786 , 2.23, 'Can', 70.2 ]
tinylist = [123, 'Can']
print
print list          # Tüm listeyi yazdırır.
print list[0]       # Listenin ilk elemanını yazdırır.
print list[1:4]     # 2. elemandan 4. elemana kadar listeyi yazdırır.
print list[2:]      # Listenin 3. elemanından itibaren yazdırır.
print tinylist * 2  # Listeyi iki defa yazdırır.
print list + tinylist # İki listeyi birleştirir.


#tuple[2] = 1000    # Invalid syntax with tuple
#list[2] = 1000     # Valid syntax with list

#Dictionaries (Key - Value Types)
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

"""
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print
print dict
print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values
"""

#Casting

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print
print type(kilometre)
