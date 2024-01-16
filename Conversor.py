from pdf2docx import Converter

# Caminho para o arquivo PDF a ser convertido
arquivo_pdf = 'C:/Users/Documento.pdf'

# Caminho para o arquivo DOCX de saída
arquivo_docx = 'C:/Users/DocumentoConvertido.docx'

# Inicializa o objeto Converter com o caminho do arquivo PDF
conversor = Converter(arquivo_pdf)

# Realiza a conversão do PDF para o formato DOCX
# Inicia da página 1 e vai até a última página do PDF
conversor.convert(arquivo_docx, start=0, end=None)

# Fecha o objeto Converter após a conversão
conversor.close()
