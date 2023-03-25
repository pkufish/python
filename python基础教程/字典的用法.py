# 先定义一个字典

# 字典是一个可以用来存储键和它们对应的值的数据结构。它们允许您根据该键快速查找其值。在Python中，字典是一种映射类型，其中键和值之间的关系由一对大括号组成。

# 以下示例用于演示如何在Python中创建字典：

my_dict = {
    "name": "John",
    "age": 30,
    "location": "New York"
}

# 一旦定义了字典，就可以通过键访问其值。

# 下面的示例显示了如何使用字典的键来访问其值：

name = my_dict["name"] # sets name to "John"
age = my_dict["age"] # sets age to 30
location = my_dict["location"] # sets location to "New York"

# 你也可以利用字典键来修改值，以下示例将字典中age字段的值更改为25

my_dict["age"] = 25  # sets age to 25

# 你也可以使用数组新增键和值

my_dict["hobby"] = "Football"  # sets hobby to "Football"

# Python有一个功能，称为字典推导，可以用一句简洁的代码创建字典，例如：

new_dict = {str(i): i*i for i in range(10)}

# 这会创建一个包含由字符串作为键和乘方结果作为值的字典，范围从0-9.例如，新字典的“1”键的值将是1的平方，即1.

# 你还可以使用一个字典来创建另一个字典。

another_dict = {key: value for key, value in my_dict.items()}

# 这会创建my_dict和another_dict完全一样的字典。

# 另一个有用的字典功能是迭代。迭代键、值或键值对。例如，要迭代出字典中的所有值，可以使用for循环：
if __name__ == '__main__':
    for value in my_dict.values():
        print(value)

# 这将输出my_dict中的所有值。