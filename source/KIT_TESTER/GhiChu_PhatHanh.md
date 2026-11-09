# RC2 Source Review — 23/10/2026

## Trạng thái
Nguồn JSON đã chỉnh sửa và kiểm định tĩnh; chưa phải bản Final hay gói cài chơi được đã kiểm chứng. Giữ nguyên RC1 để đối chiếu, không ghi đè bản lưu trên Notion.

## Thực sự đã sửa
- 2.235 bản ghi/giá trị trong 43 JSON: 1.918 mục chỉ sửa kỹ thuật, 311 mục chỉ sửa nội dung, 6 mục có cả hai. Không quy đổi số này thành số câu thoại.
- Phục hồi bảng nội thất, cá, mũ, gói, công thức, quái vật, quà tặng, hoạt ảnh và trường kỹ thuật nhiệm vụ theo dữ liệu tham chiếu 1.6 đi kèm RC1. Tách Name nội bộ khỏi DisplayName, giữ nguyên tên hiển thị tiếng Việt qua Strings.
- Sửa mất `none` ở cảnh rời đảo, 4 dấu nháy đóng ở Beach; sửa dấu `/` bị dùng trong nội dung nhiệm vụ làm lệch trường dữ liệu.
- Rà toàn bộ file thoại thường Leah và thoại ở chung Krobus; sửa vai xưng hô, nghĩa và các câu thêm ý. Sửa thêm thoại sinh hoạt hôn nhân, Jas, Elliott, Willy, Clint và một số cảnh/phản ứng khác theo bằng chứng cụ thể.
- Đồng bộ Hang Đầu lâu, Mảnh Tán Sắc, Hội Thám Hiểm, gridball, Nấm Truffle; sửa dry wine thành vang khô.
- Dịch các chuỗi UI/Joja/hoạt ảnh còn sót; khôi phục mẫu nhiệm vụ bị cụt; sửa giá mua gấp ba; bỏ các câu đùa ngoài game trong RandomSentence.
- Khôi phục đúng thứ tự/tên người đóng góp của credits 1.6; dịch vai trò thay vì ghi sai tên tác giả.
- Thay tài liệu RC1 có tuyên bố chưa được kiểm chứng bằng trạng thái trung thực của gói nguồn.

## Kiểm tra tĩnh
2.266 JSON hợp lệ; 0 khóa trùng; 0 U+FFFD. Cấu trúc cây dữ liệu không thêm/mất đường dẫn. 2.028 file tham chiếu không thay byte. 36/36 trường hợp báo cáo RC1 có vá. 43 file Events/258 bản ghi không còn lệch khung lệnh với nguồn tham chiếu sau khi che phần thoại/câu hỏi. 666 đích tham chiếu phục hồi từ bảng nội thất/hoạt ảnh giải được trong gói.

Các kiểm tra này không chứng minh game đã chạy đúng, toàn bộ câu dịch đều hay hoặc font không tràn khung. Các chuỗi kỹ thuật tiếng Anh được khôi phục không phải sót dịch.
