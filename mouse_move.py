# 실시간 마우스 위치 추적
import tkinter as tk

mouse_x =0
mouse_y =0
mouse_c =0

#마우스 포인터 이동 시 실행할 함수
def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

#마우스 버튼 클릭 시 실행할 함수
def mouse_press(e):
    global mouse_c
    mouse_c = 1

#마우스 버튼 클릭 후 해제 시 실행할 함수
def mouse_release(e):
    global mouse_c
    mouse_c = 0

#실시간 처리 수행 함수
def game_main():
    fnt = ("Times New Roman", 30)
    txt = f"mouse({mouse_x},{mouse_y}) {mouse_c}"
    canvas.delete("TEST")
    canvas.create_text(456, 384, text=txt, fill="black", font=fnt, tag="TEST")
    root.after(100, game_main)


root = tk.Tk()
root.title("마우스 입력")
root.resizable(0,0)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<ButtonRelease>", mouse_release)
canvas = tk.Canvas(root, width=912, height=768)
canvas.pack()
game_main()
root.mainloop()
