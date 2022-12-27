# 数据集处理

## xlsx.py

本代码主要对./data/sent_train.txt进行处理，得到people_relation_extract项目中“人物关系表.xlsx”形式的数据集

可能需要修改的地方：

- 5-41行：类别聚合的映射表
  - 注：修改映射表之后需要相应地到people_relation_extract项目的model_train.py的48行修改类别数
- 43行：要处理的文件（默认train）
- 60行：丢弃了“姻亲”关系，因为数量太少，如果保留可以注释掉
- **64行**：数据集分层抽样比例，训练结果差的可以增加样本数

使用过程：

1. `python xlsx.py`
2. `python relation_bar_chart.py`
3. 把./人物关系表.xlsx复制到people_relation_extract项目的/data目录
4. 在people_relation_extract项目的/data目录中执行`python data_into_train_test.py`，得到train.txt和test.txt
5. 训练和测试模型即可

## ner.py

本代码主要利用hanlp免费api进行ner，得到**演示**用的数据（不是实验数据）

可能需要修改的地方：

- 5行：token
- 9行：需要ner的txt文件
- 13行：需要ner的范围
