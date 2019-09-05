from tkinter import *
from PIL import Image, ImageTk
import pickle as p


def array_to_image(file_path):
    with open(file_path, 'rb') as f:
        image_array = p.load(f)
    image_array = image_array.reshape(3, 180, 180)
    r = Image.fromarray(image_array[0]).convert('L')
    g = Image.fromarray(image_array[1]).convert('L')
    b = Image.fromarray(image_array[2]).convert('L')
    image = Image.merge('RGB', (r, g, b))
    return image


# popup windows
class ChildWindow(Toplevel):
    images = [[array_to_image('./icon/%d.bin' % i) for i in range(1, 5)],
              [array_to_image('./icon/%d.bin' % -1)]]
    labels = [['不对不对！', '再给一次机会', '你好笨哦', '最后一次'], ['不会有的别想了！', '哈哈哈哈承认了吧', '略略略略略']]

    def __init__(self, parent=None):
        super().__init__()
        self.title('不会吗？')
        self.parent = parent
        self.geometry('400x300')
        self.create_widgets()

    def create_widgets(self):
        if ChildWindow.labels[0]:
            # file_num = ChildWindow.images[0][0]
            # ChildWindow.images[0].remove(file_num)
            # load = Image.open('%d.jpg' % file_num).resize((180, 180))
            load = ChildWindow.images[0][0]
            ChildWindow.images[0].pop(0)
            render = ImageTk.PhotoImage(load)
            self.img = Label(self, image=render, width='100', height='100')
            self.img.image = render
            self.img.pack(expand=YES, fill=BOTH)
            label = ChildWindow.labels[0][0]
            ChildWindow.labels[0].remove(label)
            self.label = Label(self, text=label, font=('微软雅黑', 16))
            self.label.pack(pady=20, fill=X, padx=10)
            self.yes_button = Button(self, text='不会', width='10', height='1', command=self.yes_command)
            self.yes_button.pack(side='left', expand=True, padx=10, pady=10)
            self.no_button = Button(self, text='会', width='10', height='1', command=self.no_command)
            self.no_button.pack(side='right', expand=True, padx=10, pady=10)
        else:
            # load = Image.open('-1.jpg').resize((180, 180))
            load = ChildWindow.images[1][0]
            render = ImageTk.PhotoImage(load)
            self.img = Label(self, image=render, width='100', height='100')
            self.img.image = render
            self.img.pack(expand=YES, fill=BOTH)
            self.label = Label(self, text=ChildWindow.labels[1][0], font=('微软雅黑', 24))
            self.label.pack(pady=30, fill=X, padx=10)
            self.after(700, self.destroy)

    def yes_command(self):
        self.yes_button.destroy()
        self.no_button.destroy()
        self.img.destroy()
        self.label.destroy()
        self.label = Label(self, text=ChildWindow.labels[1][1], font=('微软雅黑', 16))
        self.label.pack(pady=50, fill=X, padx=10)
        self.label2 = Label(self, text=ChildWindow.labels[1][2], font=('幼圆', 10))
        self.label2.pack(pady=50, padx=30, side=RIGHT)
        self.after(1200, self.destroy)
        return

    def no_command(self):
        no_window = ChildWindow(self)
        self.wait_window(no_window)
        self.destroy()
        return


# main window
class APP(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(expand=True, fill=BOTH)
        w, h = 400, 300
        self.master.geometry('%dx%d' % (w, h))
        self.create_widgets()

    def create_widgets(self):
        load = array_to_image('./icon/start.bin')
        # load = Image.open('start.jpg').resize((180, 180))
        render = ImageTk.PhotoImage(load)
        self.img = Label(self, image=render, width='100', height='100')
        self.img.image = render
        self.img.pack(expand=YES, fill=BOTH)
        self.label = Label(self, text='cqq会有男朋友吗？', font=('微软雅黑', 16))
        self.label.pack(pady=20, fill=X, padx=10)
        self.yes_button = Button(self, text='不会', width='10', height='1', command=self.yes_command)
        self.yes_button.pack(side='left', expand=True, padx=10, pady=10)
        self.no_button = Button(self, text='会', width='10', height='1', command=self.no_command)
        self.no_button.pack(side='right', expand=True, padx=10, pady=10)

    def yes_command(self):
        self.yes_button.destroy()
        self.no_button.destroy()
        # load = Image.open('end.jpg').resize((180, 180))
        load =array_to_image('./icon/end.bin')
        render = ImageTk.PhotoImage(load)
        self.img.destroy()
        self.img = Label(self, image=render, width='100', height='100')
        self.img.image = render
        self.img.pack(expand=YES, fill=BOTH)

        self.label.destroy()
        self.label = Label(self, text='真乖 ~', font=('微软雅黑', 16))
        self.label.pack(pady=30, fill=X, padx=10)
        self.after(1500, self.quit)
        return

    def no_command(self):
        no_window = ChildWindow(self)
        self.wait_window(no_window)
        self.quit()
        return


if __name__ == '__main__':
    app = APP()
    app.master.title('嘿嘿嘿')
    app.mainloop()
