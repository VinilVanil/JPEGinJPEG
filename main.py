from PIL import Image, ImageDraw, ImageFont
import datetime

def date_now(x_date,y_date1, y_date2, y_date3, im):
    dt_obj = datetime.datetime.now()
    dt_string = dt_obj.strftime("%d.%m.%y")
    date = f"Дата   {str(dt_string)}"
    draw_text = ImageDraw.Draw(im)
    draw_text.text((x_date, y_date1), date, font=font, fill='#5d5d5d')
    draw_text.text((x_date, y_date2), date, font=font, fill='#5d5d5d')
    draw_text.text((x_date, y_date3), date, font=font, fill='#5d5d5d')


font = ImageFont.truetype(r'font\Calibri.ttf', size=46)
#put_pr = r'C:\Users\Work\PycharmProjects\JPEGinJPEG\\'

id = 9
if id == 1:
    x_id = 1560
    y_id = 858
    im = Image.open(r'jpg\1p.jpg')
    #даты на странице
    date = date_now(335, 1448, 2149, 2852, im)

    rezult_file = "rezult1.jpg"
elif id == 2:
    x_id = 1560
    y_id = 1670
    im = Image.open('rezult1.jpg')
    rezult_file = "rezult1.jpg"
elif id == 3:
    x_id = 1575
    y_id = 2373
    im = Image.open('rezult1.jpg')
    rezult_file = "rezult1.jpg"
elif id == 4:
    x_id = 1700
    y_id = 345
    im = Image.open(r'jpg\1p.jpg')
    #даты на странице
    date = date_now(360, 826, 1528, 2928, im)
    rezult_file = "rezult2.jpg"
elif id == 5:
    x_id = 1700
    y_id = 1047
    im = Image.open(r'rezult2.jpg')
    rezult_file = "rezult2.jpg"
elif id == 6:
    x_id = 1700
    y_id = 1748
    im = Image.open(r'rezult2.jpg')
    rezult_file = "rezult2.jpg"
elif id == 7:
    x_id = 1700
    y_id = 2449
    im = Image.open(r'rezult2.jpg')
    rezult_file = "rezult2.jpg"
elif id == 8:
    x_id = 1700
    y_id = 345
    im = Image.open(r'jpg\3p.jpg')
    date = date_now(350, 835, 1535, 9000, im)
    rezult_file = "rezult3.jpg"
elif id == 9:
    x_id = 1700
    y_id = 1055
    im = Image.open(r'rezult3.jpg')
    rezult_file = "rezult3.jpg"

draw_text = ImageDraw.Draw(im)
draw_text.text((x_id, y_id),'9002509004180', font=font, fill='#5d5d5d')
#im.show()





put = rezult_file
im.save(put)





















