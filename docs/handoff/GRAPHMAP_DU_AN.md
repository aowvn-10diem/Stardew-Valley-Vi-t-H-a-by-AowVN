# Graphmap — bản đồ dự án Việt hóa Stardew Valley

Trạng thái tham chiếu: RC2 SOURCE REVIEW 23/10/2026. Sơ đồ mô tả quan hệ và điểm chặn, **không khẳng định các cổng chưa làm đã đạt**. Mermaid được hỗ trợ trong GitHub, nhiều trình đọc Markdown và các công cụ Mermaid. Bản nguồn sơ đồ riêng: `graphmap.mmd`.

```mermaid
flowchart TB
    Goal["Mục tiêu: Việt hóa Stardew Valley 1.6<br/>bàn giao đội độc lập"]
    Base["RC1 baseline<br/>ZIP gốc • lịch sử"]
    Audit["Kiểm định RC1<br/>36 trường hợp cần vá"]
    Source["RC2 SOURCE REVIEW<br/>2.266 JSON • chưa cài được"]
    QA["QA RC2<br/>2.235 thay đổi / 43 JSON<br/>validator + log + 7 cảnh báo"]
    Wiki["Wiki dự án<br/>ngữ cảnh • giọng • thuật ngữ<br/>kỹ thuật • lịch sử"]
    subgraph Content["Nội dung & cấu trúc nguồn RC2"]
        D["Dialogue/<br/>thoại, quan hệ, nhánh"]
        S["Strings/<br/>UI, tên, mô tả, lịch trình"]
        A["Data/<br/>vật phẩm, nhiệm vụ, dữ liệu"]
        E["Data/Events + Festivals<br/>script và lời thoại"]
        R["Bản tham chiếu locale<br/>giữ nguyên, kiểm nguồn gốc"]
        K["KIT_TESTER + VERSION<br/>tài liệu nguồn, chưa phải hướng dẫn cài cuối"]
    end
    Version["Chốt game 1.6.x, nền tảng<br/>asset chuẩn, quyền và toolchain"]
    Review["Đội ngoài: kiểm định độc lập<br/>kỹ thuật + biên tập + triage"]
    Build["Thiết kế & thực thi tích hợp<br/>XNB hoặc content pack phù hợp"]
    Play["Playtest thực tế<br/>font • UI • nhánh • gameplay • save"]
    Gate{"Cổng nghiệm thu<br/>bằng chứng + người duyệt?"}
    Return["Báo cáo + lỗi + vá có guard<br/>log, hash, quyết định, retest"]
    Final["Ứng viên Final<br/>chỉ sau đầy đủ nghiệm thu"]
    Goal --> Source
    Base --> Audit --> Source
    Base -. "so sánh" .-> QA
    Source --> Content
    Source --> QA
    Wiki --> Review
    Content --> Review
    QA --> Review
    Version --> Review
    Version --> Build
    Review --> Build --> Play --> Gate
    Review --> Return
    Play --> Return
    Gate -- "chưa đạt" --> Return
    Return -- "sửa và kiểm lại" --> Review
    Gate -- "đủ bằng chứng & phê duyệt" --> Final
    classDef ready fill:#e8f1ec,stroke:#46a171,color:#163526
    classDef todo fill:#fbebde,stroke:#d5803b,color:#44290f
    classDef blocked fill:#fce9e7,stroke:#e56458,color:#4e211e
    class Base,Audit,Source,QA,Wiki ready
    class Version,Review,Build,Play,Return todo
    class Gate,Final blocked
```

## Bản đồ thao tác

| Nút | Đầu vào | Việc cần kiểm | Đầu ra / trạng thái |
| --- | --- | --- | --- |
| RC1 → kiểm định → RC2 | ZIP RC1 + báo cáo RC1 | Không nhầm lỗi đã báo với lỗi chưa vá; so `changes.json` | RC2 là nguồn mới nhất, chưa Final |
| RC2 → QA | ZIP RC2 và RC1, Python 3 | Chạy validator, xem phạm vi và các ngoại lệ | Kiểm định tĩnh có sẵn; không thay thế game thật |
| Wiki → biên tập | Trang 2/3/4/5/7/9/12/13 và 14/15 | Xung đột chuẩn, bối cảnh, tên, đại từ, token | Người có thẩm quyền chốt và ghi quyết định |
| Đầu vào game → tích hợp | Game hợp pháp + đúng 1.6.x, nền tảng và toolchain | Mapping asset, kiểu dữ liệu, cơ chế nạp | Chưa có pipeline hay gói cài đã xác minh |
| Build → playtest | Build cài thử + save thử được sao lưu | UI, font, sự kiện, nhánh, gameplay, load/save | Log, ảnh, lỗi và kết quả retest |
| Nghiệm thu → phát hành | Báo cáo độc lập, bản build, bằng chứng, quyền | Ký duyệt các cổng và hash gói cuối | Chưa đạt; chỉ gắn Final sau phê duyệt |

Đọc `README_BAN_GIAO.md` cho số liệu, giới hạn, chi tiết và checklist đầy đủ; đọc `WIKI_VA_QUYEN_TRUY_CAP.md` để mở wiki.
