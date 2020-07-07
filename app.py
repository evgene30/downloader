from urllib import request
import sys
import time
from tqdm import tqdm

myURL = str(input('Введите ссылку для загрузки: '))
myFILE = '/home/pavel/Загрузки/' + str(input('Сохранить объект под именем: '))

try:
    print('Start DOWNLOAD => ' + myURL)
    a = request.urlretrieve(myURL, myFILE)
    for i in tqdm(a):
        time.sleep(0.01)
    print('DOWNLOAD complete!')

except Exception:
    print("Download error!", sys.exc_info())
    exit()