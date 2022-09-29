# +------------+--------------+-----------------------------------------------------------+
# |   Author   |     Date     |                         Changed                           |
# +------------+--------------+-----------------------------------------------------------+
# |  Andrew A. |  2022/09/28  | Initial release (basic QR recognition)                    |
# +------------+--------------+-----------------------------------------------------------+
# |  Andrew A. |  2022/09/28  | Display name using Pillow. Minor debug                    |
# +------------+--------------+-----------------------------------------------------------+


from PIL import ImageFont, ImageDraw, Image
import pyzbar.pyzbar as pyzbar
import numpy
import dbman
import cv2


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
font = ImageFont.truetype("../resources/NanumGothic-Bold.ttf", 20)

previous_qr = ""
interval = 0

while True:
    success, frame = cap.read()

    codes = pyzbar.decode(frame)

    if not codes:
        interval += 1

        if interval > 50:
            interval = 0
            previous_qr = ""

    else:
        for code in codes:
            print(code)
            recognized_qr = code.data.decode('utf-8')

            # 데이터베이스에서 이름 검색
            name = dbman.find_name(recognized_qr)

            # 데이터베이스에서 일치하는 이름을 찾지 못하면 다른 QR로 간주함
            if not name:
                continue

            # QR 인식 표시
            frame = cv2.rectangle(frame, code.rect, (255, 0, 0), 2)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            draw = ImageDraw.Draw(frame)
            draw.text(
                code.polygon[2], recognized_qr + " " + name,
                font=font,
                fill=(255, 255, 255),
                stroke_width=3,
                stroke_fill=(0, 0, 0)
            )

            frame = numpy.array(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            if not recognized_qr == previous_qr and interval < 45:
                previous_qr = recognized_qr
                print(recognized_qr, name)
                print(code)
                dbman.insert_data(recognized_qr, name, 36.5)

    cv2.imshow("QR", frame)

    if cv2.waitKey(1) == ord('q'):
        break
