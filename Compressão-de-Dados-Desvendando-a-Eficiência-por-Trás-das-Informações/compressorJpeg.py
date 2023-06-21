from PIL import Image


def compress_image_jpeg(input_image, output_image, quality=75):
    with Image.open(input_image) as image:
        image.save(output_image, format="JPEG", optimize=True, quality=quality)


# Exemplo de uso:
input_image = "imagem_original.jpg"
output_image = "imagem_comprimida.jpg"
compress_image_jpeg(input_image, output_image, quality=50)
