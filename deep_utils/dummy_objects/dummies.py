from .dummy_framework import DummyObject
from ..utils.constants import Backends


class SITKUtils(metaclass=DummyObject):
    _backend = [Backends.SIMPLE_ITK]


class TFUtils(metaclass=DummyObject):
    _backend = [Backends.TENSORFLOW]


class QdrantUtils(metaclass=DummyObject):
    _backend = [Backends.QDRANT_CLIENT]


class DownloadUtils(metaclass=DummyObject):
    _backend = [Backends.REQUESTS]


class HaarcascadeCV2FaceDetector(metaclass=DummyObject):
    _backend = [Backends.CV2]


class CVUtils(metaclass=DummyObject):
    _backend = [Backends.CV2]


class ImageEditingGLIDE(metaclass=DummyObject):
    _backend = [Backends.TORCH, Backends.GLIDE_TEXT2IM]


class ImageEditingGLIDETypes(metaclass=DummyObject):
    _backend = [Backends.TORCH, Backends.GLIDE_TEXT2IM]


class Text2BoxVisualGroundingDino(metaclass=DummyObject):
    _backend = [Backends.TORCH, Backends.GROUNDINGDINO, Backends.PILLOW]


class MTCNNTFFaceDetector(metaclass=DummyObject):
    _backend = [Backends.TENSORFLOW, Backends.CV2]


class MTCNNTorchFaceDetector(metaclass=DummyObject):
    _backend = [Backends.TORCH, Backends.CV2]


class YOLOV5TorchObjectDetector(metaclass=DummyObject):
    _backend = [Backends.TORCH, Backends.CV2]


class YOLOV7TorchObjectDetector(metaclass=DummyObject):
    _backend = [Backends.TORCH, Backends.CV2]


class ColorRecognitionCNNTorchPrediction(metaclass=DummyObject):
    _backend = [Backends.TORCH, Backends.CV2]


class CRNNModelTorch(metaclass=DummyObject):
    _backend = [Backends.TORCH, Backends.CV2]


class CRNNInferenceTorch(metaclass=DummyObject):
    _backend = [Backends.TORCH, Backends.CV2]


class TensorboardTorch(metaclass=DummyObject):
    _backend = [Backends.TORCH]


class TorchUtils(metaclass=DummyObject):
    _backend = [Backends.TORCH]


class BlocksTorch(metaclass=DummyObject):
    _backend = [Backends.TORCH]


class ColorRecognitionCNNTorch(metaclass=DummyObject):
    _backend = [Backends.TORCH]


class MonaiChannelBasedContrastEnhancementD(metaclass=DummyObject):
    _backend = [Backends.MONAI, Backends.TORCH]


class BlipTorchImageCaption(metaclass=DummyObject):
    _backend = [Backends.TORCH,
                Backends.TORCHVISION,
                Backends.TIMM,
                Backends.TRANSFORMERS,
                Backends.FAIRSCALE
                ]


class ElasticsearchEngin(metaclass=DummyObject):
    _backend = [Backends.ELASTICSEARCH]


class VggFace2TorchFaceRecognition(metaclass=DummyObject):
    # ["torch", "cv2", "albumentations", "sklearn"]
    _backend = [Backends.TORCH, Backends.CV2, Backends.ALBUMENTATIONS, Backends.SCIKIT]

class UltralightTorchFaceDetector(metaclass=DummyObject):
    # ["torch", "cv2", "albumentations", "sklearn"]
    _backend = [Backends.TORCH, Backends.CV2, Backends.ALBUMENTATIONS, Backends.SCIKIT]
