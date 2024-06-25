import cv2
import webbrowser
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    # QR kodu içeren resmi okuyun
    image = cv2.imread(image_path)
    
    # QR kodunu çözümleyin
    qr_codes = decode(image)
    
    if qr_codes:
        # İlk QR kodunun verisini alın (varsayılan olarak tek bir QR kodu olduğunu varsayıyoruz)
        qr_code_data = qr_codes[0].data.decode('utf-8')
        return qr_code_data
    else:
        return None

def open_website(url):
    # URL'yi tarayıcıda açın
    webbrowser.open(url)

def main():
    image_path = "qrMenu.png"  # QR kodu içeren resmin yolu
    qr_code_data = read_qr_code(image_path)
    
    if qr_code_data:
        print(f"QR kodu içeriği: {qr_code_data}")
        open_website(qr_code_data)
    else:
        print("QR kodu okunamadı.")

if __name__ == "__main__":
    main()
