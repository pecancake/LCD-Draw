from PIL import Image

def translate_pixel(img, x, y):
    if img.getpixel((x,y)) == (255, 0, 0, 255):
        return '1'
    else:
        return '0'

def code_to_char(code):
    char = ""
    for y in range(5):
        for x in range(5):
            if code[y*5+x] == '1':
                char += "#"
            else:
                char += " "
        char+="\n"
    print(char)

def traverse(img, i, k):
    code = ''
    for y in range(i, i+5):
        for x in range(k, k+5):
            code += translate_pixel(img, x, y)
    return code

def read_font_file(img):
    letters = {' ': '0'*25}
    alp = (c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890<>-^/~')

    for i in range(0, img.size[1], 5):
        for k in range(0, img.size[0], 5):
            code = traverse(img, i, k)
            letters[next(alp)] = code

    return letters

imgfile = Image.open('font.bmp')
ProtoFont = read_font_file(imgfile)
imgfile.close()
