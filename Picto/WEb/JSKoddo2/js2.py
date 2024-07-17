# Sample bytes and key
bytes_list = [i for i in range(32)]  # Example byte array for visualization
key = "11111111111111111111111111111111"
LEN = 16

# Function to visualize the processing of bytes
def visualize_processing(bytes_list, key):
    result = [0] * len(bytes_list)
    print("Initial Bytes List:", bytes_list)
    print("Key:", key)
    print("LEN:", LEN)
    print()

    for i in range(LEN):
        shifter = int(key[i * 2])
        print(f"i={i}, shifter={shifter}")
        for j in range(len(bytes_list) // LEN):
            old_index = ((j + shifter) * LEN) % len(bytes_list) + i
            new_index = (j * LEN) + i
            result[new_index] = bytes_list[old_index]
            print(f"  j={j}, old_index={old_index}, new_index={new_index}, value={bytes_list[old_index]}")
        print(f"Result after processing column {i}:", result)
        print()
    
    # Remove trailing zeros
    while result[-1] == 0:
        result.pop()
    
    print("Final Result:", result)
    return result

# Visualize the processing
final_result = visualize_processing(bytes_list, key)
