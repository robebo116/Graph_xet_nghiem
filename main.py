import sys
import requests
import csv
from matplotlib import pyplot
from pathlib import Path
from ui_main import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QApplication,QCompleter
from PySide6.QtCore import Qt,QSortFilterProxyModel,QStringListModel,QRegularExpression
from PySide6.QtGui import QFont
import matplotlib
matplotlib.use('TkAgg')

data_dir = Path()



# Lấy danh sách tên xét nghiệm
lst_ten_xet_nghiem = []

with open(data_dir/'ds_ten_xn.txt','r',encoding='utf-8') as file:
    try:
        for i in range(2000):
            ten = file.readline().replace('\n','')
            if ten not in lst_ten_xet_nghiem:
                lst_ten_xet_nghiem.append(ten)
    except:
        pass
    file.close()

class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Nhấn vào để search bệnh nhân
        self.ui.pushButton_search.clicked.connect(lambda: self.Button_search())
        self.ui.lineEdit_search.returnPressed.connect(lambda:self.Button_search())
        self.ui.pushButton_search_2.clicked.connect(lambda: self.Button_search2())

        # TẠO 1 LINE IMPUT CÓ CHỨC NĂNG TỰ TÌM KIẾM STRING TRONG DATA VÀ HIỂN THỊ THEO DẠNG POPUP VÀ COMPLETER
        completer = QCompleter()
        font = QFont('Segeo UI',12) # cài đặt font của completer
        completer.popup().setFont(font) # set font cho completer

        # Tạo một QSortFilterProxyModel để loại bỏ phân biệt chữ hoa/thường và dấu
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.proxy_model.setSourceModel(completer.model())
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        completer.setModel(QStringListModel(lst_ten_xet_nghiem))

        self.ui.lineEdit_search_2.textChanged.connect(lambda: self.on_text_changed())
        
        self.ui.lineEdit_search_2.setCompleter(completer)        

    ##############################################################
    # Hàm lấy token
    def token_add(self): # lấy token (token thay đổi mỗi ngày theo máy chủ)
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'http://192.168.15.50',
            'Referer': 'http://192.168.15.50/',
            'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        }
        json_data = {
            'email': 'vinhdv_ntlm',
            'password': '1',
            'forgot-password': True,
            'benhVien': 2,
        }
        response = requests.post('http://192.168.15.60/api/v1/auth/login', headers=headers, json=json_data, verify=False)
        token = response.json()["token"]
        return token
    # Hàm lấy lịch sử xét nghiệm
    def history_xet_nghiem(self,token,benh_nhan_id):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
            'Authorization':'Bearer {}'.format(token),
            'Connection': 'keep-alive',
            'Origin': 'http://192.168.15.50',
            'Referer': 'http://192.168.15.50/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'X-RED-HID': '2',
        }

        params = {
            'tuNgay': '2023-05-26',
            'denNgay': '2023-05-26',
        }

        response = requests.get(
            'http://192.168.15.60/api/v1/dangkykhambenh/getLichSuXetNghiem/{}/145040'.format(benh_nhan_id),
            params=params,
            headers=headers,
            verify=False,
        )
        data_phieu_y_lenh = response.json()['data']
        return  data_phieu_y_lenh

    # Hàm lấy chi tiết xét nghiệm
    def list_xet_nghiem(self,token,phieu_y_lenh):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
            'Authorization':'Bearer {}'.format(token),
            'Connection': 'keep-alive',
            'Origin': 'http://192.168.15.50',
            'Referer': 'http://192.168.15.50/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'X-RED-HID': '2',
        }
        response = requests.get('http://192.168.15.60/api/v1/phongkham/getDetailPhieuYLenh/{}/2'.format(phieu_y_lenh), headers=headers, verify=False)
        data_xn = response.json()
        return  data_xn
    
    # Hàm lấy thông tin bệnh nhân
    def info_patient(self,token,benh_nhan_id):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
            'Authorization':'Bearer {}'.format(token),
            'Connection': 'keep-alive',
            'Origin': 'http://192.168.15.50',
            'Referer': 'http://192.168.15.50/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'X-RED-HID': '2',
        }

        response = requests.get('http://192.168.15.60/api/v1/dontiep/detailHsbaByBenhNhanId/{}'.format(benh_nhan_id), headers=headers, verify=False)
        return response.json()

    # Hàm click vào button search để tìm bệnh nhân
    def Button_search(self):
        with open(data_dir/'data_xet_nghiem.csv','w') as file:
            file.write('')
        token = self.token_add()
        benh_nhan_id = self.ui.lineEdit_search.text()
        data_info = self.info_patient(token,benh_nhan_id)
        self.ui.label_nam_patient.setText(data_info['ten_benh_nhan'])
        self.ui.label_maBN.setText(str(data_info['benh_nhan_id']))
        self.ui.label_namsinh.setText(str(data_info['nam_sinh']))
        # xử lý giới tính
        if data_info['gioi_tinh'] == 1:
            self.ui.label_sex.setText('Nam')
        else:
            self.ui.label_sex.setText('Nữ')
        # Xử lý địa chỉ có đầy đủ phường xã huyện
        ten_phuong_xa = data_info['ten_phuong_xa']
        ten_quan_huyen = data_info['ten_quan_huyen']
        ten_tinh_thanh_pho = data_info['ten_tinh_thanh_pho']
        dia_chi = ten_phuong_xa + ', ' + ten_quan_huyen + ', ' + ten_tinh_thanh_pho
        self.ui.label_dia_chi.setText(dia_chi)
        # Xử lý loại viện phí
        if data_info['loai_vien_phi'] == 2:
            self.ui.label_loai_vien_phi.setText('BHYT')
        else:
            self.ui.label_loai_vien_phi.setText('Viện phí')
        self.ui.label_sothe.setText(data_info['ms_bhyt'])
        # Xử lý mức hưởng
        if data_info['muc_huong'] == '1':
            self.ui.label_quyen_loi.setText('100%')
        elif data_info['muc_huong'] == '0.8':
            self.ui.label_quyen_loi.setText('80%')
        elif data_info['muc_huong'] == '0.95':
            self.ui.label_quyen_loi.setText('95%')
        else:
            self.ui.label_quyen_loi.setText('0%')
        # Xử lý hạn thẻ
        den_ngay = data_info['den_ngay']
        self.ui.label_han_the.setText(den_ngay)
        # Xử trí khoa phòng hiện tại
        khoa_phong = data_info['ten_khoa']
        self.ui.label_phonghientai.setText(khoa_phong)
        # Xử lý ngày vào viện
        self.ui.label_ngay_vao_vien.setText(data_info['ngay_vao_vien'])

        # Lấy danh sách tên các xét nghiệm
        data_phieu_y_lenh = self.history_xet_nghiem(token,benh_nhan_id)
        lst_phieu_y_lenh = []
        self.data = []
        try:
            for i in range(150):
                phieu_y_lenh = data_phieu_y_lenh[i]['phieu_y_lenh_id']
                thoi_gian_chi_dinh = data_phieu_y_lenh[i]['thoi_gian_chi_dinh']
                if phieu_y_lenh not in lst_phieu_y_lenh:
                    data_xn = self.list_xet_nghiem(token,phieu_y_lenh)
                    for i in range(len(data_xn)):
                        code = True
                        ten = data_xn[i]['ten']
                        # if ten not in lst_ten_xet_nghiem:
                        #     with open(data_dir/'ds_ten_xn.txt','a',encoding='utf-8') as file:
                        #         file.write(ten)
                        #         file.write('\n')
                        #         file.close()
                        ket_qua = data_xn[i]['ket_qua']
                        for char in 'ket_qua':
                            code = True
                            if char not in ket_qua:
                                data_xet_nghiem = [ten,ket_qua,thoi_gian_chi_dinh]
                                # self.data.append(data_xet_nghiem)
                                with open(data_dir/'data_xet_nghiem.csv','a',encoding='utf-8',newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow(data_xet_nghiem)
                                code = False
                                if code == False:
                                    break
                    lst_phieu_y_lenh.append(phieu_y_lenh)
        except:
            pass
        data_ten = []
        self.lst_xn_all = []

        with open('data_xet_nghiem.csv','r',encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] not in data_ten:
                    data_ten.append(row[0])
        for ten in data_ten:
            lst_xn = []
            lst_ket_qua = []
            lst_thoi_gian_chi_dinh = []
            with open('data_xet_nghiem.csv','r',encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == ten:
                        try: 
                            lst_ket_qua.append(float(row[1]))
                        except:
                            try:
                                lst_ket_qua.append(int(row[1]))
                            except:
                                lst_ket_qua.append((row[1]))
                        date_xn = row[2].split(' ')[0]
                        lst_thoi_gian_chi_dinh.append(date_xn) 

            lst_xn.append(ten)
            lst_xn.append(lst_ket_qua)
            lst_xn.append(lst_thoi_gian_chi_dinh)
            self.lst_xn_all.append(lst_xn)



    # Hàm click vào button search xét nghiệm
    def Button_search2(self):

        for i in range(len(self.lst_xn_all)):
            if self.lst_xn_all[i][0] == self.ui.lineEdit_search_2.text(): 
                with open(data_dir/'data_graph_xn.txt','w',encoding='utf-8') as file:
                    file.write(str(self.lst_xn_all[i]))


                ten = self.lst_xn_all[i][0]
                ket_qua = self.lst_xn_all[i][1]
                ket_qua_reversed = list(reversed(ket_qua))
                thoi_gian_chi_dinh = self.lst_xn_all[i][2]

                thoi_gian_reversed = list(reversed(thoi_gian_chi_dinh))
                pyplot.plot(thoi_gian_reversed,ket_qua_reversed,marker = '.',markersize =10)
                pyplot.ylabel(ten)
                pyplot.xlabel('Thời gian xét nghiệm')
                pyplot.legend([ten])
                for i in range(len(thoi_gian_reversed)):
                    pyplot.annotate(f'({thoi_gian_reversed[i]}, {ket_qua_reversed[i]})', (thoi_gian_reversed[i], ket_qua_reversed[i]), textcoords="offset points", xytext=(0,10),ha = 'center')
                pyplot.tight_layout()
                pyplot.show()
                
    # METHOD CẬP NHẬT TEXT TRONG Ô TÌM KIẾM TÊN BỆNH NHÂN
    def on_text_changed(self):
        self.proxy_model.setFilterRegularExpression(QRegularExpression('.*')) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())