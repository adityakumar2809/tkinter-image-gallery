import tkinter
from PIL import Image, ImageTk


global current_image_index, max_image_index
current_image_index = 0
max_image_index = 0


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


def createDirectionCommandButton(root, text, direction):
    my_button = tkinter.Button(
        master=root,
        text=text,
        command=lambda: moveInADirection(direction)
    )
    return my_button


def moveInADirection(direction):
    global current_image_index
    if direction == 'left':
        pass
    print(direction)


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

    global max_image_index

    running_status = {
        'icon': True
    }

    # ICONS
    if running_status['icon']:
        root = tkinterSetup(title='Icon Window')

        img_list = [createImage(f'images/image{counter}.jfif')
                    for counter in range(1, 6)]
        img_label_list = [createLabelWithImage(root, img_item)
                          for img_item in img_list]

        max_image_index = len(img_list)

        img_label_list[0].grid(row=0, column=0, columnspan=3)

        quit_button = createQuitCommandButton(root)
        left_button = createDirectionCommandButton(
            root,
            text='<<',
            direction='left'
        )
        right_button = createDirectionCommandButton(
            root,
            text='>>',
            direction='right'
        )
        left_button.grid(row=1, column=0)
        quit_button.grid(row=1, column=1)
        right_button.grid(row=1, column=2)

        root.mainloop()


if __name__ == "__main__":
    main()
