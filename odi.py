# !/usr/bin/python
import os
import imghdr

IMAGE_JPEG = 'jpeg'
IMAGE_PNG = 'png'


def scan_folder(input, output):
    ''' Recorre un directorio y retorna la lista de todas las imágenes '''
    _files = []

    for root, dirs, files in os.walk(input):
        for name in files:
            print(os.path.join(root, name))
            _files.append(os.path.join(root, name))

        for name in dirs:
            _dir = os.path.join(root, name)
            print(os.path.join(root, name))
            recreate_output(input, output, _dir)


    for _file in _files:
        optimize_image(_file, input, output)


def recreate_output(input, output, path):
    ''' Recrea la estructura de los directorios de entrada en el directorio de salida '''
    new_path = path.replace(input, output)

    if not os.path.exists(new_path):
        os.makedirs(new_path)


def optimize_image(img, input, output):
    ''' Optimiza una imagen '''
    image_type = imghdr.what(img)
    if image_type == 'jpeg':
        pass
    elif image_type == 'png':
        optimize_png(img, input, output)


def optimize_png(input_png, input_folder, output_folder):
    ''' Optimiza un archivo PNG '''
    output_png = input_png.replace(input_folder, output_folder)

    '''
    optimpng_command = 'optipng -o7 -strip all -dir "{}" "{}"'.format(
        os.path.dirname(output_png),
        input_png
    )

    print(optimpng_command)
    os.system(optimpng_command)
    '''

    pngquant_command = 'pngquant --quality=75-90 -o"{}" "{}"'.format(
        output_png,
        input_png
    )

    print(pngquant_command)
    os.system(pngquant_command)


if __name__ == '__main__':
    INPUT_FOLDER = 'input'
    OUTPUT_FOLDER = 'output'

    scan_folder(INPUT_FOLDER, OUTPUT_FOLDER)
