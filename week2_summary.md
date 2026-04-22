# Week 2 Summary

## 完成内容
- 读取并理解 behaviors.tsv 和 news.tsv
- 为原始表添加列名
- 统计 history 和 impressions 长度分布
- 将 impressions 展开为候选级样本
- 将候选样本与新闻表合并
- 保存处理后的 parquet 文件

## 产出文件
- notebooks/02_preprocess.ipynb
- src/data/preprocess_utils.py
- data/processed/train_merged_20k.parquet
- data/processed/valid_merged_10k.parquet

## 下一周计划
- 构造 TF-IDF 特征
- 跑 Logistic Regression
- 跑 LightGBM