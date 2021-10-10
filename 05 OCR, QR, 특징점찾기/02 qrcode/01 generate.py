import qrcode

img = qrcode.make('this is another test')
type(img)
img.save('img/test.jpg')