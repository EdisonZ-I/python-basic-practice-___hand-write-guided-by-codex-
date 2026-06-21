# Python Basic Practice

目标：先把 Python 语法、函数、数据结构和基础算法练扎实，再进入 NumPy 和 MNIST。

建议节奏：

- 每次只做 1 到 3 题。
- 先不要查完整答案，先写出能跑的版本。
- 每道题都放到指定 `.py` 文件里。
- 运行文件时，用 `assert` 自测。没有报错才算初步通过。
- 你把代码发给我后，我按“结论 / 主要问题 / 为什么 / 修改建议 / 下一题”批改。

通用要求：

- 除非题目允许，不要使用第三方库。
- 函数名、参数名尽量按题目给的来。
- 优先写清楚，再追求简短。
- 遇到边界情况时，先想清楚输入可能为空、长度为 1、存在重复值等情况。

推荐文件组织：

```text
python basic practice/
  python_basic_practice.md
  p01_basics.py
  p02_conditions.py
  p03_loops.py
  ...
```

## 第一阶段：变量、函数、条件判断

### P01：温度转换和数值计算

文件：`p01_basics.py`

实现：

```python
def celsius_to_fahrenheit(celsius):
    ...

def rectangle_area(width, height):
    ...

def average_three(a, b, c):
    ...
```

要求：

- `celsius_to_fahrenheit(0)` 返回 `32`
- `rectangle_area` 返回长方形面积
- `average_three` 返回三个数的平均值

自测：

```python
assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
assert rectangle_area(3, 4) == 12
assert average_three(3, 6, 9) == 6
```

### P02：条件判断

文件：`p02_conditions.py`

实现：

```python
def grade(score):
    ...

def is_even(n):
    ...

def max_of_three(a, b, c):
    ...
```

要求：

- `grade(score)`：
  - `score >= 90` 返回 `"A"`
  - `score >= 80` 返回 `"B"`
  - `score >= 70` 返回 `"C"`
  - `score >= 60` 返回 `"D"`
  - 否则返回 `"F"`
- `is_even(n)` 判断整数是否为偶数，返回布尔值
- `max_of_three` 返回三个数中的最大值，不要直接用 `max`

自测：

```python
assert grade(95) == "A"
assert grade(80) == "B"
assert grade(59) == "F"
assert is_even(10) is True
assert is_even(7) is False
assert max_of_three(3, 9, 5) == 9
assert max_of_three(-1, -3, -2) == -1
```

### P03：循环和累加

文件：`p03_loops.py`

实现：

```python
def sum_to_n(n):
    ...

def factorial(n):
    ...

def count_even_numbers(numbers):
    ...
```

要求：

- `sum_to_n(5)` 返回 `1 + 2 + 3 + 4 + 5`
- `factorial(0)` 返回 `1`
- `count_even_numbers` 统计列表中偶数个数
- 先用循环实现，不要用 `sum` 或 `math.factorial`

自测：

```python
assert sum_to_n(5) == 15
assert sum_to_n(1) == 1
assert factorial(0) == 1
assert factorial(5) == 120
assert count_even_numbers([1, 2, 3, 4, 6]) == 3
assert count_even_numbers([]) == 0
```

### P04：函数拆分

文件：`p04_functions.py`

实现：

```python
def is_positive(n):
    ...

def count_positive(numbers):
    ...

def positive_ratio(numbers):
    ...
```

要求：

- `is_positive(n)` 判断 `n > 0`
- `count_positive(numbers)` 必须调用 `is_positive`
- `positive_ratio(numbers)` 返回正数占比
- 如果列表为空，`positive_ratio([])` 返回 `0`

自测：

```python
assert is_positive(3) is True
assert is_positive(0) is False
assert count_positive([-1, 0, 2, 5]) == 2
assert positive_ratio([-1, 0, 2, 5]) == 0.5
assert positive_ratio([]) == 0
```

## 第二阶段：列表、字符串、字典

### P05：列表基础操作

文件：`p05_lists.py`

实现：

```python
def square_all(numbers):
    ...

def filter_greater_than(numbers, threshold):
    ...

def reverse_list(items):
    ...
```

要求：

- 返回新列表，不要修改原列表
- `reverse_list` 先用循环实现，不要直接用 `items[::-1]`

自测：

