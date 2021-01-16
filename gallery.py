import tkinter
from PIL import Image, ImageTk


global current_image_index, max_image_index, img_label_list, left_button,\
       right_button, status_label
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


def createDirectionCommandButton(root, text, direction, state=tkinter.NORMAL):
    my_button = tkinter.Button(
        master=root,
        text=text,
        command=lambda: moveInADirection(root, direction),
        state=state
    )
    return my_button


def moveInADirection(rooot, direction):
    global current_image_index, max_image_index, img_label_list, left_button,\
           right_button

    img_label_list[current_image_index].grid_forget()

    if direction == 'left':
        current_image_index -= 1
    elif direction == 'right':
        current_image_index += 1

    if current_image_index <= 0:
        current_image_index = 0
        left_button.config(state=tkinter.DISABLED)
    elif current_image_index >= max_image_index:
        current_image_index = max_image_index
        right_button.config(state=tkinter.DISABLED)
    else:
        left_button.config(state=tkinter.NORMAL)
        right_button.config(state=tkinter.NORMAL)

    img_label_list[current_image_index].grid(row=0, column=0, columnspan=3)




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


def createStatusLabel(root):
    global status_label
    text = f'Image { current_image_index + 1 } of { max_image_index + 1 }'
    status_label = tkinter.Label(
        master=root,
        text=text
    )


def main():

    global max_image_index, img_label_list, left_button, right_button,\
           status_label

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

        max_image_index = len(img_list) - 1

        img_label_list[0].grid(row=0, column=0, columnspan=3)

        quit_button = createQuitCommandButton(root)
        left_button = createDirectionCommandButton(
            root,
            text='<<',
            direction='left',
            state=tkinter.DISABLED
        )
        right_button = createDirectionCommandButton(
            root,
            text='>>',
            direction='right'
        )
        status_label = createStatusLabel(root)
        left_button.grid(row=1, column=0)
        status_label.grid(row=1, column=1)
        right_button.grid(row=1, column=2)
        quit_button.grid(row=2, column=1)

        root.mainloop()


if __name__ == "__main__":
    main()
