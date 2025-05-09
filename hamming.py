def hamming_check():
    code = input("Enter received Hamming Code: ")
    code = list(code)
    n = len(code)
    error_position = 0

    i = 0
    while 2 ** i < n + 1:
        pos = 2 ** i
        count = 0
        for j in range(pos - 1, n, 2 * pos):
            for k in range(j, min(j + pos, n)):
                if code[k] == '1':
                    count += 1
        if count % 2 != 0:
            error_position += pos
        i += 1

    if error_position != 0:
        print("Error at position:", error_position)
        code[error_position - 1] = '0' if code[error_position - 1] == '1' else '1'
        print("Corrected Code:", ''.join(code))
    else:
        print("No Error Detected.")

if __name__ == "__main__":
    hamming_check()




