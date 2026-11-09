# Giới hạn nghiệm thu — RC2 Source Review

## Chưa thể đóng
1. Gói chỉ chứa JSON, chưa có pipeline XNB/content pack đã chạy. Chưa được quảng bá là bản cài chơi ngay.
2. Chưa chạy game: font tiếng Việt, line-wrap, màn hình perk, thoại dài, nhánh nam/nữ, cảnh Beach/rời đảo, quà tặng, chế tạo, cá, gói và nội thất cần test thực tế.
3. Phần kỹ thuật được khôi phục theo tham chiếu đi kèm ZIP, không phải đối chiếu với một bản game cài đặt cụ thể. Cần chốt đúng phiên bản trước tích hợp.
4. Đã quét tĩnh toàn bộ 43.155 giá trị chuỗi; chỉ những nhóm ghi rõ trong báo cáo được đọc biên tập thủ công sâu. Không chứng nhận đã đọc từng câu toàn corpus.
5. Heuristic token vẫn có 7 cảnh báo kế thừa, không có khóa cảnh báo mới: cần đọc ngữ pháp biến/tường thuật, không tự sửa theo regex. Các cảnh báo văn phong/spacing cũng gồm trường kỹ thuật và trường hợp hợp lệ.
6. Good_3 của Krobus dùng cách chuyển âm “cam... thảo... đen” cho lời nói mớ về black licorice; cần tester/biên tập viên nghe nhịp thoại và duyệt cách chuyển trò chơi chữ.

## Không còn coi là ngoại lệ vô hại
Không tiếp tục miễn trừ bảng Furniture thiếu trường, dữ liệu 1.5 lệch 1.6, mã nội bộ bị dịch hoặc câu thêm ý là “có chủ đích nên không sao”. Các nhóm này đã có vá cụ thể trong RC2; vẫn phải thử sau tích hợp.
