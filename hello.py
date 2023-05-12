import numpy as np

N = np.array([['.', '.', '.'],
              ['.', '.', '.'],
              ['.', '.', '.']])

num = input('数字を入力してください')
num_int = int(num)

if 0 == num_int:
    print(N)
elif 1 == num_int:
    N[:1, :1] = "#"
    print(N)
elif 2 == num_int:
    N[:1, :2] = "#"
    print(N)
elif 3 == num_int:
    N[:1, :3] = "#"
    print(N)
elif 4 == num_int:
    N[:1, :3] = "#"
    N[:2, :1] = "#"
    print(N)
elif 5 == num_int:
    N[:1, :3] = "#"
    N[:2, :2] = "#"
    print(N)
elif 6 == num_int:
    N[:1, :3] = "#"
    N[:2, :3] = "#"
    print(N)
elif 7 == num_int:
    N[:1, :3] = "#"
    N[:2, :3] = "#"
    N[:3, :1] = "#"
    print(N)
elif 8 == num_int:
    N[:1, :3] = "#"
    N[:2, :3] = "#"
    N[:3, :2] = "#"
    print(N)
elif 9 == num_int:
    N[:1, :3] = "#"
    N[:2, :3] = "#"
    N[:3, :3] = "#"
    print(N)
