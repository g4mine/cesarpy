put = input('Texto para criptografar: ')
a = put.replace('z', '`')
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
result = str1.replace('!', ' ')
print(result)
