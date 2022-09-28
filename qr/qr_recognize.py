# +------------+--------------+-----------------------------------------------------------+
# |   Author   |     Date     |                         Changed                           |
# +------------+--------------+-----------------------------------------------------------+
# |  Andrew A. |  2022/09/28  | Initial release (basic QR recognition)                    |
# +------------+--------------+-----------------------------------------------------------+


import cv2
import pyzbar.pyzbar as pyzbar
import dbman


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

previous_qr = ""
interval = 0

while True:
    success, frame = cap.read()

    codes = pyzbar.decode(frame)

    if not codes:
        interval += 1

        if interval > 20:
            interval = 0
            previous_qr = ""

    else:
        for code in codes:
            recognized_qr = code.data.decode('utf-8')
            name = dbman.find_name(int(recognized_qr))
            frame = cv2.rectangle(frame, code.rect, (255, 0, 0), 2)
            frame = cv2.putText(frame, recognized_qr + name, code.polygon[2], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, 2)

            if not recognized_qr == previous_qr and interval < 10:
                previous_qr = recognized_qr
                print(recognized_qr, name)
                print(code)

    cv2.imshow("QR", frame)
    cv2.waitKey(1)