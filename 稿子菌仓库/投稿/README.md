# 投稿

每篇论文以 JSON 文件存储，文件名格式：`{论文ID}_{论文标题}.json`

## 示例数据

```json
{
  "id": "demo_paper_001",
  "title": "基于机器学习的碳排放预测研究",
  "journal": "Journal of Cleaner Production",
  "status": "under_review",
  "role": "first_author",
  "priority": 3,
  "submittedDate": "2026-03-15",
  "manuscriptId": "JCLEPRO-D-26-01234",
  "tags": ["机器学习", "碳排放", "预测"],
  "workId": "",
  "account": {
    "username": "researcher@example.com",
    "password": ""
  },
  "trackingUrl": "https://ees.elsevier.com/jclepro/",
  "timeline": [
    {
      "id": "evt_001",
      "date": "2026-03-15",
      "label": "收稿",
      "color": "#6366f1",
      "note": "通过 Editorial Manager 投稿"
    },
    {
      "id": "evt_002",
      "date": "2026-03-20",
      "label": "初审",
      "color": "#8b5cf6",
      "note": "编辑初步审查通过"
    },
    {
      "id": "evt_003",
      "date": "2026-04-10",
      "label": "外审",
      "color": "#ec4899",
      "note": "送三位审稿人",
      "reviewComments": [],
      "reviewReplies": []
    }
  ]
}
```

## 审稿意见和回复

在时间线节点中，`reviewComments` 和 `reviewReplies` 字段存储上传文件的引用：
- `reviewComments`：审稿意见文件列表
- `reviewReplies`：审稿意见回复文件列表
- 实际文件存储在 `文件/{论文名称}/审稿意见/` 和 `文件/{论文名称}/审稿意见回复/`
