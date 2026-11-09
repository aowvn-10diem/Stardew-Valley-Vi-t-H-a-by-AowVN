STARDEW VALLEY VIỆT HÓA — RC2 SOURCE REVIEW

CẢNH BÁO: Đây là nguồn JSON, KHÔNG phải gói cài trực tiếp.
Hướng dẫn RC1 “chép Data/Dialogue/Strings vào Content, không cần SMAPI”
chưa được chứng minh và không còn được coi là hướng dẫn hợp lệ.

Gói này không chứa XNB hoặc manifest/content pack để game nạp bản dịch.
Nhóm tích hợp cần chọn một pipeline:
1. Content pack phù hợp với SMAPI + Content Patcher; khai báo đúng asset,
   đường dẫn (đặc biệt Characters/Dialogue), loại dữ liệu và điều kiện nạp.
2. Nếu có pipeline XNB sẵn có của dự án, đóng lại đúng loại asset và phiên
   bản game, rồi thử trên bản cài riêng. Không giả định JSON đổi đuôi là XNB.

CHƯA có pipeline nào ở trên được thực thi/kiểm thử trong gói này.
Không ghi đè thư mục game đang chơi hoặc dùng save chính để thử.
Sao lưu Content và Saves trước mọi bước tích hợp; thử trên save mới/copy.
Sau tích hợp: dùng HuongDan_Test.md; lưu log game/SMAPI và ảnh màn hình.
Tháo gỡ bằng cơ chế của gói tích hợp; không hứa save không bị ảnh hưởng.

Tài liệu tham khảo:
https://wiki.stardewvalley.net/Modding:Content_Patcher
https://stardewvalleywiki.com/Modding:Using_XNB_mods
