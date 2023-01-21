import pyqrcode
s = "www.Inprogrammer.com"
url = pyqrcode.create(s)
url.svg("myqr.svg", scale=0)