```python
data = [1, 2, 3]
assert square_all(data) == [1, 4, 9]
assert data == [1, 2, 3]
assert filter_greater_than([1, 5, 2, 8], 3) == [5, 8]
assert reverse_list(["a", "b", "c"]) == ["c", "b", "a"]
```

### P06：字符串处理

文件：`p06_strings.py`

实现：

```python
def count_char(text, target):
    ...

def remove_spaces(text):
    ...

def is_palindrome(text):
    ...
```

要求：

- `count_char` 统计字符出现次数
- `remove_spaces` 删除所有空格字符 `" "`
- `is_palindrome` 判断字符串是否回文，忽略大小写和空格

自测：

```python
assert count_char("banana", "a") == 3
assert remove_spaces("a b  c") == "abc"
assert is_palindrome("level") is True
assert is_palindrome("A man a plan a canal Panama") is True
assert is_palindrome("python") is False
```

### P07：字典计数

文件：`p07_dict_counting.py`

实现：

```python
def count_items(items):
    ...

def most_frequent(items):
    ...
```

要求：

- `count_items(["a", "b", "a"])` 返回 `{"a": 2, "b": 1}`
- `most_frequent(items)` 返回出现次数最多的元素
- 如果 `items` 为空，`most_frequent([])` 返回 `None`
- 出现次数相同时，返回更早出现的元素

自测：

```python
assert count_items(["a", "b", "a"]) == {"a": 2, "b": 1}
assert most_frequent(["x", "y", "x", "z"]) == "x"
assert most_frequent(["a", "b"]) == "a"
assert most_frequent([]) is None
```

### P08：成绩表

文件：`p08_student_scores.py`

实现：

```python
def average_score(scores):
    ...

def best_student(score_dict):
    ...

def pass_students(score_dict, pass_score):
    ...
```

要求：

- `average_score(scores)` 接收分数列表，空列表返回 `0`
- `best_student(score_dict)` 接收 `{"Alice": 90, "Bob": 80}`，返回最高分学生名
- 如果字典为空，`best_student({})` 返回 `None`
- `pass_students` 返回分数大于等于 `pass_score` 的学生名列表，保持原顺序

自测：

```python
scores = {"Alice": 90, "Bob": 75, "Cindy": 88}
assert average_score([90, 80, 70]) == 80
assert average_score([]) == 0
assert best_student(scores) == "Alice"
assert best_student({}) is None
assert pass_students(scores, 80) == ["Alice", "Cindy"]
```

## 第三阶段：基础算法

### P09：线性搜索

文件：`p09_linear_search.py`

实现：

```python
def find_index(items, target):
    ...

def contains(items, target):
    ...
```

要求：

- `find_index` 返回目标第一次出现的位置
- 找不到返回 `-1`
- `contains` 必须调用 `find_index`
- 不要用 `list.index` 或 `in`

自测：

```python
assert find_index([5, 3, 7, 3], 3) == 1
assert find_index([5, 3, 7], 9) == -1
assert contains(["a", "b"], "b") is True
assert contains(["a", "b"], "c") is False
```

### P10：找最小值和最大值

文件：`p10_min_max.py`

实现：

```python
def find_min(numbers):
    ...

def find_max(numbers):
    ...

def min_max(numbers):
    ...
```

要求：

- 不要用内置 `min`、`max`
- 空列表时返回 `None`
- `min_max([3, 1, 5])` 返回 `(1, 5)`

自测：

```python
assert find_min([3, 1, 5]) == 1
assert find_max([3, 1, 5]) == 5
assert min_max([3, 1, 5]) == (1, 5)
assert find_min([]) is None
assert min_max([]) is None
```

### P11：冒泡排序

文件：`p11_bubble_sort.py`

指定算法：冒泡排序。

实现：

```python
def bubble_sort(numbers):
    ...
```

要求：

- 返回升序新列表
- 不要修改原列表
- 不要用 `sorted` 或 `.sort`

自测：

```python
data = [5, 1, 4, 2]
assert bubble_sort(data) == [1, 2, 4, 5]
assert data == [5, 1, 4, 2]
assert bubble_sort([]) == []
assert bubble_sort([3]) == [3]
```

### P12：二分查找

文件：`p12_binary_search.py`

指定算法：二分查找。

实现：

```python
def binary_search(sorted_numbers, target):
    ...
```

要求：

