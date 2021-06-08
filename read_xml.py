# Aqui vamos usar a biblioteca para ler o arquivo que criamos
# Do mesmo jeito que usamos ela para criar o arquivo
import xml.etree.ElementTree as ET

# Aqui pegarmos o arquivo com esse 'parse', passando o nome do arquivo
# Passando isso tudo dentro de uma variavel para poder usarmos à frente
root = ET.parse('atilio_lindo.xml').getroot()

# Aqui vamos fazer um looping para entrar dentro do XML
# Percebe que vamos usar a propria variavel que criamos ali encima para entrar no arquivo
for i in root:
    # Aqui pegamos o 'i', que referencia ao nosso 'root'
    # Através do 'i', pegamos os atributos do nosso arquivo XML que criamos
    print(i.text, i.tag)   