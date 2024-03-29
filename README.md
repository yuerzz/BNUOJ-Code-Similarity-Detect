# BNUOJ-Code-Similarity-Detect
针对BNUOJ的代码查重辅助工具

BNU Online Judge:

校外：http://www.bnuoj.com

校内：http://acm.bnu.edu.cn

## 可用于：
* 比赛查重，IP定位
* 作业查重

## 功能：
* 抓取IP对应的网络环境，由此判定交题时的终端物理位置合法性
* 删除注释片段并重新格式化代码
* 通过Levenshtein距离来判断代码相似度

没有可执行文件，使用方法示例：
[Jupyter Notebook](https://github.com/ZitanChen/BNUOJ-utility/blob/master/BNUOJ%20Submission%20Analysis.ipynb)

## 欢迎大家来改进啊
可选思路：
* 拼接上开源工具[SIM](https://dickgrune.com/Programs/similarity_tester/)，从词法层面增强检测效果

## 用法
![image](https://github.com/ZitanChen/BNUOJ-Code-Similarity-Detect/blob/master/1.jpg)
![image](https://github.com/ZitanChen/BNUOJ-Code-Similarity-Detect/blob/master/2.jpg)
![image](https://github.com/ZitanChen/BNUOJ-Code-Similarity-Detect/blob/master/3.png)
