import qrcode
img = qrcode.make('LG TV [FAKE PRODUCT],Model:ML225LL/A')
type(img)  
img.save("lg-tv-fake.png")