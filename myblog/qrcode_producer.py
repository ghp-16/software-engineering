import qrcode


def produce_qrcode(url, path):
    img = qrcode.make(url)
    with open(path, 'wb') as f:
        img.save(f)
