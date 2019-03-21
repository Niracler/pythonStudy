# python-exercise

> 关于python的面试题及leetcode题目代码实现

## 目录

## Python基础

### 文件操作

1. [写一个返回该文件夹中文件的路径,以及其包含文件夹中文件的路径的函数](interview_question/print_dir.py)

### 模块与包

1. [函数输入为年月日，输出这是该年的第几天](interview_question/get_date.py)

1. [打乱一个排好序的list对象alist？](interview_question/upset_a_list.py)

### 数据类型

1. [现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?](interview_question/sort_dicts.py)

1. [请反转字符串 "aStr"?](interview_question/reverse_str.py)

1. [将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}](interview_question/to_dicts.py)

1. [请按alist中元素的age由大到小排序](interview_question/sort_list.py)

1. 下面代码的输出结果将是什么？
    ```python
    list1 = ['a','b','c','d','e']
    print(list1[10:])
    ```
    代码将会输出[]， 不会产生IndexError错误， 就像所期望的那样，尝试用超出成员的个数的index来获取某个列表的成员。例如尝试获取list[10]和之后的成员，会导致IndexError。然而， 尝试获取列表的切片，开始的index超过了成员个数不会产生IndexError， 而是仅仅返回一个空列表。这成为特别让人恶心的疑难杂症， 因为运行的时候没有产生错误，导致BUG很难被追踪到。

1. [写一个列表生成式，产生一个公差为11的等差数列](interview_question/gen_list.py)

1. [给定两个列表，怎么找出他们相同的元素和不同的元素？(集合)](interview_question/different_list.py)

1. [请写出一段python代码实现删除list里面的重复元素？](interview_question/dif_sim.py)

### 企业面试题

1. Python新式类与经典类的区别？  
  a. Python里凡是继承了object的类都是新式类  
  b. Python3中只有新式类  
  c. Python2中继承object的类是新式类,没有写父类的是经典类  
  d. 经典类目前在Python中基本没有应用  

2. Python中内置数据结构有几种?  
  int, str, float, complex, long(Python3中没有, 只有无限精度的int)  
  list, tuple, set, dict  

3. Python中如何实现单例模式? 请写出至少两种实现方法  
    第一种方法:[使用装饰器](interview_question/singleton.py)  
    第二种方法:[使用基类new](interview_question/singleton.py), 是真正创建实例对象的方法,所以重写基类的new方法,以此保证创建对象的时候只生成一个实例  
    ~~第三种方法:[元类](interview_question/singleton.py), 元类是用于创建类对象的类,类对象创建实例对象时一定要调用call方法, 因此在调用call时候始终只创建一个实例即可,type是Python的元类~~

4. [反转一个整数，例如-123 --> -321](interview_question/reverse_int.py)

5. [设计实现遍历目录与子目录，抓取.py文件](interview_question/os_test.py)

6. [一行代码实现1-100之和](interview_question/one_line_add.py)

7. [Python-遍历列表时删除元素的正确做法](interview_question/del_list.py)

8. [字符串的操作题目](interview_question/str_operation.py)

9. 可变类型与比可变类型  
  a. 可变类型有list,dict, 不可变类型有tuple, number, string  
  b. 当进行修改操作时,可变类型传递的是内存中的地址,也就是说,直接修改内存中的值,并没有开辟新的内存  
  c. 不可变类型被修改时,并没有改变原来内存地址中的值,而是开辟一块新的内存,将原来地址中的之复制进去,对这块新开辟的内存中的值进行操作

10. is和==有什么区别?  
  is: 比较的是两个对象的id是否相等,也就是比较两对象是否为同一个实例对象.是否指向同一个内存地址  
  ==: 比较两个对象的内容/值是否相等, 默认会调用对象的eq()方法
  
11. [求出列表所有奇数并构造新列表 ](interview_question/odd_number.py)

12. Python中变量的作用域?(变量查找顺序)  
    函数作用域的LEGB顺序  
    a. 什么是LEGB?  
    L: local函数内部作用域   
    E: enclosing 函数内部与内嵌函数之间  
    G: global全局作用域  
    B: build-in 内置作用域  
    python在函数中的查找分为4种, 称之为LEGB,也正是按照这种顺序来查找的  
    
13. 

## LeetCode热门面试问题

### Array

1. [两个数相加的和等于某个数](leetcode/two_sum.py)

1. [将零放到最后](leetcode/move_zeros.py)

1. [找单个出现的值](leetcode/single_number.py)

1. [list的交集](leetcode/intersect.py)

1. [一个存在列表里的数,你将它加1(高精度加法)](leetcode/plus_one.py)

1. [不新建一个二维列表旋转图片](leetcode/rotate_image.py)

1. [买卖股票的最好时间及最大收益分析](leetcode/max_profit.py)

1. [列表中是否有重复的元素？](leetcode/contains_duplicate.py)

1. [列表挪位](leetcode/rotate_array.py)

## 参考文章

- [关于python的面试题](https://github.com/Niracler/python-interview-question)  
- [python-exercises](https://www.w3resource.com/python-exercises/)
