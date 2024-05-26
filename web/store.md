# Đầu bài:

![Screenshot (450)](https://github.com/ductohno/ehc-adward/assets/152991010/dc5af649-5ac1-4592-847c-150f1dfb4580)

- Khi vào trang web thì ta thấy:

![Screenshot (451)](https://github.com/ductohno/ehc-adward/assets/152991010/0ec4c974-7f30-4d48-a558-fb990bdd38c7)

- Bài này rất có thể là sql injection
# Hướng làm: (chỉ có thể thực hiện trên burp)
- Bước 1: Sử dụng ' order by 1;-- để check xem có tất cả bao nhiêu cột
- Bước 2: Sử dụng ' UNION SELECT ... tùy vào số cột để check loại dữ liệu
- Bước 3: Kiểm tra version => suy đoán ra loại sql được sử dụng ( phỏng đoán xem cột nào chứa dữ liệu version)
- Bước 4: Áp playload vô và khai thác
# Exploit:
- Trước tiên thì vào burp, và test các câu lệnh order, ta nhận thấy với order by 4, server gặp lỗi

![Screenshot (452)](https://github.com/ductohno/ehc-adward/assets/152991010/eb9e8d4d-4cc5-4a45-ba95-339acfe980b1)

- Tiếp theo ta sẽ check từng cột xem chúng là loại dữ liệu gì, phỏng đoán đương nhiên là cột 1 là số, 2 cột còn lại là chữ


![Screenshot (453)](https://github.com/ductohno/ehc-adward/assets/152991010/0230dbb9-de4b-4178-be75-120553efa2fe)

- Chuẩn xác, bước tiếp theo là check version, do sử dụng sql cheat sheat của postswigger mà ko được, mình đã xin hint các anh, và nhận dc câu trả lời là sqlite, vậy nên mình tức tốc lên mạng tìm câu lệnh sau đó áp vô
- Câu lệnh: SELECT sqlite_version();
  
![Screenshot (454)](https://github.com/ductohno/ehc-adward/assets/152991010/e6cf0990-db8c-4b26-8f21-875f4e1a2916)

- Giờ thì mình truy cập vô https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md#sqlite-comments và tìm payload

- Xác định bảng chứa flag: SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'

![Screenshot (455)](https://github.com/ductohno/ehc-adward/assets/152991010/1292b6c8-08cf-4df1-89ff-840a1ffe1a3b)

- Truy cập bảng đó và lấy thông tin về cột chứa flag: SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='table_name'
  
![Screenshot (456)](https://github.com/ductohno/ehc-adward/assets/152991010/00f5a54a-a1a6-4fb3-a1d4-a391d5d65262)

- Cuói cùng thì truy cập vô cột flag và lấy flag thôi:

![Screenshot (457)](https://github.com/ductohno/ehc-adward/assets/152991010/5a9b5b2a-5a14-4be8-abbd-d30d58d02be5)

# Flag:
actf{37619bbd0b81c257b70013fa1572f4ed}




