#!/usr/bin/env python3
"""Chạy validator RC2 gốc (qa/validate.py) trên source/ so với RC1 baseline và trả mã lỗi cho CI.

Không sửa qa/: copy qa sang thư mục tạm vì validate.py ghi validation.json cạnh chính nó.
Dùng: python3 tools/ci_validate.py <thư_mục_rc1_đã_giải_nén> [<thư_mục_xuất_báo_cáo>]
"""
import json, shutil, subprocess, sys, tempfile
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
rc1 = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else repo / "ci-report"
out.mkdir(parents=True, exist_ok=True)

with tempfile.TemporaryDirectory() as tmp:
    qa = Path(tmp) / "qa"
    shutil.copytree(repo / "qa", qa)
    subprocess.run([sys.executable, "-I", str(qa / "validate.py"), str(repo / "source"), str(rc1)],
                   check=True, stdout=subprocess.DEVNULL)
    shutil.copy(qa / "validation.json", out / "validation.json")

r = json.loads((out / "validation.json").read_text(encoding="utf-8"))
fail = []
if r["errors"]:
    fail.append(f"{len(r['errors'])} lỗi validator")
if r["event_skeleton_remaining"]:
    fail.append(f"{r['event_skeleton_remaining']} kịch bản Events lệch khung lệnh")
if r["base_files"] != 238 or r["reference_files"] != 2028:
    fail.append(f"số file lệch: base={r['base_files']} ref={r['reference_files']}")

lines = ["## Kết quả kiểm định tĩnh", "",
         f"- JSON: {r['json_files']} (nguồn {r['base_files']} / tham chiếu {r['reference_files']})",
         f"- Chuỗi quét: {r['string_leaves']}",
         f"- Events: {r['event_records']} bản ghi, lệch khung: {r['event_skeleton_remaining']}",
         f"- Lỗi: {len(r['errors'])}",
         "", "**ĐẠT**" if not fail else "**KHÔNG ĐẠT:** " + "; ".join(fail)]
for e in r["errors"][:50]:
    lines.append(f"- `{e}`")
(out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
sys.exit(1 if fail else 0)
