import pyqrcode
import png
from pyqrcode import QRCode
link=input("ENTER LINK :")
download=pyqrcode.create(link)
download.png("images.png",scale=4)
print("Downloaded..")