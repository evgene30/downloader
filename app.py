from urllib import request
import sys
import time
from alive_progress import alive_bar

myURL = str(input('Введите ссылку для загрузки: '))
myFILE = '/home/pavel/Загрузки/' + str(input('Сохранить объект под именем: '))

try:
    print('Start DOWNLOAD => ' + myURL)
    a = request.urlretrieve(myURL, myFILE)
    with alive_bar(len(a)) as bar:
        for i in a:
            bar()
            time.sleep(1)
    print('DOWNLOAD complete!')

except Exception:
    print("Download error!", sys.exc_info())
    exit()