import qrcode

# Creating QR code object
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,  
    border = 4,     
)

# Add the link
qr.add_data("https://{researcher's GitHub ID}.github.io/{project name}")
qr.make(fit=True)

# Generate the QR code
img = qr.make_image(fill_color = "black", back_color = "white")

# Show the code
img.show()

# Save the code
img.save("survey_qr.png")
