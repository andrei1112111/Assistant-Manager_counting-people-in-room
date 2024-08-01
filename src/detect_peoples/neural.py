from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import torch

from src.logger import logger

processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-101",
                                               trust_remote_code=True, low_cpu_mem_usage=True)
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-101",
                                               trust_remote_code=True, low_cpu_mem_usage=True, )


def get_peoples_count_from_photo(raw_shot_path: str) -> int:
    logger.info("Start Photo Processing...")
    with Image.open(raw_shot_path).convert("RGB") as camera_image:
        inputs = processor(images=camera_image, return_tensors="pt")
        outputs = model(**inputs)

        logger.info("tensoring...")
        target_sizes = torch.tensor([camera_image.size[::-1]])

        logger.info("clearing cache...")
        torch.cuda.empty_cache()

    del inputs

    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.8)[0]

    del outputs, target_sizes

    logger.info("Photo Processed!")

    people_count = 0
    for label, box in zip(results["labels"], results["boxes"]):
        if model.config.id2label[label.item()] == "person":
            people_count += 1

    del results

    return people_count
