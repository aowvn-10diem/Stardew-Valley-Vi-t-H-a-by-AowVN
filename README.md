# Việt hóa Stardew Valley 1.6.16 — AowVN

Dự án tiếp quản từ đội trước ngày 09/11/2026. Baseline: **RC2 SOURCE REVIEW 23/10/2026**.
Đây là nguồn JSON, **chưa phải bản cài**. Mục tiêu đóng gói: **XNB cho game 1.6.16**.

## Cấu trúc

| Thư mục | Nội dung | Quy tắc |
| --- | --- | --- |
| `source/` | Nguồn đang làm việc (RC2 giải nén: Data, Dialogue, Strings, KIT_TESTER) | Chỉ sửa 238 file không hậu tố locale; mọi sửa phải qua changes có guard |
| `baseline/` | ZIP gốc RC1, RC2 SOURCE, RC2 QA + `SHA256SUMS.txt` | Bất biến, không sửa |
| `qa/` | Hồ sơ QA RC2 nguyên bản (validator, changes.json, evidence, 7 cảnh báo token) | Không sửa; công cụ mới đặt ở `tools/` |
| `tools/` | Script dự án | `ci_validate.py` chạy validator và trả mã lỗi cho CI |
| `docs/handoff/` | Tài liệu bàn giao của đội trước | Tham khảo |

2.028 file có hậu tố locale (`*.es-ES.json`…) là bộ tham chiếu, phải giữ nguyên byte (`.gitattributes` tắt chuyển đổi EOL).

## Kiểm định tự động

GitHub Actions `Kiem dinh tinh` chạy trên mỗi push/PR: kiểm SHA256 baseline, giải nén RC1, chạy `qa/validate.py` trên `source/`, fail nếu có lỗi hoặc lệch khung lệnh Events. Báo cáo nằm trong Summary và artifact `validation-report`.

Chạy tay:

```sh
mkdir -p /tmp/rc1 && unzip -q baseline/Stardew_vi_1.6_RC1_BASELINE.zip -d /tmp/rc1
python3 tools/ci_validate.py /tmp/rc1
```

Kiểm định tĩnh đạt **không** có nghĩa là chạy được game.

## Kế hoạch

Plan phân chia model và lộ trình G0–G7: wiki Notion, trang "16. Plan tiếp quản".
