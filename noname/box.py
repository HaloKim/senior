import cv2
class Recognition:
    def ExtractNumber(self):
        Number = 'sample.jpeg'
        img = cv2.imread(Number, cv2.IMREAD_COLOR)
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('gray.jpg', img2)
        blur = cv2.GaussianBlur(img2, (3, 3), 0)
        cv2.imwrite('blur.jpg', blur)
        canny = cv2.Canny(blur, 100, 200)
        cv2.imwrite('canny.jpg', canny)
        contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        box = []

        # Set the Box threshold
        for i in range(len(contours)):
            cnt = contours[i]
            if i != len(contours)-1:
                cnt2 = contours[i+1]
                x2, y2, w2, h2 = cv2.boundingRect(cnt2)
                rect_area2 = w2 * h2  # area size
            x, y, w, h = cv2.boundingRect(cnt)
            rect_area = w * h  # area size
            aspect_ratio = float(w) / h  # ratio = width/height
            if (aspect_ratio >= 0.2) and (aspect_ratio <= 1.0) and (rect_area >= 100) and (rect_area <= 200):
                if (0 <= abs(rect_area - rect_area2)) and (abs(rect_area - rect_area2) <= 20):
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
                    box.append(cv2.boundingRect(cnt))

        for i in range(len(box)):  # Buble Sort on python
            for j in range(len(box) - (i + 1)):
                if box[j][0] > box[j + 1][0]:
                    temp = box[j]
                    box[j] = box[j + 1]
                    box[j + 1] = temp
        cv2.imwrite('box.jpg', img)
        return 1

recogtest = Recognition()
result = recogtest.ExtractNumber()