"""
 * Project name(项目名称)：Python面向对象
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 20:00
 * Version(版本): 1.0
 * Description(描述)：
 类：可以理解是一个模板，通过它可以创建出无数个具体实例。比如，前面编写的 tortoise 表示的只是乌龟这个物种，
 通过它可以创建出无数个实例来代表各种不同特征的乌龟（这一过程又称为类的实例化）。
对象：类并不能直接使用，通过类创建出的实例（又称对象）才能使用。这有点像汽车图纸和汽车的关系，
图纸本身（类）并不能为人们使用，通过图纸创建出的一辆辆车（对象）才能使用。
属性：类中的所有变量称为属性。例如，tortoise 这个类中，bodyColor、footNum、weight、hasShell 都是这个类拥有的属性。
方法：类中的所有函数通常称为方法。不过，和函数所有不同的是，类方法至少要包含一个 self 参数。
例如，tortoise 类中，crawl()、eat()、sleep()、protect() 都是这个类所拥有的方法，类方法无法单独使用，只能和类的对象一起使用。
 """


class Tortoise:
    bodyColor = "绿色"
    footNum = 6
    weight = 13
    hasShell = True

    # 会爬
    def crawl(self):
        print("乌龟会爬")

    # 会吃东西
    def eat(self):
        print("乌龟吃东西")

    # 会睡觉
    def sleep(self):
        print("乌龟在睡觉")

    # 会缩到壳里
    def protect(self):
        print("乌龟缩进了壳里")
