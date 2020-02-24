from urllib import request, parse
import base64

#Le o arquivo .zip e retornar os bytes em base64
def readBytes(file):
     
     file_zip = open(file,"rb")
     file_zip_base64 = base64.b64encode(file_zip.read())
     return file_zip_base64

#Envia os bytes em base64 para o dontpad
def sendFile(file_zip_base64,dontpad):

     data_data = {"text":file_zip_base64}
     data = parse.urlencode(data_data).encode()
     req =  request.Request("http://dontpad.com/"+dontpad, data=data)
     resp = request.urlopen(req)

#Baixa os bytes em base64 do dontpad
def downFile(dontpad):

     dontpad = request.urlopen("http://dontpad.com/"+dontpad)
     html_dontpad = dontpad.read().decode()
     text_area_start = html_dontpad.find('<textarea id="text">') + len('<textarea id="text">')
     html_dontpad = html_dontpad[text_area_start:]
     text_area_stop = html_dontpad.find('</textarea>')
     file_zip_base64 = html_dontpad[:text_area_stop]
     return file_zip_base64

#Realiza do decode do base64 e escreve o arquivo
def writeFile(file_zip,file_name):
     file_zip = base64.b64decode(file_zip)
     arq = open(file_name, "wb")
     arq.write(file_zip)
     arq.close()

def main(args):
     if args[1] == "-u":
          file_zip_base64 = readBytes(args[2])
          sendFile(file_zip_base64,args[3])
          
     elif args[1] == "-d":
          file_zip = downFile(args[3])
          writeFile(file_zip, args[2])
          
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))




                         





