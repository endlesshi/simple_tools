# Simple Tools
学习过程中的小工具

## rotation.py:
读取kitti格式的txt文件，对其中所有数据进行旋转变换，最后保存为新的文件。
### How to use:
```bash
python3 scripts/rotation.py
```
## pose2T.py:
读取pose格式的txt文件，将其转换成变换矩阵，最后以kitti格式保存为新的文件。
### How to use:
```bash
python3 scripts/pose2T.py
```

## combine_CSV.py:
将数据类型相同的CSV文件合并，保存为新的文件。
### How to use:
```bash
python3 scripts/combine_CSV.py
```

## remove_blank.py:
去除文件中每一行最后的空格，保存为新的文件。
### How to use:
```bash
python3 scripts/combine_CSV.py
```