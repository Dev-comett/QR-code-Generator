#pip install qrcode
#pip install pillow(PIL)

import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=30,border=10,)
#add any desired URL below:
qr.add_data("https://github.com/")
#fit=True checks the URL 
qr.make(fit=True)

img=qr.make_image(fill_color="pink", back_color="black")
#save the image name as per the URL
img.save("GITHUB.png")

#image will saved in the file folder, path such >>> C:\Users\user\OneDrive\Desktop


   