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
    import optparse

    #vamos instância para receber os argumentos
    parser = optparse.OptionParser('Use o promgrama:' '-a <Caminho do arquivo> ' '-w <Wordlista.txt>')
    #vamos adicionar opções
    parser.add_option('-a', dest='caminho', \
                    type='string', help='Informar o caminho do arquivo')
    parser.add_option('-w', dest='wordlist', type='string', help='Informe a wordlista de senha que deseja testar')
    (options, args) = parser.parse_args()
    #vamos validar se o caminho do arquivo foi passado.
    if options.caminho == None or options.wordlist == None:
        print(parser.usage)
        exit(0)
    else:
        # o arquivo zipado protegido por senha
        zip_nome = options.caminho
        zip_file = zip_nome.strip()
        # A lista com as senhas, no mesmo diretorio
        word_nome = options.wordlist
        wordlist = word_nome.strip()
        # inicializa o objeto do arquivo zip
        zip_file = zipfile.ZipFile(zip_file)
        # conta o numero de palavras na wordlist
        n_words = len(list(open(wordlist, "rb")))
        print(f'Total de senhas para testar: {n_words}')
        senha_correta = Open_arq(wordlist, n_words)
        print(f'[+] Senha Encontrada: {senha_correta}')
        exit(0)





    
    

    


