import cv2
import pyzbar.pyzbar as pyzbar


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

previous_qr = ""

while True:
    success, frame = cap.read()

    codes = pyzbar.decode(frame)

    if not codes:
        previous_qr = ""

    else:
        for code in codes:
            recognized_qr = code.data.decode('utf-8')

            if recognized_qr == previous_qr:
                continue
            previous_qr = recognized_qr
            print(recognized_qr)

    cv2.imshow("QR", frame)
    cv2.waitKey(1)