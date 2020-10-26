# Written by Lateraluz++.
# 25-8-2019
# I wrote it using Python because I don't ever program using it, so it was a opportunity to learn something new.
# Feel free to improve it and share it, Knowledge belongs to humanity!
# Info got it from  https://github.com/robchava/LectorCedulasCR/blob/master/app/src/main/java/com/vbalex/cedulascr/CedulaCR.java

#imports
import re

# Definitions
def xorOperation(p1, p2):
    return p1 ^ p2


def getString():
    # Private Key to decrypt using Xor Algoritm ()
    key = [0x27, 0x30, 0x04, 0xA0, 0x00, 0x0F, 0x93, 0x12, 0xA0, 0xD1, 0x22, 0xE0, 0x03, 0xD0, 0x00, 0xDf, 0x00]

    # data readed from id in format pdf 417
    # Info can be extracted scanning Identificaciont and upload the file at https://online-barcode-reader.inliteresearch.com/
    dataFromId = [0x16 ,0x01 ,0x36 ,0x91 ,0x38 ,0x3f ,0xa4 ,0x24 ,0x98 ,0x9c ,0x7c ,0xb9 ,0x42 ,0xd0 ,0x00 ,0xdf ,
                    0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,
                    0xdf ,0x00 ,0x27 ,0x63 ,0x45 ,0xee ,0x43 ,0x47 ,0xd6 ,0x48 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,
                    0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x75 ,0xa1 ,0x41 ,
                    0x99 ,0x41 ,0x91 ,0x20 ,0x66 ,0x62 ,0x49 ,0xe1 ,0x4e ,0x4b ,0xdc ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,
                    0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0xde ,0x23 ,0x99 ,0xe9 ,0x07 ,
                    0xd0 ,0x3a ,0xe2 ,0x34 ,0xed ,0x30 ,0x15 ,0x01 ,0x34 ,0x98 ,0x30 ,0x37 ,0x93 ,0x12 ,0xa0 ,0xd1 ,
                    0x33 ,0xe0 ,0x03 ,0xd0 ,0x31 ,0xe9 ,0x02 ,0x14 ,0x30 ,0x54 ,0xf0 ,0xff ,0x8f ,0x13 ,0x81 ,0x3d ,
                    0x45 ,0xb1 ,0x78 ,0x77 ,0x77 ,0x66 ,0x6a ,0xb3 ,0x85 ,0x99 ,0xb2 ,0xc7 ,0x8a ,0xa7 ,0x19 ,0x8c ,
                    0x2f ,0x62 ,0x86 ,0x8e ,0x83 ,0x41 ,0x7c ,0x49 ,0x5a ,0x59 ,0x5e ,0x79 ,0xcc ,0x6e ,0xdc ,0x1f ,
                    0xdb ,0x3a ,0x12 ,0xa4 ,0x6a ,0x68 ,0x46 ,0x59 ,0x4a ,0x8f ,0x9a ,0x44 ,0x83 ,0x38 ,0x80 ,0x94 ,
                    0xda ,0x89 ,0x68 ,0xbc ,0x62 ,0x73 ,0x64 ,0x45 ,0x76 ,0x53 ,0x41 ,0x5b ,0x8a ,0x83 ,0xf8 ,0x78 ,
                    0xc6 ,0x1f ,0x7c ,0xd0 ,0xbe ,0x4a ,0x95 ,0x7a ,0x8f ,0x62 ,0x6f ,0x92 ,0x59 ,0x5f ,0xa7 ,0x32 ,
                    0xb3 ,0x90 ,0x18 ,0x7c ,0x2f ,0x88 ,0xbc ,0x82 ,0xb8 ,0x7d ,0x9e ,0x80 ,0xaa ,0x7e ,0x84 ,0x5a ,
                    0x10 ,0xa8 ,0x90 ,0x33 ,0xb2 ,0x36 ,0x07 ,0x9c ,0x37 ,0x56 ,0x2f ,0x5b ,0x92 ,0x2e ,0x0a ,0x85 ,
                    0x15 ,0xf2 ,0xfd ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,
                    0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,
                    0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,
                    0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,
                    0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,
                    0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,
                    0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,
                    0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,
                    0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,
                    0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,
                    0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x32 ,0x2f ,0xa0 ,0x57 ,0x5d ,0x6c ,0x92 ,
                    0x20 ,0x43 ,0x95 ,0x4e ,0x69 ,0x47 ,0xad ,0x7a ,0x87 ,0xa0 ,0x8d ,0x7c ,0x15 ,0x7b ,0xa5 ,0x08 ,
                    0x81 ,0x17 ,0x4b ,0xfe ,0x66 ,0x39 ,0x4b ,0x56 ,0x49 ,0x5e ,0xb6 ,0x74 ,0x94 ,0xf0 ,0x81 ,0x62 ,
                    0xfa ,0x8c ,0xca ,0x40 ,0xb9 ,0x42 ,0xb3 ,0x45 ,0xa2 ,0x75 ,0xb5 ,0x82 ,0x9d ,0xbc ,0x1d ,0xc2 ,
                    0x83 ,0xe6 ,0xa4 ,0x1a ,0x65 ,0xf5 ,0x40 ,0xcf ,0x42 ,0xc2 ,0x65 ,0xbd ,0x89 ,0xfe ,0xae ,0xe6 ,
                    0xa3 ,0x5c ,0x0e ,0x28 ,0x27 ,0xb7 ,0xb3 ,0xbc ,0x73 ,0xaf ,0x8c ,0x56 ,0x60 ,0xbf ,0x6f ,0x9a ,
                    0xce ,0x86 ,0x9f ,0x01 ,0x64 ,0x2c ,0x50 ,0x60 ,0x25 ,0xf6 ,0xa1 ,0xfb ,0x01 ,0x5e ,0xac ,0x7a ,
                    0x51 ,0x57 ,0x75 ,0x29 ,0x6e ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,
                    0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,
                    0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,
                    0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,
                    0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,
                    0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,
                    0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,0xe0 ,
                    0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,0x33 ,
                    0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,0xd1 ,
                    0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,0xa0 ,
                    0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04 ,0xa0 ,0x00 ,0x0f ,0x93 ,0x12 ,
                    0xa0 ,0xd1 ,0x33 ,0xe0 ,0x03 ,0xd0 ,0x00 ,0xdf ,0x00 ,0x27 ,0x30 ,0x04]

    # Convert the list to byte array
    keyBytes = bytearray(key)
    dataFromIdBytes = bytearray(dataFromId)

    # index used in order to get info from dataFromId
    index = 0
    data = ""

    for byteFromArray in dataFromIdBytes:
        # Xor array to decrypt is 17 long bytes, reset when counter is 17
        if index == 17:
            index = 0

        caracter = xorOperation(keyBytes[index], byteFromArray);

        # From byte to char
        char_caracter = chr(caracter);

        # MUST include either letters or numbers
        if re.match("^[a-zA-Z0-9]*$", char_caracter):
            data += char_caracter
        else:
            data += " "
        # increment index
        index = index + 1;
    return data

class Tico:
    def __init__(self,data):
        self.data = data

    def getId(self):
        return self.data[0:9]

    def getApellido1(self):
        return self.data[9:35]

    def getApellido2(self):
        return self.data[35:61]

    def getNombre(self):
        return self.data[61:91]

    def getSexo(self):
        return self.data[91]

    def getFechaNacimiento(self):
        return self.data[92: 96] + "-" + self.data[96: 98] + "-" + self.data[98: 100]

    def getFechaVencimiento(self):
        return self.data[100: 104] + "-" + self.data[104: 106] + "-" + self.data[106: 108]

def main():
    data = getString()
    # print string with whole data
    # print(data)
    #instance Object
    tico = Tico(data)
    print("Identificacion :", tico.getId())
    print("Apellido1      :", tico.getApellido1())
    print("Apellido2      :", tico.getApellido2())
    print("Nombre         :", tico.getNombre())
    print("Sexo           :", tico.getSexo())
    print("F. Nacimiento  :", tico.getFechaNacimiento())
    print("F. Vencimiento :", tico.getFechaVencimiento())


# main
if "__main__":
    main();




