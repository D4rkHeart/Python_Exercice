message = "EBG13 rknzcyr"
#V1
def rot13(message):
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()*2
    print(alphabet)
    alphabetUpper = "a b c d e f g h i j k l m n o p q r s t u v w x y z".upper().split()*2
    decodedString = ""
    for i in message:
        if i in alphabetUpper:
            decodedString += alphabetUpper[alphabetUpper.index(i)+13]
        elif i in alphabet:
            decodedString += alphabet[alphabet.index(i)+13]
        else:
            decodedString += i
    print(decodedString)

rot13(message)
## V1
import codecs
message = codecs.decode(message, 'rot_13')
print(message)