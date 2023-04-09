import pyqrcode

# URL address where qr code is requested to be generated
qr = "https://bunyaminyavuz.github.io/"

# Qr code generator
url = pyqrcode.create(qr)

# Generating qr code in .svg file
url.svg("myWebsiteQrCode.svg", scale=10)