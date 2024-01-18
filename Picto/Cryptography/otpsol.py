# hex_string = "51066c4808566c4851016c4854546c4808536c48530556026c4855051d036c4851556c485254506c4853566c485452786c4809516c4856066c"

# # Convert hexadecimal string to bytes
# byte_array = bytes.fromhex(hex_string)

# # Convert bytes to ASCII
# ascii_text = byte_array.decode('utf-8')

# print(ascii_text)

input_string = "[VKnA\9N8KU:N\Y{mJ\ZhMP=nK"

# Count total number of characters
total_characters = len(input_string)
print(total_characters)

# # # Count occurrences of '0'
# # count_zero = input_string.count('0')

# # # Print the results
# # print("Total number of characters:", total_characters)
# # print("Number of '0' characters:", count_zero)

print("0"*32)

# # # Given XOR equation: x XOR 51 = 54
# # result_xor = 54546d1d0d50681a5754684951076c1d0b5a681d530156036f4051571d0b694d5204681d570755654f0150384c05572b69190f59681c53066c5f433f18394c53
# # constant_value = 51066c4808566c4851016c4854546c4808536c48530556026c4855051d036c4851556c485254506c4853566c485452786c4809516c4856066c5e406b1e6c4801

# # # Find the value of x
# # x = result_xor ^ constant_value

# # # Print the result
# # print("The value of x is:", x)


# result_xor_hex = "54546d1d0d50681a5754684951076c1d0b5a681d530156036f4051571d0b694d5204681d570755654f0150384c05572b69190f59681c53066c5f433f18394c53"
# constant_value_hex = "51066c4808566c4851016c4854546c4808536c48530556026c4855051d036c4851556c485254506c4853566c485452786c4809516c4856066c5e406b1e6c4801"

# # Convert hexadecimal strings to byte arrays
# result_bytes = bytes.fromhex(result_xor_hex)
# constant_bytes = bytes.fromhex(constant_value_hex)

# # Perform XOR on each pair of bytes
# result_xor_bytes = bytes(a ^ b for a, b in zip(result_bytes, constant_bytes))

# # Convert the result back to a hexadecimal string
# result_xor_hex_result = result_xor_bytes.hex()

# # Print the result
# print("Result of XOR operation:")
# print(result_xor_hex_result)

# #result_xor_hex_result to ASCII
# byte_array = bytes.fromhex(result_xor_hex_result)
# ascii_text = byte_array.decode('utf-8')
# print(ascii_text)

