# Reverse Engineering
flag = "picoCTF"
encode = ''.join(
    [
        chr((ord(flag[i]) << 8) + ord(flag[i + 1])) 
                     for i in range(0, len(flag)-1, 2)
    ])

print(encode)

# The flag is never specified in the Python string given in the problem.
# I decided to take note of the hint and “wing it” a bit to see if I can extract a solution. 
# Before doing so, it is worth discussing what some of these functions do.

# chr is a function that takes the integer representation of a character and returns
# its string representation (Python 3.11.2 documentation n.d.) and ord takes in a string
# representation of a character and returns its integer value (Ibid). chr is the inverse 
# of ord and ord is the inverse of chr(Ibid).

flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"

characters = [char for char in flag]

# for i in characters:
#     print(ord(i))

print("characters:", characters)
# characters = ["灩", "捯", "䍔", "䙻", "ㄶ", "形", "楴", "獟", "楮", "獴", "㌴", "摟", "潦", "弸", "弲", "㘶", "㠴", "挲", "ぽ"]


sum_array = [ord(char) for char in characters]

print("sum_array:", sum_array)
# sum_array: [28777, 25455, 17236, 18043, 12598, 24418, 26996, 29535, 26990, 29556, 13108, 25695, 28518, 24376, 24370, 13878, 14388, 25394, 12413]



def decode_sum(sum_array):
    decoded = ''
    for s in sum_array:
        for i in range(0, 127):
            if 0 <= (s - (i << 8)) <= 126:
                decoded += chr(i) + chr(s - (i << 8))
                break
    return decoded

# Example usage:

decoded_result = decode_sum(sum_array)
print("Decoded:", decoded_result)


