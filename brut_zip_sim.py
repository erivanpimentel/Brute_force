def Open_arq(wordlist, n_words):
    # abre o arquivo e tenta uma senha
    with open(wordlist, "rb") as wordlist:
        for word in tqdm(wordlist, total=n_words, unit="word"):
            try:
                zip_file.extractall(pwd=word.strip())
            except:
                continue
            else:
                senha_arq = word.decode().strip()
                return senha_arq
                
    print("[*[*]*] Não foi possível encontra a senha, você pode tentar outra wordlista de senhas!")

if __name__ == '__main__':
    #Para trabalhamos com arquivos zip
    import zipfile
    #Caso não tenha o "tqdm" instalado utilize o comando --> pip3 install tqdm
    # Com o tqdm vamos mostrar uma barra de progesso.
    from tqdm import tqdm

    # A lista com as senhas, no mesmo diretorio
    wordlist = "Wordlist_senha.txt"
    # o arquivo zipado protegido por senha "Em "nome_do_arquivo_zipado.zip" Troque pelo nome do seu arquivo zipado"
    zip_file = "nome_do_arquivo_zipado.zip"

    # inicializa o objeto do arquivo zip
    zip_file = zipfile.ZipFile(zip_file)
    # conta o numero de palavras na wordlist
    n_words = len(list(open(wordlist, "rb")))
    print(f'Total de senhas para testar: {n_words}')

    senha_correta = Open_arq(wordlist, n_words)
    print(f'[+] Senha Encontrada: {senha_correta}')
    exit(0)
