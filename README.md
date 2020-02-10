# Handling_PDF_files
PYTHON - Ler arquivos PDF - Extrair texto de arquivos PDF - Ler varios arquivos com Python

Usado para coletar Chave de Acesso de NFe para importação no sistema ERP.
Desenvolvido na Versão Python 3.7.4
# Note:
  - Cada emissor de NFe gera seu PDF em um padrão diferente. Consegui coletar de todos arquivos que possuo, mas, extrai dados não numericos também, que precisam ser tratados no arquivo de saída.
  
  =============================================================================================================================
  1 - Modulos necessarios(Instalar com 'pip install'):
      - io
      - pdfminer
      - os
      
  2 - Executar no terminal>> python Extrair_Chave_NFe.pdf
  3 - Digitar caminho completo da pasta onde estão os aquivos PDF.
  4 - Nomeie o arquivo de saida conforme sua preferência na linha 60-'numeros_de_chave = open('ChavesNF.txt','w')'
