a = input('Texto para criptografar: ')
texto = []
encoded = []
cipher = []
for letra in a:
    code = ord(letra)
    b = texto.append(code)
    
for num in texto:
    encoded.append(num+1)
    
for x in encoded:
    cha = chr(x)
    y = cipher.append(cha)
str1 = ''.join(cipher)
print(str1)
