def generate_encrypted_string(string):
    out = ""
    for i in string:
        if not i.isalpha():
            out = out+i
        else:
            asc = ord(i)
            if((asc>=97 and asc<=109) or (asc>=65 and asc<=77)):
                out = out + chr(asc+13)
            else:
                out = out + chr(asc-13)
    return out

print generate_encrypted_string("a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 !@#$%^&*()_+=- A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
