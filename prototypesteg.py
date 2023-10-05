from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import os

class SteganographyApp:

    output_image_size = 0

    def __init__(self, root):
        self.root = root
        self.root.title('Image Steganography')
        self.root.geometry('500x600')
        self.root.configure(bg='black')
        self.root.resizable(width=False, height=False)
        self.initialize_ui()

    def initialize_ui(self):
        main_frame = Frame(self.root, bg='black')
        main_frame.pack(fill=BOTH, expand=True)

        title_label = Label(main_frame, text='Image Steganography', font=('Courier', 20), fg='white', bg='black')
        title_label.pack(pady=10)

        encode_button = self.create_button(main_frame, 'Encode', self.frame1_encode)
        decode_button = self.create_button(main_frame, 'Decode', self.frame1_decode)

        encode_button.pack(pady=20)
        decode_button.pack()

    def create_button(self, parent, text, command):
        button = Button(parent, text=text, command=command, font=('Courier', 14), bg='white')
        button['borderwidth'] = 2
        button['relief'] = 'solid'
        return button

    def home(self, frame):
        frame.destroy()
        self.initialize_ui()

    def frame1_decode(self):
        self.root.withdraw()  # Hide the main window
        d_f2 = Toplevel()
        d_f2.title('Decode Image')
        d_f2.geometry('400x300')
        d_f2.configure(bg='black')
        label_art = Label(d_f2, text='٩(^‿^)۶', font=('Courier', 40), fg='white', bg='black')
        label_art.pack(pady=50)

        l1 = Label(d_f2, text='Select Image with Hidden Text:', font=('Courier', 14), fg='white', bg='black')
        l1.pack()

        bws_button = self.create_button(d_f2, 'Select', self.frame2_decode)
        back_button = self.create_button(d_f2, 'Cancel', lambda: self.home(d_f2))

        bws_button.pack()
        back_button.pack(pady=15)

    def frame2_decode(self):
        myfile = tkinter.filedialog.askopenfilename(
            filetypes=[('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
            return

        myimg = Image.open(myfile, 'r')
        myimage = myimg.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)

        d_f3 = Toplevel()
        d_f3.title('Decoded Image')
        d_f3.geometry('500x400')
        d_f3.configure(bg='black')

        l4 = Label(d_f3, text='Selected Image:', font=('Courier', 16), fg='white', bg='black')
        l4.pack()

        panel = Label(d_f3, image=img)
        panel.image = img
        panel.pack()

        hidden_data = self.decode(myimg)

        l2 = Label(d_f3, text='Hidden Data:', font=('Courier', 16), fg='white', bg='black')
        l2.pack(pady=10)

        text_area = Text(d_f3, width=50, height=10)
        text_area.insert(INSERT, hidden_data)
        text_area.configure(state='disabled')
        text_area.pack()

        back_button = self.create_button(d_f3, 'Cancel', lambda: self.page3(d_f3))
        back_button.pack(pady=15)

        show_info = self.create_button(d_f3, 'More Info', self.info)
        show_info.pack()

    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())

        while True:
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data

    def frame1_encode(self):
        self.root.withdraw()  # Hide the main window
        f2 = Toplevel()
        f2.title('Encode Image')
        f2.geometry('400x300')
        f2.configure(bg='black')
        label_art = Label(f2, text='\'\(°Ω°)/\'', font=('Courier', 40), fg='white', bg='black')
        label_art.pack(pady=50)

        l1 = Label(f2, text='Select the Image in which you want to hide text:', font=('Courier', 14), fg='white',
                   bg='black')
        l1.pack()

        bws_button = self.create_button(f2, 'Select', self.frame2_encode)
        back_button = self.create_button(f2, 'Cancel', lambda: self.home(f2))

        bws_button.pack()
        back_button.pack(pady=15)

    def frame2_encode(self):
        myfile = tkinter.filedialog.askopenfilename(
            filetypes=[('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
            return

        myimg = Image.open(myfile)
        myimage = myimg.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)

        ep = Toplevel()
        ep.title('Encoded Image')
        ep.geometry('500x500')
        ep.configure(bg='black')

        l3 = Label(ep, text='Selected Image', font=('Courier', 16), fg='white', bg='black')
        l3.pack()

        panel = Label(ep, image=img)
        panel.image = img
        self.output_image_size = os.stat(myfile)
        self.o_image_w, self.o_image_h = myimg.size
        panel.pack()

        l2 = Label(ep, text='Enter the message:', font=('Courier', 16), fg='white', bg='black')
        l2.pack(pady=15)

        text_area = Text(ep, width=50, height=10)
        text_area.pack()

        encode_button = self.create_button(ep, 'Encode', lambda: [self.enc_fun(text_area, myimg), self.home(ep)])
        encode_button.pack(pady=15)

    def info(self):
        try:
            info_str = 'Original Image Info:\nSize: {:.2f} MB\nWidth: {}\nHeight: {}\n\n' \
                       'Decoded Image Info:\nSize: {:.2f} MB\nWidth: {} Height: {}'.format(
                           self.output_image_size.st_size / (1024 * 1024),
                           self.o_image_w, self.o_image_h,
                           self.d_image_size / (1024 * 1024),
                           self.d_image_w, self.d_image_h)
            messagebox.showinfo('Info', info_str)
        except:
            messagebox.showinfo('Info', 'Unable to get the information')

    def gen_data(self, data):
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def mod_pix(self, pix, data):
        datalist = self.gen_data(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            # Extracting 3 pixels at a time
            pixels = [value for value in imdata.__next__()[:3] +
                      imdata.__next__()[:3] +
                      imdata.__next__()[:3]]
            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(8):
                if (datalist[i][j] == '0') and (pixels[j] % 2 != 0):
                    if (pixels[j] % 2 != 0):
                        pixels[j] -= 1
                elif (datalist[i][j] == '1') and (pixels[j] % 2 == 0):
                    pixels[j] -= 1
            # Eighth pixel of every set tells
            # whether to stop or read further.
            # 0 means keep reading; 1 means the
            # message is over.
            if (i == lendata - 1):
                if (pixels[-1] % 2 == 0):
                    pixels[-1] -= 1
            else:
                if (pixels[-1] % 2 != 0):
                    pixels[-1] -= 1

            pixels = tuple(pixels)
            yield pixels[0:3]
            yield pixels[3:6]
            yield pixels[6:9]

    def encode_enc(self, newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.mod_pix(newimg.getdata(), data):
            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self, text_area, myimg):
        data = text_area.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert", "Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            my_file = BytesIO()
            temp = os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=[('png', '*.png')],
                                                            defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w, self.d_image_h = newimg.size
            messagebox.showinfo("Success",
                                "Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")

    def page3(self, frame):
        frame.destroy()
        self.initialize_ui()


if __name__ == "__main__":
    root = Tk()
    app = SteganographyApp(root)
    root.mainloop()
