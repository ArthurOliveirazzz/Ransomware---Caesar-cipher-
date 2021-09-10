encrypt = ''
decrypt = ''
ask = input("Criptografar (1) ou Descriptografar (2): ")

if(ask == '1'): 
    with open('teste.txt', 'r', encoding='utf-8') as arquivo:
        content = arquivo.read()
            
    for i in range (0, len(content)):
        encrypt = encrypt + chr(ord(content[i]) + 3)

    print(encrypt)

    with open('teste.txt', 'w', encoding="utf-8") as arquivo:
        arquivo.write(encrypt)

    print('Arquivo criptografado com sucesso!')

if(ask == '2'):
    with open('teste.txt', 'r', encoding='utf-8') as arquivo:
        content = arquivo.read()

    for i in range (0, len(content)):
        decrypt = decrypt + chr(ord(content[i]) - 3)

    with open('teste.txt', 'w', encoding="utf-8") as arquivo:
        arquivo.write(decrypt)
    
    print('Arquivo descriptografado com sucesso!')