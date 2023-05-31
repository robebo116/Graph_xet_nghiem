import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.image import imread

def on_button_clicked(event):
    print("Button clicked!")

fig, ax = plt.subplots()

# Tạo nút tùy chỉnh
button_ax = plt.axes([0.7, 0.9, 0.1, 0.05])  # Vị trí và kích thước của nút
image = imread('bar-chart-5-24.png')
button = Button(button_ax,'',image=image)  # Tạo nút với nội dung 'Custom Button'
button.on_clicked(on_button_clicked)  # Gán hàm xử lý sự kiện khi nút được nhấn

plt.show()
