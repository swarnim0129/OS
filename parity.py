def generate_parity_bit(data):
    ones = data.count('1')
    return '0' if ones % 2 == 0 else '1'

def parity_check():
    sent = input("Enter sent data (binary): ")
    parity = generate_parity_bit(sent)
    print("Parity Bit:", parity)

    received = input("Enter received data (binary): ")
    if generate_parity_bit(sent) != generate_parity_bit(received):
        print("Error Detected!")
    else:
        print("No Error Detected.")
