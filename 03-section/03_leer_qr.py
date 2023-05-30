import qrcode
 
data = 'Gabriel Casas ejemplo python 2569874523652'
 
img = qrcode.make(data)
 
img.save('mi-qr.png')