def crc(data,divisor):
    padded_data=data+'0'*(len(divisor)-1)
    data_bits=list(padded_data)

    for i in range (len(data)):
        if data_bits[i]=='1':
            for j in range(len(divisor)):
                data_bits[i+j]=str(int(data_bits[i+j])^int(divisor[j]))
    
    return "".join(data_bits[-(len(divisor)-1):])

data =input("Enter the data which is sent")
divisor =input("Enter the divisor")

crc_value=crc(data,divisor)

received=input("Enter the received data")

if received!=data+crc_value:
    print("Error in transmission")
else:
    print("No error in transmission")



