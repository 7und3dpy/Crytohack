from Crypto.PublicKey import RSA
with open(r"C:\Users\DELL\OneDrive - Hanoi University of Science and Technology\Crytohack\Mathematics\"C:\Users\DELL\OneDrive - Hanoi University of Science and Technology\Crytohack\Mathematics\privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem","r") as f:
    print(RSA.import_key(f.read()))