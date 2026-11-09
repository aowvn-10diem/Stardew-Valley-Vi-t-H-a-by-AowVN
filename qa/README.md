# RC2 — Hồ sơ kiểm định và bản vá có guard

Nguồn RC1: SHA256 7d0f2ce4698e50c4394decc79c65265d051dacd936447b1fe4a9020c9c2cbf05.
RC2_SOURCE ZIP: SHA256 be34782ba9db1b414ce5cd2cf3be81846fffc05e651e88adbfa88fc1e29e9bdf.

- changes.json: từng file/key/giá trị cũ/mới và nhóm lý do, 2.235 mục, 43 JSON.
- evidence_rc1.json: 36 trường hợp của đợt kiểm định độc lập trước bản vá.
- validation.json: kiểm định sau khi mở lại chính ZIP RC2.
- token_candidates_remaining.json: 7 cảnh báo heuristic còn lại, không có khóa cảnh báo mới so với RC1. Không phải danh sách 7 lỗi game đã được chứng minh.
- apply_changes.py: tạo bản vá JSON từ thư mục RC1 giải nén; có guard chặn khác dữ liệu nguồn. Không chạy vào thư mục game. Không tự áp dụng các thay đổi tài liệu KIT_TESTER.
- validate.py: kiểm định cây RC2 so với cây RC1; Python 3, không cần thư viện ngoài.

Ví dụ:
python apply_changes.py /path/RC1 /path/RC2_json
python validate.py /path/RC2_json /path/RC1

Chỉ kiểm tra tĩnh: không chứng nhận tính tương thích engine, font, render,
load/save hay chất lượng văn phong của mọi câu. File tham chiếu .es-ES trong
kho tùy biến này chứa tiếng Anh; không suy diễn sang game cài đặt khác.

Gói nguồn không chứa XNB/manifest/content.json; phải tích hợp và chạy game
trước khi gọi là bản Final. Bản ghi kỹ thuật được khôi phục theo tham chiếu
đi kèm ZIP, chưa đối chiếu một bản game cài đặt cụ thể.
