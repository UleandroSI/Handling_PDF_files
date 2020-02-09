# version__ = "0.1"
# autor__ = "UleandroSI"

from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

#converts pdf, returns its text content as a string
#from https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    #infile = file(fname, 'rb')
    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

# Chave_de_acesso function - to get the string from the location of the chave de acesso.
# Retira somente o campo da chave da NF
def chave_de_acesso(text):
    onde = stringSaida.find('ACESSO') # Encontrar palavra chave antes dos numeros
    inicio = onde + 6 # Posição de inicio da chave da NF
    fim = inicio + 54 # Posição final de todos caracteres da NF
    numero = stringSaida[inicio:fim]
    #print(numero) # Teste se captura a string com o numero da chave corretamente.
    return numero

# Procurar_arquivos function - list files within the directory 'caminho'
def procurar_arquivos(lista_de_arquivos, caminho):
    for arquivo in lista_de_arquivos:
        # print(arquivo) # Teste para saber os nomes dos arquivos na pasta
    # Para abrir PDF online  urlopen(“https://s3.novatec.com.br/sumarios/sumario-9788575226926.pdf&#8221;)
        local = caminho + '/' + arquivo # Juntar caminho da pasta + nome do arquivo PDF.
        #print(local) #Teste para saber se esta correto o caminho
        arquivoPDF = open(local,'rb') # Abrir cada arquivo PDF para leitura
        #print(stringSaida,'\n') #Teste para visualizar o conteudo do PDF.
        text = convert(arquivoPDF) #get string of text content of pdf
        chave = chave_de_acesso(text) # Chamada de funçao para retornar string com o numero da chave.
        chave = chave.replace(" ","") # Remover espaços da chave
        #print(chave)
        numeros_de_chave.write(chave) # Grava chave no arquivo ChavesMMJ.txt
        numeros_de_chave.write('\n')
        arquivoPDF.close()  # Fechar arquivo PDF lido


numeros_de_chave = open('ChavesMMJ.txt','w') # Arquivo para gravar, já em numero, as chaves lidas.
caminho = str(input("Digite o caminho da pasta: ")) # Solicitar caminho da pasta onde estão os arquivos PDFs.
lista_de_arquivos = os.listdir(caminho) # Carrega a pasta dos arquivos para interar e ler cada um com o FOR
arquivo = procurar_arquivos(lista_de_arquivos, caminho)

numeros_de_chave.close() # Fechar arquivo com as chaves salvas.