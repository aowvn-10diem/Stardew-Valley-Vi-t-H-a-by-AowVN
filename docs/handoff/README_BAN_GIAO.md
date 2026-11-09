# Bàn giao dự án Việt hóa Stardew Valley 1.6

## 1. Tóm tắt điều hành

**Mục đích:** chuyển toàn bộ tư liệu sẵn có cho đội độc lập rà soát kỹ thuật, nội dung và đề xuất đường phát hành. **Baseline hiện hành: RC2 SOURCE REVIEW, đóng gói ngày 23/10/2026**. Đây là bản nguồn mới nhất đã tìm thấy, **không phải bản Final, không phải bản cài có thể chơi ngay**. Công việc của đội nhận bàn giao là đánh giá độc lập, không mặc định duyệt lại các kết luận cũ.

Gói này gồm nguồn RC2, nguyên bản RC1 làm baseline so sánh, báo cáo và công cụ QA, bản đồ dự án, cùng danh mục wiki để chủ dự án cấp quyền. Không có bản game, save thử, font/mod, XNB, manifest hoặc content pack đã kiểm chứng. Chưa xác định được bản vá 1.6.x, nền tảng, công cụ build và môi trường game đích.

## 2. Đọc và mở gói

1. Kiểm tra `SHA256SUMS.txt` bằng `sha256sum -c SHA256SUMS.txt` từ thư mục gốc bàn giao (Linux/macOS có `sha256sum`; công cụ tương đương trên Windows). Nếu sai, dừng và lấy lại gói; không ghi đè bản gốc.
2. Đọc `GRAPHMAP_DU_AN.md` và `WIKI_VA_QUYEN_TRUY_CAP.md`.
3. Dùng `01_Nguon/Stardew_vi_1.6_RC2_SOURCE_2026-10-23.zip` làm **nguồn đang giao**. Giải nén vào thư mục làm việc riêng. Giữ nguyên cả thư mục tham chiếu và cấu trúc đường dẫn.
4. Giải nén `02_QA/Stardew_vi_RC2_QA_2026-10-23.zip` và `03_Baseline/Stardew_vi_1.6_RC1_BASELINE.zip` vào hai thư mục riêng nếu cần tái lập kiểm định. RC1 chỉ phục vụ đối chiếu và truy vết, không phải bản mới nhất.
5. Đọc `VERSION.txt` và `KIT_TESTER/` trong RC2. Các tài liệu trong RC1 là lịch sử; nếu hướng dẫn cài hoặc tuyên bố hoàn tất mâu thuẫn với cảnh báo RC2 thì **không làm theo RC1**.

Ví dụ trên Linux/macOS, chạy từ gốc gói đã giải nén:

```sh
sha256sum -c SHA256SUMS.txt
mkdir -p work/rc1 work/rc2 work/qa
unzip -q 03_Baseline/Stardew_vi_1.6_RC1_BASELINE.zip -d work/rc1
unzip -q 01_Nguon/Stardew_vi_1.6_RC2_SOURCE_2026-10-23.zip -d work/rc2
unzip -q 02_QA/Stardew_vi_RC2_QA_2026-10-23.zip -d work/qa
python3 work/qa/validate.py work/rc2 work/rc1
```

`validate.py` cần Python 3, không cần thư viện ngoài; nó **ghi lại** `work/qa/validation.json`, do đó hãy giữ bản ZIP QA nguyên vẹn. Báo cáo đạt kiểm định tĩnh không đồng nghĩa chạy được game. Xem `work/qa/README.md` để hiểu phạm vi và cách áp patch; chỉ chạy patch trên bản sao, không chạy vào thư mục game. Patch chỉ tạo lại các thay đổi JSON, không tự áp thay đổi tài liệu `KIT_TESTER`. Trước khi áp hãy kiểm tra SHA-256 baseline.

## 3. Dữ liệu và nguồn chuẩn

- `Data/`: dữ liệu trò chơi, có trường kỹ thuật lẫn văn bản; `Data/Events/` chứa script sự kiện, cần bảo toàn lệnh, điều kiện, dấu phân tách, tên NPC, ID, tọa độ.
- `Dialogue/`: hội thoại, quan hệ và các nhánh nhân vật; phải kiểm tra ai nói, người nghe, ngữ cảnh, giới tính và trạng thái quan hệ.
- `Strings/`: UI, mô tả, tên, chuỗi hệ thống, lịch trình và nội dung khác. Văn bản hiển thị có thể tham chiếu từ Data; phân biệt `Name` nội bộ và `DisplayName`/đường dẫn bản địa hóa.
- 2.266 JSON gồm **238 file không có hậu tố locale** trong phạm vi nguồn VI và **2.028 file có hậu tố locale** dùng tham chiếu; các file base còn có cả dữ liệu kỹ thuật, không phải mọi giá trị đều là câu dịch. Không dịch hoặc chỉnh các bộ tham chiếu nếu chưa có quyết định chính thức.
- Trong kho tùy biến này, nhiều file `.es-ES.json` được dùng làm tham chiếu tiếng Anh. Không giả định nhãn locale hay wiki cũ phản ánh chính xác dữ liệu game đích: kiểm tra từng file/key, nguồn gốc và độ khớp với **bản game thật** trước khi kết luận.
- Phải bảo toàn biến và ngữ pháp điều khiển, như `@`, `{0}`, `#$e#`, `#$b#`, `${...^...}$`, `#`, `/`, ID và enum. Chênh lệch token chỉ là tín hiệu cần đọc theo ngữ cảnh; không tự sửa hàng loạt bằng regex.

