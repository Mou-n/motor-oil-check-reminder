import tkinter as tk
from tkinter import messagebox

# Quy định số km tối đa theo loại nhớt
oil_limits = {
    "thuong": 1500,
    "ban_tong_hop": 2000,
    "tong_hop": 3000
}

def check_oil():
    try:
        km = int(entry_km.get())
        oil_type = oil_var.get()

        max_km = oil_limits[oil_type]
        if km >= max_km:
            msg = f"⚠ Đã đi {km}km kể từ lần thay nhớt.\n📌 Nên thay nhớt ngay (giới hạn {max_km}km)!"
        else:
            remaining = max_km - km
            msg = f"✅ Nhớt còn tốt.\nBạn có thể đi thêm khoảng {remaining}km."

        messagebox.showinfo("Kết quả kiểm tra nhớt", msg)
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng số km!")

# Giao diện
root = tk.Tk()
root.title("Nhắc thay nhớt xe máy 🛵")
root.geometry("300x250")

tk.Label(root, text="Nhập số km đã đi từ lần thay nhớt:").pack()
entry_km = tk.Entry(root)
entry_km.pack()

tk.Label(root, text="Chọn loại nhớt bạn dùng:").pack()

oil_var = tk.StringVar(value="thuong")
tk.Radiobutton(root, text="Dầu thường", variable=oil_var, value="thuong").pack()
tk.Radiobutton(root, text="Bán tổng hợp", variable=oil_var, value="ban_tong_hop").pack()
tk.Radiobutton(root, text="Tổng hợp", variable=oil_var, value="tong_hop").pack()

tk.Button(root, text="Kiểm tra", command=check_oil).pack(pady=10)

root.mainloop()
