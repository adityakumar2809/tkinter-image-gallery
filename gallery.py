import tkinter
from PIL import Image, ImageTk


def tkinterSetup(title='Untitled', icon_path='images/icon.ico'):
    root = tkinter.Tk()
    root.title(title)
    root.iconbitmap(icon_path)
    return root


def createQuitCommandButton(root, text='Exit Program'):
    my_button = tkinter.Button(
        master=root,
        text=text,
        command=root.quit
    )
    return my_button


def createImage(path='images/image1.jfif'):
    img = ImageTk.PhotoImage(
        Image.open(path)
    )
    return img


def createLabelWithImage(root, img):
    my_label = tkinter.Label(
        master=root,
        image=img
    )
    return my_label


def main():

    running_status = {
        'icon': True
    }

    # ICONS
    if running_status['icon']:
        root = tkinterSetup(title='Icon Window')

        quit_button = createQuitCommandButton(root)
        quit_button.pack()

        img_list = [createImage(f'images/image{counter}.jfif')
                    for counter in range(1, 6)]

        root.mainloop()


if __name__ == "__main__":
    main()
