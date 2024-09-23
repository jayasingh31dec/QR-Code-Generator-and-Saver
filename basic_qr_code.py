import qrcode
img = qrcode.make("https://www.indiamart.com/proddetail/fresh-apple-fruit-19835557748.html")
img.save("example.png")


# # Customization
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data("https://example.com")
# qr.make(fit=True)
# img = qr.make_image(fill_color="blue", back_color="yellow")
# img.save("custom_qr.png")
#
#





