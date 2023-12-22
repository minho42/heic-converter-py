import fire
from PIL import Image
from pillow_heif import register_heif_opener
from pathlib import Path


def heic_converter(filename):
    register_heif_opener()
    img = Image.open(filename)
    img2 = (
        Path(Path(filename).resolve().parent / Path(filename).stem).as_posix() + ".jpg"
    )
    img.save(img2)


if __name__ == "__main__":
    fire.Fire(heic_converter)