- 输入列表已经按升序排列
- 找到返回索引
- 找不到返回 `-1`
- 不要用 `in`、`.index`

自测：

```python
assert binary_search([1, 3, 5, 7, 9], 5) == 2
assert binary_search([1, 3, 5, 7, 9], 4) == -1
assert binary_search([], 1) == -1
assert binary_search([2], 2) == 0
```

### P13：去重但保持顺序

文件：`p13_unique.py`

实现：

```python
def unique_keep_order(items):
    ...
```

要求：

- 返回去重后的新列表
- 保留第一次出现的顺序
- 可以使用 `set` 辅助

自测：

```python
assert unique_keep_order([3, 1, 3, 2, 1]) == [3, 1, 2]
assert unique_keep_order(["a", "b", "a"]) == ["a", "b"]
assert unique_keep_order([]) == []
```

### P14：前缀和

文件：`p14_prefix_sum.py`

实现：

```python
def prefix_sum(numbers):
    ...

def range_sum(prefix, left, right):
    ...
```

要求：

- `prefix_sum([2, 4, 6])` 返回 `[2, 6, 12]`
- `range_sum(prefix, left, right)` 返回原数组中从 `left` 到 `right` 的闭区间和
- 假设 `left` 和 `right` 都合法，且 `left <= right`

自测：

```python
p = prefix_sum([2, 4, 6, 8])
assert p == [2, 6, 12, 20]
assert range_sum(p, 0, 1) == 6
assert range_sum(p, 1, 3) == 18
assert range_sum(p, 2, 2) == 6
```

## 第四阶段：嵌套列表和矩阵思维

### P15：二维列表形状

文件：`p15_matrix_shape.py`

实现：

```python
def matrix_shape(matrix):
    ...

def is_rectangular(matrix):
    ...
```

要求：

- `matrix_shape([[1, 2], [3, 4]])` 返回 `(2, 2)`
- 空矩阵 `[]` 返回 `(0, 0)`
- `is_rectangular` 判断每一行长度是否相同

自测：

```python
assert matrix_shape([[1, 2], [3, 4]]) == (2, 2)
assert matrix_shape([]) == (0, 0)
assert is_rectangular([[1, 2], [3, 4]]) is True
assert is_rectangular([[1], [2, 3]]) is False
```

### P16：矩阵转置

文件：`p16_transpose.py`

实现：

```python
def transpose(matrix):
    ...
```

要求：

- 输入是规则二维列表
- 返回转置后的新二维列表
- 不要修改原矩阵

自测：

```python
m = [[1, 2, 3], [4, 5, 6]]
assert transpose(m) == [[1, 4], [2, 5], [3, 6]]
assert m == [[1, 2, 3], [4, 5, 6]]
assert transpose([]) == []
```

### P17：矩阵加法

文件：`p17_matrix_add.py`

实现：

```python
def matrix_add(a, b):
    ...
```

要求：

- 两个矩阵形状相同时，返回对应元素相加的新矩阵
- 形状不同时，返回 `None`

自测：

```python
assert matrix_add([[1, 2], [3, 4]], [[10, 20], [30, 40]]) == [[11, 22], [33, 44]]
assert matrix_add([[1, 2]], [[1], [2]]) is None
assert matrix_add([], []) == []
```

### P18：点积

文件：`p18_dot_product.py`

实现：

```python
def dot_product(a, b):
    ...
```

要求：

- `a` 和 `b` 是一维列表
- 长度相同时返回点积
- 长度不同时返回 `None`
- 先用循环实现

自测：

```python
assert dot_product([1, 2, 3], [4, 5, 6]) == 32
assert dot_product([1, 2], [3]) is None
assert dot_product([], []) == 0
```

## 第五阶段：文件、异常、模块

### P19：读取数字文件

文件：`p19_file_numbers.py`

实现：

```python
def read_numbers(path):
    ...
```

要求：

- 文件中每行一个整数
- 返回整数列表
- 空行跳过
- 如果文件不存在，让 Python 自然抛出异常即可，不要静默吞掉

自测：

```python
with open("numbers_test.txt", "w", encoding="utf-8") as f:
    f.write("1\n\n2\n3\n")

assert read_numbers("numbers_test.txt") == [1, 2, 3]
```

### P20：CSV 简易解析

文件：`p20_csv_parse.py`

实现：

```python
def parse_score_csv(path):
    ...
```

