import cv2

# Создаем объект VideoCapture для доступа к веб-камере
cap = cv2.VideoCapture(0)  # 0 - индекс веб-камеры (может отличаться в зависимости от системы)

# Проверяем, успешно ли открыта веб-камера
if not cap.isOpened():
    print("Не удалось открыть веб-камеру")
    exit()

# Читаем видеопоток кадр за кадром и отображаем его
while True:
    # Читаем текущий кадр из видеопотока
    ret, frame = cap.read()

    # Если кадр считывается успешно
    if ret:
        # Отображаем кадр
        cv2.imshow("Webcam", frame)

    # Прерываем цикл, если нажата клавиша 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()