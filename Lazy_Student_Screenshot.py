import pyscreenshot as ImageGrab
from PIL import ImageChops
import time
from datetime import datetime
from statistics import mean
import imgcompare
from pynput.mouse import Controller
from shutil import copyfile
import os
import io


mouse = Controller()
q=0
img_path = str(input("Cual es la ruta(path) absoluta para guardar las imagenes?"+"\n"))
assert os.path.exists(img_path), "No fue posible encontrar la ruta, "+str(img_path)


#Seleccionar el area para capturar
print("coloca el cursor en el primer punto")
for i in range(5,0,-1):
    time.sleep(1)
    print(i)
x=mouse.position

print("coloca el cursor en el segundo punto")
for i in range(5,0,-1):
    time.sleep(1)
    print(i)
y=mouse.position
coord=x+y


#validar si esta bien
while q==0:
    im0 = ImageGrab.grab(bbox =(coord))
    im0.show()
    ok=input("La imagen es correcta?"+"\n"+"(ok/no)"+"\n")
    if ok=="ok":
        q=1
    else:
        print("coloca el cursor en el primer punto")
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        x=mouse.position

        print("coloca el cursor en el segundo punto")
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        y=mouse.position
        coord=x+y

now = datetime.now()
im1 = ImageGrab.grab(bbox =(coord))
im1.save('primera.png', 'PNG')
n=0
while True:
    time.sleep(2)
    im2 = ImageGrab.grab(bbox =(coord))
    percentage = imgcompare.image_diff_percent(im1, im2)
    print(percentage)

    if percentage < 1:
        print('igual')
    else:
        print('diferente')
        im2_name = now.strftime("%Y%m%d_")
        im2.save(img_path+im2_name+str(n)+'.png', 'PNG')
        n=n+1
    im1=im2
        