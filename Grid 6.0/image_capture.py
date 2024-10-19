import cv2

def capture_image(camera_id=0):
    cap = cv2.VideoCapture(camera_id)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('product_image.jpg', frame)
    cap.release()

if __name__ == "__main__":
    capture_image()