要求：

- CSV 每行格式：`name,score`
- 返回字典，例如 `{"Alice": 90, "Bob": 80}`
- 第一行不是表头
- 可以用字符串 `.split(",")`，也可以用标准库 `csv`

自测：

```python
with open("scores_test.csv", "w", encoding="utf-8") as f:
    f.write("Alice,90\nBob,80\n")

assert parse_score_csv("scores_test.csv") == {"Alice": 90, "Bob": 80}
```

### P21：安全除法

文件：`p21_exceptions.py`

实现：

```python
def safe_divide(a, b):
    ...

def parse_int_or_none(text):
    ...
```

要求：

- `safe_divide(a, b)`：如果 `b == 0`，返回 `None`
- `parse_int_or_none(text)`：能转成整数则返回整数，否则返回 `None`
- 练习 `try / except`

自测：

```python
assert safe_divide(6, 2) == 3
assert safe_divide(6, 0) is None
assert parse_int_or_none("123") == 123
assert parse_int_or_none("abc") is None
```

## 第六阶段：面向之后 ML 的纯 Python 练习

### P22：标签统计

文件：`p22_label_stats.py`

实现：

```python
def label_counts(labels):
    ...

def label_distribution(labels):
    ...
```

要求：

- `label_counts([0, 1, 1, 2])` 返回 `{0: 1, 1: 2, 2: 1}`
- `label_distribution` 返回每个标签的比例
- 空列表时，`label_distribution([])` 返回 `{}`

自测：

```python
assert label_counts([0, 1, 1, 2]) == {0: 1, 1: 2, 2: 1}
assert label_distribution([0, 1, 1, 2]) == {0: 0.25, 1: 0.5, 2: 0.25}
assert label_distribution([]) == {}
```

### P23：one-hot 编码的纯 Python 版本

文件：`p23_one_hot_python.py`

实现：

```python
def one_hot(labels, num_classes):
    ...
```

要求：

- 输入：`labels = [2, 0, 1]`
- 输出：`[[0, 0, 1], [1, 0, 0], [0, 1, 0]]`
- 先用列表和循环实现

自测：

```python
assert one_hot([2, 0, 1], 3) == [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
assert one_hot([], 3) == []
```

### P24：预测类别

文件：`p24_argmax.py`

实现：

```python
def argmax(values):
    ...

def predict_classes(logits):
    ...
```

要求：

- `argmax([0.1, 0.7, 0.2])` 返回 `1`
- 如果最大值重复，返回第一次出现的位置
- `predict_classes` 接收二维列表，返回每一行的最大值索引
- 不要用内置 `max` 的 `key` 参数，先自己写循环

自测：

```python
assert argmax([0.1, 0.7, 0.2]) == 1
assert argmax([5, 5, 1]) == 0
assert predict_classes([[0.1, 0.7], [3, 2], [1, 4]]) == [1, 0, 1]
```

### P25：分类准确率

文件：`p25_accuracy.py`

实现：

```python
def accuracy(predictions, labels):
    ...
```

要求：

- `predictions` 是预测类别列表
- `labels` 是真实类别列表
- 长度不一致时返回 `None`
- 空列表时返回 `0`

自测：

```python
assert accuracy([1, 0, 1], [1, 1, 1]) == 2 / 3
assert accuracy([], []) == 0
assert accuracy([1], [1, 0]) is None
```

### P26：mini-batch 切分

文件：`p26_batches.py`

实现：

```python
def make_batches(items, batch_size):
    ...
```

要求：

- 把列表按 `batch_size` 切成多个小列表
- 最后一个 batch 可以不足 `batch_size`
- `batch_size <= 0` 时返回 `None`

自测：

```python
assert make_batches([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
assert make_batches([1, 2, 3], 3) == [[1, 2, 3]]
assert make_batches([], 2) == []
assert make_batches([1, 2], 0) is None
```

### P27：数据集划分

文件：`p27_train_test_split.py`

实现：

```python
def train_test_split(items, test_ratio):
    ...
```

要求：

- 不打乱顺序
- `test_ratio` 是 `0` 到 `1` 之间的小数
- 返回 `(train_items, test_items)`
- 测试集数量用 `int(len(items) * test_ratio)`
- 测试集取列表最后一段

自测：

