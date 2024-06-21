from ultraopt import YOLO

model = YOLO('yolov8x')

model.predict('input_videos/image.jpg', sv=True)