import qrcode
import urllib.parse
from pathlib import Path

def url_valida(url):
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def salvar_arquivo(url, nome_do_arquivo):
    # Checar se a pasta "QRcodes" existe, caso não exista ela será criada antes do QRcode ser salvo
    pasta = Path("QRcodes")
    if not pasta.exists():  
        pasta.mkdir()

    # A variável "code" guarda o QRcode da url passada
    code = qrcode.make(url)
    
    # variavel "file_path" guarda o caminho do arquivo
    file_path = Path(f"QRcodes/{nome_do_arquivo}.jpeg")

    # Caso o arquivo já exista é criado um arquivo com uma numeração
    if file_path.exists():
        i = 1
        while True:
            new_file_path = Path(f'QRcodes/{nome_do_arquivo}_{i}.jpeg')
            if not new_file_path.exists():
                file_path = new_file_path
                break
            i += 1
    
    # Criação do arquivo em si
    try:
        with open(file_path, 'wb') as file:
            code.save(file)
        print(f"QR code criado e salvo em '{file_path}'.")
    except Exception as e:
        print(f"Erro ao criar: {e}")



while True:
    # Usuário digita a URL que deseja criar um QR code
    print("Digite a URL que você deseja criar o QR code: ")
    url = input()

    # Se o usuário digitar "Q" ele sai do loop
    if url.lower() == 'q':
        break

    # Caso a validação de URL retorne True, ele continua
    if url_valida(url):

        # Usuário digita o nome que deseja dar ao arquivo de QR code
        nome_do_arquivo = input("Digite o nome que deseja colocar no arquivo QR code (sem a extensão): ")
       
        # Execução da função "salvar_arquivo"
        salvar_arquivo(url, nome_do_arquivo)
    else:
        print("Você não digitou uma URL válida.")