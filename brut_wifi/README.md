# 📡 WiFi Brute Force Finder (com nmcli)

Este script em Python realiza **testes automatizados de conexão Wi-Fi via força bruta** utilizando a ferramenta `nmcli` (Network Manager CLI).

O objetivo do projeto é **aprimorar o entendimento sobre segurança em redes wireless**, explorando a tentativa de autenticação com múltiplas senhas a partir de uma **wordlist personalizada**.

> ⚠️ **Uso exclusivo para fins educacionais e ambientes de teste controlados.**

---

## 🧠 O que o script faz?

1. Lista todas as redes Wi-Fi disponíveis usando `nmcli`
2. Pede ao usuário o nome da rede, a interface de rede e uma wordlist
3. Tenta se conectar à rede fornecida testando senha por senha
4. Informa quando uma senha correta é encontrada

---

## ⚙️ Requisitos

- Python3
- Sistema Linux com `nmcli` instalado
- Permissões adequadas para alterar conexões de rede
- Placa de rede Wi-Fi compatível
- Wordlist com senhas (ex: `wordlist.txt`)

---

## 🚀 Como usar

  python3 wifi_bruteforce.py -d <NOME_DA_REDE> -w <WORDLIST> -i <INTERFACE>

✅ Exemplo prático:
  python3 wifi_bruteforce.py -d "MinhaRedeWiFi" -w wordlist.txt -i wlan0
  Esse comando vai testar todas as senhas da wordlist.txt na rede chamada "MinhaRedeWiFi" usando a interface wlan0.


🛠️ Tecnologias utilizadas
    subprocess → para executar comandos do sistema com nmcli
    
    optparse → para lidar com os argumentos do terminal
    
    nmcli → ferramenta nativa do Linux para gerenciamento de redes
    
    time, os, string → funções auxiliares no processo

📌 Observações
A wordlist deve conter uma senha por linha.

O script para quando encontra a senha correta (ou quando a lista acaba).

A interface usada (ex: wlan0, wlp2s0) deve estar ativa.

⚠️ Aviso de Ética e Legalidade
Este projeto tem caráter puramente educacional.
Jamais utilize este script para acessar redes sem autorização.
Testes desse tipo devem ser feitos somente em ambientes controlados ou com permissão explícita.

📚 Aprender segurança da informação também é aprender responsabilidade.




