import cv2
import supervision as sv
import torch
def main():
    model = torch.hub.load('ultralytics/yolov5', "custom", path='../ml_models/paddletracker', force_reload=True)
