from transformers import DetrImageProcessor, DetrForObjectDetection
from torchvision.utils import draw_bounding_boxes
from torchvision.io import read_image
import torchvision.transforms as tvt
from torchvision.io.image import ImageReadMode
from PIL import Image
import torch

processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-101")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-101")


def find_people(raw_shot_path):
    with Image.open(raw_shot_path).convert("RGB") as camera_image:
        inputs = processor(images=camera_image, return_tensors="pt")
        outputs = model(**inputs)
        target_sizes = torch.tensor([camera_image.size[::-1]])

        results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.8)[0]

        boxes = []
        for label, box in zip(results["labels"], results["boxes"]):
            if model.config.id2label[label.item()] == "person":
                boxes.append(box.tolist())

    return boxes


def make_bounds(boxes, bounded_path, raw_shot_path):
    count = len(boxes)
    if count > 0:
        tensor_image = read_image(raw_shot_path, ImageReadMode.RGB)
        boxes = torch.tensor(boxes, dtype=torch.float)
        tensor_result = draw_bounding_boxes(tensor_image, boxes, width=6, colors="green")

        bounded_image = tvt.ToPILImage()(tensor_result)
        bounded_image.save(bounded_path)
    else:
        with Image.open(raw_shot_path) as img:
            img.save(bounded_path)

    return count


def get_peoples_count_from_photo(raw_shot_path: str, bounded_path: str):
    boxes = find_people(raw_shot_path)
    count = make_bounds(boxes, bounded_path, raw_shot_path)

    return count