```python
train, test = train_test_split([1, 2, 3, 4, 5], 0.4)
assert train == [1, 2, 3]
assert test == [4, 5]

train, test = train_test_split([1, 2, 3], 0)
assert train == [1, 2, 3]
assert test == []
```

### P28：归一化的纯 Python 版本

文件：`p28_normalize_python.py`

实现：

```python
def min_max_normalize(values):
    ...
```

要求：

- 返回归一化后的新列表
- 公式：`(x - min_value) / (max_value - min_value)`
- 空列表返回 `[]`
- 如果最大值等于最小值，返回全 `0`

自测：

```python
assert min_max_normalize([10, 20, 30]) == [0.0, 0.5, 1.0]
assert min_max_normalize([5, 5, 5]) == [0, 0, 0]
assert min_max_normalize([]) == []
```

## 第七阶段：小综合练习

### P29：待办事项列表

文件：`p29_todo.py`

实现：

```python
def add_task(tasks, title):
    ...

def complete_task(tasks, index):
    ...

def active_tasks(tasks):
    ...
```

要求：

- `tasks` 是列表，每个任务是字典：`{"title": "learn", "done": False}`
- `add_task` 返回新列表，不修改原列表
- `complete_task` 返回新列表，把指定位置任务的 `done` 改成 `True`
- 如果 `index` 不合法，返回原任务列表的复制
- `active_tasks` 返回所有未完成任务标题

自测：

```python
tasks = []
tasks = add_task(tasks, "learn python")
tasks = add_task(tasks, "practice loops")
assert active_tasks(tasks) == ["learn python", "practice loops"]

done_tasks = complete_task(tasks, 0)
assert active_tasks(done_tasks) == ["practice loops"]
assert active_tasks(tasks) == ["learn python", "practice loops"]
```

### P30：简易词频统计器

文件：`p30_word_count.py`

实现：

```python
def word_count(text):
    ...

def top_k_words(text, k):
    ...
```

要求：

- 统一转小写
- 按空格分词即可
- `word_count("AI ai Python")` 返回 `{"ai": 2, "python": 1}`
- `top_k_words` 返回出现次数最高的前 `k` 个单词列表
- 次数相同时，先出现的单词排前面

自测：

```python
assert word_count("AI ai Python") == {"ai": 2, "python": 1}
assert top_k_words("a b a c b a", 2) == ["a", "b"]
assert top_k_words("", 3) == []
```

### P31：简易数据清洗

文件：`p31_clean_records.py`

实现：

```python
def clean_records(records):
    ...
```

要求：

- `records` 是字典列表，例如 `{"name": " Alice ", "age": "20", "score": "88"}`
- 返回清洗后的新列表
- `name` 去掉首尾空格
- `age` 转成整数
- `score` 转成浮点数
- 如果某条记录转换失败，跳过该记录

自测：

```python
records = [
    {"name": " Alice ", "age": "20", "score": "88.5"},
    {"name": "Bob", "age": "bad", "score": "70"},
]

assert clean_records(records) == [{"name": "Alice", "age": 20, "score": 88.5}]
```

### P32：训练日志分析

文件：`p32_training_log.py`

实现：

```python
def best_epoch(logs):
    ...

def loss_decreased_every_epoch(logs):
    ...
```

要求：

- `logs` 是字典列表，例如 `{"epoch": 1, "loss": 0.9, "accuracy": 0.6}`
- `best_epoch` 返回 accuracy 最高的 epoch；如果列表为空返回 `None`
- `loss_decreased_every_epoch` 判断 loss 是否每一轮都严格下降

自测：

```python
logs = [
    {"epoch": 1, "loss": 0.9, "accuracy": 0.6},
    {"epoch": 2, "loss": 0.7, "accuracy": 0.75},
    {"epoch": 3, "loss": 0.5, "accuracy": 0.72},
]

assert best_epoch(logs) == 2
assert loss_decreased_every_epoch(logs) is True
assert loss_decreased_every_epoch([{"epoch": 1, "loss": 0.5}, {"epoch": 2, "loss": 0.5}]) is False
```

## 建议的第一轮任务

先做这 3 道：

1. `P01：温度转换和数值计算`
2. `P02：条件判断`
3. `P03：循环和累加`

你写完后，把 `p01_basics.py`、`p02_conditions.py`、`p03_loops.py` 的代码发给我。我会先看正确性，再看代码风格和基础概念是否扎实。
