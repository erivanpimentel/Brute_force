# 🔐 Zip Password Cracker (Python)

Este projeto é um script em Python que utiliza força bruta para tentar descobrir a senha de arquivos `.zip` protegidos por senha, utilizando uma **wordlist** fornecida pelo usuário.

O script exibe uma **barra de progresso com `tqdm`**, facilitando a visualização do processo.

> ⚠️ Uso estritamente educacional e ético! Nunca utilize este script para acessar arquivos que você **não tem permissão legal**.

---

## 🧠 O que o script faz?

1. Recebe via terminal o caminho do arquivo `.zip` e o caminho para uma wordlist
2. Conta quantas senhas existem na lista
3. Tenta extrair o conteúdo do `.zip` usando cada senha da lista
4. Para imediatamente quando encontra a senha correta
5. Exibe o resultado no terminal

---

## ⚙️ Requisitos

- Python3
- [`tqdm`](https://pypi.org/project/tqdm/) instalado  
  👉 Instale com: `pip install tqdm`

---

## 🚀 Como usar

```bash
python3 zip_cracker.py -a <CAMINHO_DO_ARQUIVO_ZIP> -w <CAMINHO_DA_WORDLIST>

✅ Exemplo prático:
  python3 zip_cracker.py -a arquivos/protegido.zip -w wordlists/senhas.txt


📌 Saída esperada
Se a senha estiver na wordlist, você verá:
 Total de senhas para testar: 15000
  [+] Senha Encontrada: minhaSenha123

Se não estiver:
  [*[*]*] Não foi possível encontrar a senha, você pode tentar outra wordlista de senhas!



🛠️ Tecnologias e bibliotecas usadas
  zipfile → para manipular arquivos .zip com senha
  tqdm → exibe barra de progresso
  optparse → leitura de argumentos da linha de comando

🛑 Aviso de Ética e Responsabilidade
Este projeto foi desenvolvido para fins educacionais e experimentação segura.

Não utilize este script para tentar quebrar senhas de arquivos de terceiros sem autorização explícita.
Respeite a legislação e os princípios da ética em segurança da informação.

