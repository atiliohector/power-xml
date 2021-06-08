# Esse é um exemplo de código que CRIA um arquivo XML

# Primeiro passo do código é a importação da biblioteca (Essa 'cElementTree')

# Vamos usá-la para criar o arquivo XML

# Ela vem como buil-tin do Python, ou seja, ela vem de "nascença" junto com o Python. 
# Não precisa instalar nada
import xml.etree.cElementTree as ET


# Agora a gente cria a estrutura
# Essa estrutura é como tags do HTML

# A primeira tag vou chamar de 'lindo'
# Percebe que eu uso a biblioteca que chamamos lá encima e crio a tag 'lindo'
root = ET.Element("lindo")
# Agora crio a outra tag, chamada de 'maravilhoso', sempre usando a mesma biblioteca
# Só que aqui eu conecto com a tag 'lindo' (pelo nome 'root')
doc = ET.SubElement(root, "maravilhoso")

# Agora uso a biblioteca para criar o restante da estrutura, como 'name', 'text'.
# Todas essas informações eu posso colocar do jeito eu eu quiser, personalizar de qualquer jeito
ET.SubElement(doc, "espaco1", name="espacozinho").text = "Atilio Maravilhoso"
ET.SubElement(doc, "espaco2", name="espacozao").text = "Atilio: o mais lindo"

# Agora eu crio a estrutura final com a mesma biblioteca
# Aqui uso o 'ET' da biblioteca e passo o 'root', que foi a base da estrutura que criei lá encima
tree = ET.ElementTree(root)
# Aqui peço para criar o arquivo, dizendo o nome que quero da pra ele
# Lembrando que a extensão é 'xml', então no final eu coloco assim: 'nome.xml'
# No caso: 'atilio_lindo.xml'
tree.write("atilio_lindo.xml")

# Got it?