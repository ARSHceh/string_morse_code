import pyfiglet as pyfiglet


morse_code = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"---."
}




def to_color(string, color):
    color_code = {'blue': '\033[34m',
                    'yellow': '\033[33m',
                    'green': '\033[32m',
                    'red': '\033[31m'
                    }
    return color_code[color] + str(string) + '\033[0m'

result = pyfiglet.figlet_format("String to Morse Code Converter\nBy ARSHMAN", font = "slant")

print(to_color(result,'red'))

user_ = str(input("Enter String/Letter's to Encrypt :").upper())



def encrypt(user:str):
    encrypted_code = ""
    for x in range(0,len(user)):
        for y in morse_code.keys():
            if y == user[x]:
                encrypted_code += morse_code[y]
            else:
                pass

    return encrypted_code




print(f"Encrypted Text : {encrypt(user_)}")

