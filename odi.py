#!/usr/bin/python3

import os
import imghdr
import argparse


def main():
    ''' Recorre un directorio, localiza las imágenes y las optimiza '''

    args = arguments()

    print(args)

    _files = []

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    for root, dirs, files in os.walk(args.input):
        for name in files:
            print(os.path.join(root, name))
            _files.append(os.path.join(root, name))

        for name in dirs:
            _dir = os.path.join(root, name)
            print(os.path.join(root, name))
            recreate_output(args.input, args.output, _dir)

    for _file in _files:
        optimize_image(_file, args.input, args.output)


def arguments():
    ''' Interpreta las opciones ingresadas por la línea de comandos '''
    parser = argparse.ArgumentParser(description='Optimiza las imágenes (jpg, png) del directorio indicado')

    parser.add_argument('input', default='input/', nargs='?', help='Directorio que contiene los archivos de entrada, '
                                                              'por defecto procesa el directorio llamado "input"')
    parser.add_argument('output', default='output/', nargs='?',
                        help='Directorio destino de las imágenes optimizadas, '
                             'por defecto genera la salida en el directorio "output"')

    return parser.parse_args()


def recreate_output(input, output, path):
    ''' Recrea la estructura de los directorios de entrada en el directorio de salida '''
    new_path = path.replace(input, output)

    if not os.path.exists(new_path):
        os.makedirs(new_path)


def optimize_image(img, input, output):
    ''' Optimiza una imagen '''
    image_type = imghdr.what(img)
    if image_type == 'jpeg':
        optimize_jpg(img, input, output)

    elif image_type == 'png':
        optimize_png(img, input, output)


def optimize_jpg(input_jpg, input_folder, output_folder):
    ''' Optimiza un archivo JPG '''
    output_jpg = input_jpg.replace(input_folder, output_folder)

    cjpeg_command = 'convert "{}" pnm:- | cjpeg -optimize -baseline -quality 75 > "{}"'.format(
        input_jpg,
        output_jpg
    )

    print(cjpeg_command)
    os.system(cjpeg_command)


def optimize_png(input_png, input_folder, output_folder):
    ''' Optimiza un archivo PNG '''
    output_png = input_png.replace(input_folder, output_folder)

    pngquant_command = 'pngquant --quality=75-90 -o"{}" "{}"'.format(
        output_png,
        input_png
    )

    print(pngquant_command)
    os.system(pngquant_command)


if __name__ == '__main__':
    main()
