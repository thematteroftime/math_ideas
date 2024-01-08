import time
import tkinter
import random
from tkinter import Canvas
from PIL import Image, ImageTk, ImageSequence


def animate(frame, canvas_gif, root_gif):
    frame = frame.resize((800, 800))
    pic = ImageTk.PhotoImage(frame)
    canvas_gif.create_image((400, 400), image=pic)

    root_gif.update_idletasks()
    root_gif.update()

    return


def animate_gif(root_gif):
    canvas_gif = Canvas(root_gif, width=800, height=800, bg='black')
    canvas_gif.pack()
    index = random.randint(1, 1)
    img = Image.open(f".\\picture_package\\picture_cal{index}.gif")  # GIF图片流的迭代器
    frames = ImageSequence.Iterator(img)  # frame就是gif的每一帧，转换一下格式就能显示了

    for frame in frames:
        animate(frame, canvas_gif, root_gif)
        time.sleep(0.05)  # 控制动画速度

    root_gif.destroy()

    return


def picture_jpg(root_jpg):
    root_jpg.minsize(500, 500)
    root_jpg.maxsize(2160, 1440)
    root_jpg.title('dummy')

    index = random.randint(1, 4)
    img = Image.open(f".\picture_package\picture{index}.jpg")
    img = img.resize((1000, 800))
    photo = ImageTk.PhotoImage(img)

    label_pic = tkinter.Label(root_jpg, image=photo)
    label_pic.pack(fill=tkinter.BOTH, expand=True)

    root_jpg.mainloop()

    return


def run_pictrue(original_root, user_chose):
    if user_chose == []:
        picture_jpg(original_root)
    elif user_chose == ['0']:
        animate_gif(original_root)

    return
