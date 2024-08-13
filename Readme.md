# Приложение для сбора статистики по количеству людей в комнатах.

**Используя камеру устройства и [DETR модель ResNet-101](https://huggingface.co/facebook/detr-resnet-101)
приложение находит людей в области зрения камеры и считает их количество.**

## Данные отправляются на сервер в формате:
```
{
    "auth_key": auth_key from .env,
    "room": room_name from .env,
    "count": count people in room,
    "date": date in format '%m/%d/%Y, %H:%M:%S'
    "image": im_b64
}
```

## Развертывание:
```shell
sudo docker pull andrei1121212/sberlab_count_assistant:manifest
```
* установить переменные среды из .env.local.example