## 4. Tiến độ và bằng chứng

| Mốc | Tình trạng thực tế |
| --- | --- |
| Các vòng dịch & rà trước đó | Wiki lưu lịch sử phân theo Dialogue, Strings, Data/Events, lễ hội và các vòng RC. Những số 100% hoặc trạng thái 'xong' cũ là lịch sử, không chứng minh chất lượng hiện tại. |
| Kiểm định RC1 ngày 23/10/2026 | Kiểm định độc lập phát hiện lỗi cấu trúc, sót dịch, sai nghĩa, thuật ngữ, xưng hô và thêm ý. Nguồn đối chiếu chủ yếu là tham chiếu có sẵn trong ZIP, không phải bản game độc lập. |
| RC2 cùng ngày | Sửa 2.235 bản ghi/giá trị trong 43 JSON: 1.918 chỉ kỹ thuật, 311 chỉ nội dung, 6 cả hai. Không gọi đây là 2.235 câu thoại. `changes.json` ghi trước/sau. |
| QA tĩnh trên ZIP RC2 đã mở lại | 2.266/2.266 JSON hợp lệ; không có khóa trùng hay U+FFFD; không đổi đường dẫn thuộc tính so với RC1; 2.028 file tham chiếu giữ nguyên byte; 36/36 trường hợp trong hồ sơ kiểm định RC1 được vá. |
| Kiểm tra có phạm vi | 43.155 giá trị chuỗi được quét, bao gồm cả dữ liệu kỹ thuật. 258 bản ghi sự kiện trong 43 file có khung lệnh khớp sau che nội dung dịch; 666 đích tham chiếu đã kiểm tra giải được. Chỉ các trường và quy tắc khai báo trong validator được bao phủ. |
| Chưa đạt | Chưa chạy game, chưa xác nhận cài đặt, tương thích 1.6.x, font, UI, save, gameplay hoặc duyệt thủ công từng câu. Còn 7 cảnh báo token heuristic kế thừa cần triage, không mặc định là 7 lỗi. |

Nguồn chi tiết: wiki RC2 và kiểm định RC1 trong `WIKI_VA_QUYEN_TRUY_CAP.md`; QA gốc trong `02_QA/`.

## 5. Hạng mục đã sửa đáng hồi quy

- Khôi phục một số trường kỹ thuật (Furniture, Fish, công thức, quái, gói, quà tặng, nhiệm vụ, animation); phân biệt Name nội bộ với tên hiển thị; khôi phục một số ID/enum và dữ liệu máy.
- Khôi phục `none` trong `Data/Events/IslandSouth.json: IslandDepart`; bổ sung nháy đóng tại bốn nhánh Beach và sửa dấu `/` làm lệch trường nhiệm vụ. Đây là rủi ro cấu trúc đã vá, chưa chứng minh từng lỗi gây crash.
- Đã đọc sâu `Dialogue/Leah.json` (96 khóa) và `Dialogue/MarriageDialogueKrobus.json` (89 khóa, gồm khóa im lặng), sửa xưng hô/nghĩa; các nhóm khác chỉ rà có mục tiêu, không được suy thành toàn corpus đã duyệt.
- Sửa một số câu hôn nhân, Jas, Elliott, Willy, Clint; thống nhất Hang Đầu lâu, Mảnh Tán Sắc, Hội Thám Hiểm, gridball, Nấm Truffle ở các vị trí đã xác nhận; sửa wine; xóa các câu ngoài nguồn; phục hồi credits theo bản tham chiếu 1.6 đi kèm. Tra `changes.json` để kiểm từng file/key.
- Phương án chơi chữ `Dialogue/MarriageDialogueKrobus.json:Good_3` “cam... thảo... đen” vẫn cần biên tập và test ngữ cảnh.

## 6. Việc đội ngoài cần làm, theo thứ tự

### P0 — Xác lập baseline và quyền
- [ ] Đối chiếu SHA-256; xác nhận file nhận đủ, có quyền xem wiki; lưu bản bất biến.
- [ ] Chủ dự án xác nhận người liên hệ, người chốt thuật ngữ/xưng hô, phạm vi chia sẻ và quyền sử dụng/phân phối tài nguyên.
- [ ] Chốt đúng game **1.6.x**, nền tảng, bản phân phối, phương án tích hợp, công cụ/phiên bản và bản tham chiếu hợp pháp phù hợp. Không mặc định RC2 tương thích mọi bản 1.6.

