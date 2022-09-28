# +------------+--------------+-----------------------------------------------------------+
# |   Author   |     Date     |                         Changed                           |
# +------------+--------------+-----------------------------------------------------------+
# |  Andrew A. |  2022/09/28  | Initial release (basic QR recognition)                    |
# +------------+--------------+-----------------------------------------------------------+


import cv2
import pyzbar.pyzbar as pyzbar


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

        if interval > 10:
            interval = 0
            previous_qr = ""

    else:
        for code in codes:
            recognized_qr = code.data.decode('utf-8')

            if not recognized_qr == previous_qr:
                previous_qr = recognized_qr
                print(recognized_qr)

    cv2.imshow("QR", frame)
    cv2.waitKey(1)