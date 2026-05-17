# 审稿

记录你作为审稿人的审稿任务。每项以 JSON 文件存储。

## 示例数据

```json
{
  "id": "demo_review_001",
  "journal": "Applied Energy",
  "paperTitle": "Renewable Energy Integration in Smart Grids",
  "round": 1,
  "inviteDate": "2026-04-01",
  "dueDate": "2026-05-01",
  "decision": "minor",
  "status": "completed",
  "link": "",
  "notes": "3位作者，8个图，补充材料齐全",
  "timeline": [
    {
      "id": "rev_evt_001",
      "date": "2026-04-01",
      "label": "收到审稿邀请",
      "color": "#059669",
      "note": ""
    }
  ]
}
```

## 决定类型
- `accept` — 接收
- `minor` — 小修
- `major` — 大修
- `reject` — 拒稿