### P1 — Kiểm định độc lập nguồn và kỹ thuật
- [ ] Chạy validator và tự viết/áp dụng kiểm tra độc lập; ghi lệnh, phiên bản công cụ, đầu vào, đầu ra và các điểm validator không bao phủ.
- [ ] Đọc `evidence_rc1.json`, `changes.json` và 7 mục trong `token_candidates_remaining.json`; hồi quy các bản sửa và triage từng cảnh báo theo ngữ pháp thực tế.
- [ ] Đối chiếu file tham chiếu trong kho với asset gốc của phiên bản game được chọn; rà cấu trúc Data/Events/Festivals, placeholders, phân nhánh, ID, enums và các chuỗi ghép. Xử lý mâu thuẫn bằng bằng chứng, không sửa mù.
- [ ] Chốt mâu thuẫn trong wiki: đặc biệt bảng thuật ngữ Hội Thám Hiểm và xưng hô Willy/Krobus. Các quyết định mới cần có người duyệt và cập nhật nguồn chuẩn.

### P2 — Rà nội dung
- [ ] Lập bảng phạm vi theo file/key và mức đã đọc thật; phân biệt quét tự động, đọc mẫu, và đọc toàn bộ. Không khẳng định 100% từ heuristic.
- [ ] Đối chiếu ngữ nghĩa, đúng giọng và 7 lớp bối cảnh; ưu tiên 60 phút đầu, UI, tên vật phẩm, lời thoại nhân vật, sự kiện, hôn nhân, nhiệm vụ, lễ hội. Tập trung lỗi thêm ý/sót ý/xưng hô, không thơ hóa ngoài nguyên tác.
- [ ] Kiểm tra Mad Libs và các chuỗi ghép theo thuật toán và thứ tự mảng; duyệt Good_3 của Krobus. Không tự diễn giải các trường kỹ thuật như văn bản cần dịch.

### P3 — Tích hợp và playtest
- [ ] Thiết kế/triển khai phương án đóng gói phù hợp (ví dụ XNB hoặc content pack sau khi xác định tính khả thi), ghi toolchain, đầu vào, asset mapping và lệnh tái lập. Bản hiện tại **không có pipeline đã xác minh**.
- [ ] Test font/dấu, cỡ chữ/wrap, UI/perk; thử giới tính, Beach, rời đảo, Leah/Jas và Krobus sống chung; test Joja, quà, công thức, gói, nội thất, máy, load/save. Chụp ảnh/video, lưu log, ghi bản game và save/test case.
- [ ] Có phương án sao lưu/gỡ/khôi phục, không thao tác trực tiếp trên save thật không sao lưu.

### P4 — Phát hành sau nghiệm thu
- [ ] Tạo build mới có phiên bản, hash, hướng dẫn cài/gỡ đã thử và danh sách giới hạn còn lại; chạy kiểm định **trên gói xuất cuối**.
- [ ] Báo cáo lỗi theo mức A: lỗi vận hành/mất dữ liệu; B: sai nghĩa/nhánh; C: diễn đạt/hiển thị; kèm file/key, EN/VI, bước tái hiện, kỳ vọng/thực tế, ảnh/log, môi trường, người xử lý, trạng thái và minh chứng retest.
- [ ] Chỉ dùng nhãn Final khi chủ dự án và đội QA ký duyệt các cổng kỹ thuật, biên tập, tích hợp, playtest, tài liệu và quyền phân phối. Chưa có mốc ngày hay người chịu trách nhiệm được chốt.

## 7. Kết quả đề nghị đội ngoài bàn giao lại

1. Báo cáo đánh giá độc lập: phạm vi đã/không kiểm, kết quả tái lập, ma trận file/key và mức tin cậy; danh sách vấn đề ưu tiên, bằng chứng và rủi ro còn lại.
2. Danh sách thay đổi dạng `file/key/old/new/lý do`, có guard và review; quyết định thuật ngữ/xưng hô, ngoại lệ và test hồi quy.
3. Mã/công cụ, quy trình build có thể tái lập, bản nguồn mới + bản cài thử nếu tạo được, mỗi tệp có version/hash; không ghi đè RC1/RC2.
4. Ma trận playtest và log/ảnh; hướng dẫn cài/gỡ và known issues cập nhật. Bảng duyệt cuối ghi người duyệt/ngày/quyết định.

## 8. Điểm cần chủ dự án quyết định

- Ai là đầu mối và người duyệt cuối? Kênh nhận issue và thời hạn?
- Bản game/platform nào là mục tiêu? Chọn pipeline nào sau khi đội kỹ thuật đánh giá?
- Chia sẻ wiki nào, quyền xem/bình luận/chỉnh sửa đến đâu? Cấp tối thiểu cần thiết; không chia sẻ tự động.
- Quyền dùng, chia sẻ tài nguyên game và credit: xác minh với chủ sở hữu/chính sách tương ứng trước khi phân phối; gói này không xác nhận quyền.
