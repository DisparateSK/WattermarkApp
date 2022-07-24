import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk, ImageFont, ImageDraw


class App:
    def __init__(self, root):
        # setting title
        root.title("Watermark App")
        # setting window size
        width = 810
        height = 704
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        upload_button = tk.Button(root)
        upload_button["bg"] = "#00ced1"
        upload_button["disabledforeground"] = "#00babd"
        ft = tkFont.Font(family='Times', size=14)
        upload_button["font"] = ft
        upload_button["fg"] = "#ffffff"
        upload_button["justify"] = "center"
        upload_button["text"] = "Upload photo"
        upload_button.place(x=300, y=460, width=193, height=50)
        upload_button["command"] = self.upload_command

        label1 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=23)
        label1["font"] = ft
        label1["fg"] = "#333333"
        label1["justify"] = "center"
        label1["text"] = "Add your watermark"
        label1.place(x=270, y=10, width=263, height=38)

        self.text_entry = tk.Entry(root)
        self.text_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.text_entry["font"] = ft
        self.text_entry["fg"] = "#333333"
        self.text_entry["justify"] = "center"
        self.text_entry["text"] = "Text"
        self.text_entry.place(x=60, y=550, width=160, height=40)

        apply_b = tk.Button(root)
        apply_b["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=14)
        apply_b["font"] = ft
        apply_b["fg"] = "#ffffff"
        apply_b["justify"] = "center"
        apply_b["text"] = "Apply"
        apply_b.place(x=230, y=600, width=160, height=50)
        apply_b["command"] = self.apply_command

        self.rotate_entry = tk.Entry(root)
        self.rotate_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.rotate_entry["font"] = ft
        self.rotate_entry["fg"] = "#333333"
        self.rotate_entry["justify"] = "center"
        self.rotate_entry["text"] = "20"
        self.rotate_entry.place(x=230, y=550, width=160, height=40)

        self.row_entry = tk.Entry(root)
        self.row_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.row_entry["font"] = ft
        self.row_entry["fg"] = "#333333"
        self.row_entry["justify"] = "center"
        self.row_entry["text"] = "2"
        self.row_entry.place(x=400, y=550, width=160, height=40)

        self.col_entry = tk.Entry(root)
        self.col_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.col_entry["font"] = ft
        self.col_entry["fg"] = "#333333"
        self.col_entry["justify"] = "center"
        self.col_entry["text"] = "5"
        self.col_entry.place(x=570, y=550, width=160, height=40)

        save_b = tk.Button(root)
        save_b["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=14)
        save_b["font"] = ft
        save_b["fg"] = "#ffffff"
        save_b["justify"] = "center"
        save_b["text"] = "Save"
        save_b.place(x=400, y=600, width=160, height=50)
        save_b["command"] = self.save_command

        text_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        text_label["font"] = ft
        text_label["fg"] = "#333333"
        text_label["justify"] = "center"
        text_label["text"] = "Text"
        text_label.place(x=90, y=520, width=99, height=30)

        rotate_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        rotate_label["font"] = ft
        rotate_label["fg"] = "#333333"
        rotate_label["justify"] = "center"
        rotate_label["text"] = "Rotate"
        rotate_label.place(x=280, y=520, width=70, height=25)

        rows_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        rows_label["font"] = ft
        rows_label["fg"] = "#333333"
        rows_label["justify"] = "center"
        rows_label["text"] = "Rows"
        rows_label.place(x=450, y=520, width=70, height=25)

        columns_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        columns_label["font"] = ft
        columns_label["fg"] = "#333333"
        columns_label["justify"] = "center"
        columns_label["text"] = "Columns"
        columns_label.place(x=610, y=520, width=70, height=25)

    def upload_command(self):
        global img2, img
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        img = Image.open(filename)
        width, height = img.size
        img_resized = img.resize((600, int(height / width * 600))) if int(height / width * 600) < 400 else img.resize(
            (int(width / height * 400), 400))  # new width & height
        img2 = ImageTk.PhotoImage(img_resized)
        b2 = tk.Button(root, image=img2)  # using Button
        b2.place(x=100, y=50, width=600, height=400)

    def apply_command(self):
        global img3
        width, height = img.size
        im_new = img.convert("RGBA")
        txt = Image.new("RGBA", img.size, (255, 255, 255, 0))
        font = ImageFont.truetype("arial.ttf", 65)
        d = ImageDraw.Draw(txt)
        text = self.text_entry.get()
        col = int(self.col_entry.get())
        row = int(self.row_entry.get())
        for i in range(0, img.width + 60, img.width // col):
            for j in range(-100, img.height + 350, img.height // row):
                d.text((i - 10, j - 10), text, fill=(200, 200, 200, 130), font=font)
        txt = txt.rotate(int(self.rotate_entry.get()))
        result = Image.alpha_composite(im_new, txt)
        img_resized = result.resize((600, int(height / width * 600))) if int(
            height / width * 600) < 400 else img.resize(
            (int(width / height * 400), 400))  # new width & height
        img3 = ImageTk.PhotoImage(img_resized)
        b2 = tk.Button(root, image=img3)  # using Button
        b2.place(x=100, y=50, width=600, height=400)

    def save_command(self):
        im_new = img.convert("RGBA")
        txt = Image.new("RGBA", img.size, (255, 255, 255, 0))
        font = ImageFont.truetype("arial.ttf", 65)
        d = ImageDraw.Draw(txt)
        text = self.text_entry.get()
        col = int(self.col_entry.get())
        row = int(self.row_entry.get())
        for i in range(0, img.width + 60, img.width // col):
            for j in range(-100, img.height + 350, img.height // row):
                d.text((i - 10, j - 10), text, fill=(200, 200, 200, 130), font=font)
        txt = txt.rotate(int(self.rotate_entry.get()))
        result = Image.alpha_composite(im_new, txt)

        save_here = askdirectory(initialdir='/', title='Select File')
        result.save(os.path.join(save_here, 'myData.jpg'), 'png')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
