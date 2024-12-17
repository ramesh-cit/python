import cv2
import blockchain as _blockchain
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
blockchain = _blockchain.Blockchain()

with open("authorized-qr.txt") as f:
    authorizedProducts = f.read().splitlines()

while True:

    success, img = cap.read()
    for barcode in decode(img):
        productCode = barcode.data.decode("utf-8")
        print(productCode)

        if (blockchain.is_item_in_blockchain(productCode)):
            message = "Authorized " + productCode
            textColor = (0, 255, 0)
        else:
            message = "Un-Authorized " + productCode
            textColor = (0, 0, 255)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, textColor, 5)
        pts2 = barcode.rect
        cv2.putText(
            img,
            message,
            (pts2[0], pts2[1]),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            textColor,
            2,
        )

    cv2.imshow("Result", img)
    keycode = cv2.waitKey(10)
    if keycode == ord('q'):
        break
