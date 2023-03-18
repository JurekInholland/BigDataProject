import cv2
from ultralytics import YOLO

import supervision as sv


def main():
    model = YOLO()
    model.weights = 'paddletracker.pt'

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=1,
        text_scale=0.5,
    )

    for result in model.track(source=0, show=True):
        frame = result.orig_img
        detection = sv.Detections.from_yolov8(result)
        detection.tracker_id = result.boxes.id.cpu().numpy().astype(int)

        labels = [
            f"(id: {tracker_id}, {model.model.names[class_id]}, {confidence:.2f})"
            for _, confidence, class_id, tracker_id in detection
        ]

        frame = box_annotator.annotate(scene=frame, detections=detection, labels=labels)

        cv2.imshow('frame', frame)

        if cv2.waitKey(30) == 27:
            break


if __name__ == '__main__':
    main()