import tkinter


def btn_click():
    print('ボタンがクリックされました')

tki = tkinter.Tk()
tki.geometry('300x200')
tki.title('ボタンイベントの検証')

btn = tkinter.Button(tki, text='計算', command=btn_click)
btn.place(x=140, y=170)
tki.mainloop()
