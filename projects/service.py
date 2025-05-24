from PIL import Image as PilImage
from django.core.files.base import ContentFile
import io


def optimize_image(image_field, max_size=(1920, 1080), format='WEBP', quality=85):
    if not image_field:
        return None

    img = PilImage.open(image_field)

    if img.mode == 'RGBA':
        img = img.convert('RGB')

    img.thumbnail(max_size, PilImage.LANCZOS)

    output = io.BytesIO()
    img.save(output, format=format, quality=quality, optimize=True)
    output.seek(0)

    extension = format.lower()
    filename = image_field.name.rsplit('.', 1)[0] + f'.{extension}'

    return ContentFile(output.read(), name=filename)