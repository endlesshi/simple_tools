# Simple Tools
学习过程中的小工具

## python创建虚拟环境
在服务器上创建并加载虚拟环境，安装自己想安装的库：
### How to use:
```bash
python3.9 -m venv env
source env/bin/activate
pip install XXX -i https://pypi.tuna.tsinghua.edu.cn/simple
```

***以下所有内容都需要修改文本路径为自己的源路径和目标路径**

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

## LCD_gt.py:
从groundtruth中提取出一定距离内的点作为回环点并保存
### How to use:
```bash
python3 scripts/LCD_gt.py
```

## LCD_draw.py:
画出一条路径上的回环检测结果
### How to use:
```bash
python3 scripts/LCD_draw.py
```