import array

width, height = 400, 400
with open('in.bmp', 'rb') as in_pic, open('out.bmp', 'wb') as out_pic:
    head = in_pic.read(54)  # первые 54 байта - заголовок
    b = [[[i for i in in_pic.read(3)] for _ in range(height)] for _ in range(width)]
    for i in b:
        print(i)

    # out_pic.write(head)
    # for i in range(400):
    #     for j in range(400):
    #         for k in range(400):
    #             out_pic.write(bytes(a[i][j][k]))
