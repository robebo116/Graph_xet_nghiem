from datetime import datetime

# Chuỗi thời gian ban đầu
thoi_gian = "2023-06-23 17:30:00"

# Chuyển đổi chuỗi thành đối tượng datetime
dt = datetime.strptime(thoi_gian, "%Y-%m-%d %H:%M:%S")

# Định dạng lại chuỗi thời gian
thoi_gian_moi = dt.strftime("%d-%m-%Y %H:%M")

print(type(thoi_gian_moi))  # Kết quả: 23-06-2023 17:30
