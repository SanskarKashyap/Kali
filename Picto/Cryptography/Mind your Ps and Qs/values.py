# Mind your Ps and Qs

# Description

# In RSA, a small e value can be problematic, but what about N? Can you decrypt this? values



from Crypto.Util.number import inverse

c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537


# http://factordb.com/ to get p and q 
p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221

# veryfing n = p*q
if (n== p*q):
    print("n = p*q","\n")

phi = ((p-1)*(q-1))

# def egcd (a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd (b % a, a)
#         return (g, x - (b // a) * y, y)


# def modinv (a, m):
#     g, x, y = egcd (a, m)
#     if g != 1:
#         raise Exception ('modular inverse does not exist')
#     else:
#         return x % m

# d = modinv(e, phi)


d = inverse(e, phi)

print("n = ", n, "\n")
print("e = ", e, "\n")

print("d = ", d, "\n")

Message = pow(c,d,n)

print("Message = ", Message, "\n")

print("Hex_Message = ", hex(Message), "\n")
print("Hex_Message = ", hex(Message)[2:], "\n")

print("Flag = ", bytearray.fromhex(hex(Message)[2:]).decode(), "\n")


# Flag =  picoCTF{sma11_N_n0_g0od_23540368} 

# REf: 

#  https://www.youtube.com/watch?v=Pq8gNbvfaoM
#  https://www.youtube.com/watch?v=_lg2AEqRTjg&list=PLL4unRYxBwriwYN0LTHzk2c2cxfYTiaY9

