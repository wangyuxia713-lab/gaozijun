# 评价

期刊评价记录，每份以 JSON 文件存储。

## 示例数据

```json
{
  "id": "demo_eval_001",
  "paperId": "demo_paper_001",
  "journalName": "Journal of Cleaner Production",
  "impactFactor": "9.8",
  "tiers": {
    "cn": {
      "cssci": false,
      "cssciEx": false,
      "pku": false,
      "econTop": false
    },
    "en": {
      "absStar": "3",
      "ssciQ": "Q1",
      "casQ": "1区"
    }
  },
  "myNotes": "审稿周期约3个月，编辑效率高，审稿意见专业。",
  "communityNotes": [
    {
      "source": "小木虫",
      "content": "审稿速度快，平均2-3个月有结果。",
      "date": "2026-01-10"
    }
  ]
}
```

## 期刊等级体系

**中文：**
- CSSCI / CSSCI扩展版
- 北大核心
- 经济Top（经济学领域）

**英文：**
- ABS 星级（0/1/2/3/4/4*）
- SSCI/SCI 分区（Q1/Q2/Q3/Q4）
- 中科院分区（1区/2区/3区/4区）
