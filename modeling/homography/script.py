from tkinter import *
import cv2
import numpy as np
import io
from PIL import Image, ImageTk


def click_first_button(path):
    new_window = Toplevel()
    image = PhotoImage(file="C:\\Users\\user\\PycharmProjects\\image_editor\\images\\img.png")
    img = cv2.imread("C:\\Users\\user\\PycharmProjects\\image_editor\\images\\img.png", 0)
    height, width = img.shape[:2]
    label = Label(new_window, image=image)
    label.pack()
    label.place(x=0, y=0)
    new_window.geometry(str(width*2)+"x"+str(height))

    im_src = cv2.imread("C:\\Users\\user\\PycharmProjects\\image_editor\\images\\img.png")

    pts_src = np.array([[100, 200], [400, 200], [100, 50], [400, 50]])
    im_dst = cv2.imread("C:\\Users\\user\\PycharmProjects\\image_editor\\images\\img.png")
    pts_dst = np.array([[150, 150], [430, 170], [130, 20], [440, 10]])
    h, status = cv2.findHomography(pts_src, pts_dst)

    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))

    image_ = np.array(im_out)
    image__ = ImageTk.PhotoImage(image=Image.fromarray(image_))

    canvas = Label(new_window, image=image__)
    canvas.pack()
    canvas.place(x=width, y=0)

    new_window.mainloop()


def click_second_button(first_path, second_path):
    im1 = cv2.imread('img.png')
    im2 = cv2.imread('for_test.png')

    img1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(50)

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)

    matches = matcher.match(des1, des2, None)

    matches = sorted(matches, key=lambda x: x.distance)

    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = kp1[match.queryIdx].pt
        points2[i, :] = kp2[match.trainIdx].pt

    h = cv2.findHomography(points1, points2, cv2.RANSAC)[0]

    height, width, channels = im2.shape

    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None)

    print(h)

    cv2.imshow('Keypoint matches', img3)
    cv2.imshow('Registered image', im1Reg)
    cv2.waitKey(0)


if __name__ == '__main__':
    window = Tk()
    window.geometry("680x400")
    window.title("image editor")

    icon = PhotoImage(file="C:\\Users\\user\\PycharmProjects\\image_editor\\images\\img.png")
    window.iconphoto(True, icon)

    background_image = PhotoImage(file="C:\\Users\\user\\PycharmProjects\\image_editor\\images\\img.png")
    background_label = Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    entry_first = Entry(window)
    entry_first.pack()

    entry_first.insert(0, "path to first image")
    entry_first.place(x=22, y=115)

    entry_second = Entry(window)
    entry_second.pack()

    entry_second.insert(0, "path to second image")
    entry_second.place(x=22, y=135)

    entry = Entry(window, width=14)
    entry.pack()

    entry.insert(0, "path")
    entry.place(x=440, y=75)

    button_first = Button(window, text="rotate image", command=lambda: click_first_button(entry.get()), font=("Comic Sans",10), fg="#00FF00", bg="black")

    button_first.pack()

    button_first.place(x=440, y=50)

    button_second = Button(window, text="get homography", command=lambda: click_second_button(entry_first.get(), entry_second.get()), font=("Comic Sans", 10), fg="#00FF00", bg="black")

    button_second.pack()

    button_second.place(x=22, y=155)

    window.mainloop()
