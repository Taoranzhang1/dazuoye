实验记录

实验目标
构建电影评分预测模型，优化预测准确率。

关键指标
- 主要指标: RMSE (均方根误差)
- 次要指标: MAE (平均绝对误差)

实验结果

基线模型 (baseline)
- 数据集: v1 (原始数据)
- 模型: RandomForest (n_estimators=50, max_depth=10)
- 性能: RMSE: 1.4519, MAE: 1.2234

改进模型 (improved)
- 数据集: v2 (清洗后数据)  
- 模型: RandomForest (n_estimators=100, max_depth=20)
- 性能: RMSE: 1.0588, MAE: 0.8829

生产就绪模型
选择：改进模型
- 理由：改进模型在清洗后的数据上表现更好，RMSE从1.4519降低到1.0588
- 指标：RMSE是我们优化的主要指标