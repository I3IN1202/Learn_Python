class NhanVien:
    luong_co_ban = 3
    def __init__(self, ho_ten, tuoi, he_so_luong):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.he_so_luong = he_so_luong
    
    def tien_luong(self):
        return self.he_so_luong * self.luong_co_ban

class CongTy:
    def __init__(self, ten):
        self.ten = ten
        self.danh_sach_nhan_vien = {}

    def them_nhan_vien(self, nhan_vien):
        if not isinstance(nhan_vien, NhanVien):
            print('Nhan vien is existed!')
        self.danh_sach_nhan_vien[len(self.danh_sach_nhan_vien) + 1] = nhan_vien

    def xoa_nhan_vien(self, nhan_vien_id):
        if nhan_vien_id in self.danh_sach_nhan_vien:
            del self.danh_sach_nhan_vien[nhan_vien_id]
            print(f"Đã xóa")
        else:
            print(f"Không tìm thấy")

    def hien_thi_danh_sach(self):
        print(f"Danh sách nhân viên {self.ten}")
        for nhan_vien_id, nhan_vien in self.danh_sach_nhan_vien.items():
            print(f"ID: {nhan_vien_id}, Họ tên: {nhan_vien.ho_ten}, Tuổi: {nhan_vien.tuoi}, Hệ só lương: {nhan_vien.he_so_luong}")

# Câu 1
huy = NhanVien('Minh Huy', 21, 1.5)
print('Ket qua 1:', huy.tien_luong(), 'trieu VND')