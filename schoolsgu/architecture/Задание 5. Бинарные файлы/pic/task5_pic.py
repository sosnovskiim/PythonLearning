import array

with open('in.bmp', 'rb') as in_pic, open('out.bmp', 'wb') as out_pic:
    head = in_pic.read(54)  # первые 54 байта - заголовок
    a = array.array('B', in_pic.read())
    # здесь можно преобразовать изображение в a
    out_pic.write(head)
    out_pic.write(a.tobytes())
