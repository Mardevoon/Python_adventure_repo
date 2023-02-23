import urllib
import urllib.request

try:
    site = urllib.request.urlopen('insira um site aqui')
except urllib.error.URLError:
    print('O site requerido está fora do ar no momento')
else:
    print('Tudo ok')