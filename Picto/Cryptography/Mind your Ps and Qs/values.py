# Mind your Ps and Qs

# Description

# In RSA, a small e value can be problematic, but what about N? Can you decrypt this? values



from Crypto.Util.number import inverse

c = 1653846567991237785165804830220570359831737422913653900771321182275434291594575820905308731552976037450800964970129746815752140809661627229628696762658709565017262748436725042640599197370336286662125629509074800238474946278625972950218750942747603293092674755755724861141223960584280198851409400183944430983866642782659239657789937724188385697
n = 16444678980678805860838202016830677237749384276518326997349441922993025641377585236834312621681704194679658925453500767865403910550308788500477796432747424753313024713247162405745304298763556243431210177010159509312044826554704858597676144947214752060885536813285307494577957338052496492114121444208152426904516475146965698477568129167480238859
e = 65537


# http://factordb.com/ to get p and q 
# multi-prime RSA --> https://www.alpertron.com.ar/ECM.HTM   https://ctf.samsongama.com/ctf/crypto/picoctf19-b00tl3gRSA3.html
p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221

# veryfing n = p*q
if (n== p*q):
    print("n = p*q","\n")

# phi = ((p-1)*(q-1))
# remove space between phi in python
input_totient = "16 444678 934705 600342 548944 457924 953326 877051 566602 353900 411480 602276 782153 350873 529155 667739 224202 014227 235418 190493 504301 536576 733682 047948 630796 079444 389931 889187 417409 967413 828532 267402 678551 825729 074734 227571 441705 750343 429091 567276 765466 788145 721030 252100 682890 090586 238204 695252 088790 845361 647758 981089 970091 426155 813928 960000 000000 000000"
# Remove spaces from the string
output_totient = input_totient.replace(" ", "")

# Convert the resulting string to a number
output_totient = int(output_totient)

# Print the result
print(output_totient)


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


# d = inverse(e, phi)
d = inverse(e, output_totient)

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
