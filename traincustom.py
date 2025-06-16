import torch
from ultralytics import YOLO

torch.manual_seed(42)


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    model_cfg = r'C:\...\yolo11-CSLA.yaml'  # set a path here
    model = YOLO(model_cfg)
    model.to(device)

    data_cfg = r'C:\...\dataset.yaml'  # set a path here

    model.train(
        data=data_cfg,
        epochs=200,
        imgsz=224,
        batch=32
    )  # set your params


if __name__ == '__main__':
    main()
