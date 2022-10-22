import os
from path import Path
from cryptography.fernet import Fernet

class encriptacao:
    def generate_keys(name_key):
        name_key = name_key + ".key"
        generated_key = Fernet.generate_key()
        with open(name_key, 'wb') as new_key:
            new_key.write(generated_key)
            print("Chave gerada com sucesso!!")

    def open_key(name_key):
        try:
            with open(name_key, 'rb') as load_key:
                key = Fernet(load_key.read())
                return key
        except FileNotFoundError:
            print("Não foi possivel carregar ou encontrar a chave -> {}".format(FileNotFoundError))

    def encrypt_files(diretorio, nome_chave):
        loaded_key = encriptacao.open_key(nome_chave)
        diretorio_to_encrypt = os.chdir(diretorio)
        with os.scandir(diretorio_to_encrypt) as arquivos:
            for lista_arquivos in arquivos:
                arquivo = Path(lista_arquivos.name)
                if arquivo.isfile() == True:
                    print(arquivo.name)
                    try:
                        with open(arquivo.name, "rb") as file:
                            file_data = file.read()
                            encrypt_data = loaded_key.encrypt(file_data)
                            with open(arquivo.name, "wb") as encritp_file:
                                encritp_file.write(encrypt_data)
                    except PermissionError:
                        print("Sem premisão para criptografar o arquivo {}".format(PermissionError))

    def decrypt_files(diretorio, nome_chave):
        loaded_key = encriptacao.open_key(nome_chave)
        diretorio_to_dencrypt = os.chdir(diretorio)
        with os.scandir(diretorio_to_dencrypt) as arquivos:
            for lista_arquivos in arquivos:
                arquivo = Path(lista_arquivos.name)
                if arquivo.isfile() == True:
                    with open(arquivo.name, "rb") as file:
                        file_data = file.read()
                        decript_data = loaded_key.decrypt(file_data)
                        with open(arquivo.name, "wb") as decritp_file:
                            print(arquivo.name)
                            decritp_file.write(decript_data)