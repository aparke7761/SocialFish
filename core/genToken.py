import secrets
import qrcode.image.svg
import qrcode
import os

def genToken():
    return ''.join(secrets.token_urlsafe(16))

def genQRCode(revoked=False):
	qr = 'templates/static/token/qrcode.svg'
	if revoked:
		os.remove(qr)
	if not os.path.exists(qr):
		factory = qrcode.image.svg.SvgImage
		img = qrcode.make(genToken(), image_factory=factory)
		img.save(qr)
	else:
		os.remove(qr)
