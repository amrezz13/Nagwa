from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab_qrcode import QRCodeImage
import qrcode


def qrcreator(url, name, author):
    doc = Canvas('pdf/'+name+'.pdf')
    qr = QRCodeImage(
        size=50 * mm,
        fill_color='black',
        back_color='white',
        border=4,
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
    )
    qr.add_data(url)
    qr.drawOn(doc, 80 * mm, 200 * mm)
    doc.drawString(250, 500, author)
    doc.drawString(250, 400, name)

    doc.showPage()
    doc.save()
