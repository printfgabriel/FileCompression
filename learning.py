from collections import Counter

binary_representation = {
    '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111', '0000', '0001', '0010', # representation for the 11 most common binaries
    '0011' #this one is the break from normal binary representation to  this representation 
}


def to_byte(binary_string):
    # converting binary string to bytes
    return int(binary_string, 2).to_bytes((len(binary_str) + 7) // 8, byteorder='big')

def changing_binary(count, content):

    char_to_binary = {char: binary_representation[i] for i, (char, _) in enumerate(count)}

    with open("C:/Users/Gabriel/OneDrive/Programação/File Compression/output.txt", "wb") as output:
        writing_my_representation = False
        for letter in content: # for each letter read
            if letter in char_to_binary: #if it's in top 11
                if writing_my_representation == False:
                    #output.write(binary_representation[11])
                    writing_my_representation = True 
                    output_file.write(binary_representation[-1].encode('utf-8')) 
                    output.write(letter.encode('utf-8'))
                else:
                    #output.write(binary_representation[ Index(count[letter])-1 ])   #seems like this doesn't work properly, cause it writes bits
                    output_file.write(char_to_binary[letter].encode('utf-8'))

            else:    
                output.write(letter.encode('utf-8'))
    output.close()
    return
    

def main():
    with open("C:/Users/Gabriel/OneDrive/Programação/File Compression/teste.txt", "rb") as file:   #opening file as binary
        content = file.read()
        bytes_count = Counter(content)

        #count = Counter(content).most_common(len(binary_representation)-1)
        changing_binary(bytes_count, content)
        
        print(bytes_count)
        file.close()


main()