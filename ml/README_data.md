数据文档

数据来源
- 数据集：电影评分模拟数据
- 生成方式：使用 ml/data_pipeline.py 生成

版本变更记录

v1 (初始版本)
- 文件：data/raw/ratings_v1.csv
- 记录数：1000条
- 特征：user_id, movie_id, rating

v2 (改进版本)  
- 文件：data/processed/ratings_v2.csv
- 改进内容：
  - 添加时间戳特征
  - 过滤低评分数据（rating < 2）
  - 记录数：约800条