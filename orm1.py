# 如何在一个python脚本或文件中加载django项目的配置和变量信息
import os
if __name__ == '__main__':
    # 加载项目配置
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_senior.settings")
    import django
    django.setup()
    from app01 import models
    # # 查询所有的人
    # ret = models.Person.objects.all()
    # print(ret)
    #
    # # get查询
    # ret = models.Person.objects.get(id=1)
    # print(ret)
    # # ret = models.Person.objects.get(name="逼逼") # 返回值
    # # print(ret)
    # ret = models.Person.objects.filter(name="逼逼") # 返回对象
    # print(ret)
    # ret = models.Person.objects.filter(id__gt=1) # 返回id大于1 的对象
    # print(ret)
    # ret = models.Person.objects.filter(id=100) # 不存在返回一个空的QuerySet，不报错
    # print(ret)
    # print("exclude".center(80, "="))
    # ret = models.Person.objects.exclude(id=1)
    # print(ret)
    # print("value".center(80, "="))
    # ret = models.Person.objects.values("name","birthday")
    # print(ret)
    # print("value list".center(80, "="))
    # ret = models.Person.objects.values_list("name","birthday") # 列表元祖形式返回值
    # print(ret)
    # print("order by".center(80, "="))
    # ret = models.Person.objects.order_by("birthday")
    # print(ret)
    # print("reverse".center(80, "="))
    # ret = models.Person.objects.order_by("id").reverse() # 对有序的QuerySet才能调用reverse
    # print(ret)
    # print("count".center(80, "="))
    # ret = models.Person.objects.all().count()
    # print(ret)
    # print("first".center(80, "="))
    # ret = models.Person.objects.all().first()
    # print(ret)
    # print("last".center(80, "="))
    # ret = models.Person.objects.all().last()
    # print(ret)
    # print("exists".center(80, "="))
    # ret = models.Book.objects.exists()
    # print(ret)

    # # 双下划线
    # # id 大于1小于4
    # ret = models.Person.objects.filter(id__gt=1, id__lt=4)
    # print(ret)
    # # id 在某个范围
    # ret = models.Person.objects.filter(id__in=[1,3,5])
    # print(ret)
    # # 排除id在某个范围
    # ret = models.Person.objects.exclude(id__in=[1,3,5])
    # print(ret)
    # # contains
    # ret = models.Person.objects.filter(name__contains="逼")
    # # ret = models.Person.objects.filter(name__icontains="apple") # 大小写不敏感
    # print(ret)
    # # range 判断id在哪个区间 between and 1<= <=3
    # ret = models.Person.objects.filter(id__range=[1,3])
    # # startswith, endswith, istartswith, iendswith
    # # 日期和时间字段还可以有以下写法
    # ret = models.Person.objects.filter(birthday__year=1997) # 返回生日年份为1997的对象
    # # ret = models.Person.objects.filter(birthday__month=1)
    # print(ret)
    # # 外键查询——正向查询
    # book_obj = models.Book.objects.all().first()
    # ret = book_obj.publisher.name
    # print(ret)
    #
    # # 查询id为1的书的出版社名称
    # ret = models.Book.objects.filter(id=5).values("publisher__name") # 双下划线表示跨表查询字段
    # print(ret)
    #
    # 反向查询
    # 基于对象
    # publisher_obj = models.Publisher_list.objects.first()
    # ret = publisher_obj.books.all()
    # print(ret)
    # 基于双下划线
    # ret = models.Publisher_list.objects.filter(id=4).values_list("xxoo__title")
    # print(ret)

    # 多对多
    # author_obj = models.Author.objects.first()
    # print(author_obj)
    # ret = author_obj.book.all()
    # print(ret)
    #
    # create 通过作者创建书，会自动保存
    # author_obj.book.create(title="docker实战", publisher_id=2)
    # INSERT INTO `app01_book` (`title`, `publisher_id`) VALUES ('docker实战', 2); args=['docker实战', 2]
    # INSERT INTO `app01_author_book` (`author_id`, `book_id`) VALUES (1, 8); args=(1, 8)
    #
    # add
    # book_obj = models.Book.objects.get(id=4)
    # author_obj.book.add(book_obj)
    #
    # book_objs = models.Book.objects.filter(id__gt=6)
    # author_obj.book.add(*book_objs) # 要把列表打散
    #
    # remove
    # book_obj = models.Book.objects.get(title="docker实战")
    # author_obj.book.remove(book_obj)
    # 按id删除
    # author_obj.book.remove(7)
    #
    #
    # clear 清空
    # author_obj = models.Author.objects.get(name="王逼逼")
    # author_obj.book.clear()

    # # 聚合
    from django.db.models import Avg, Sum, Max, Min, Count
    # # ret = models.Book.objects.all().aggregate(Avg("price"))
    # # print(ret)
    #
    # ret = models.Book.objects.all().aggregate(price_sum=Sum("price"), price_max=Max("price"), price_min=Min("price"))
    # print(ret)
    # print(ret.get("price_sum"))

    # # 分组
    # ret = models.Book.objects.all().annotate(author_num=Count("author"))
    # print(ret)
    # for book in ret:
    #     print("书名{}，作者数量{}".format(book, book.author_num))

    # # 查询作者数量大于1的作者
    # ret = models.Book.objects.all().annotate(author_num=Count("author")).filter(author_num__gt=1)
    # print(ret)
    # for book in ret:
    #     print("书名{}，作者数量{}".format(book, book.author_num))

    # 查询各个作者出的书的总价格
    # ret = models.Author.objects.all().annotate(price_sum=Sum("book__price")).values_list("name","price_sum")
    # print(ret)

    # F和Q
    # ret = models.Book.objects.filter(price__gt=9.99)
    # print(ret)

    # 查询出库存数大于卖出数的所有书 （两个字段作比较）
    from django.db.models import F
    # ret = models.Book.objects.filter(kucun__gt=F("sold"))
    # print(ret)

    # # 刷单 把每本书卖出数乘以3
    # models.Book.objects.update(sold=(F("sold")+1)*3)

    # # 给每一本书的书名后面加上 第一版
    # from django.db.models.functions import Concat
    # from django.db.models import Value
    # models.Book.objects.update(title=Concat(F("title"), Value(" 第一版")))

    # # Q查询
    # ret = models.Book.objects.filter(sold__gt=1000, price__lt=100)
    # print(ret)

    # # 查询卖出数大于1000且价格小于100的所有书
    # from django.db.models import Q
    # # ret = models.Book.objects.filter(Q(sold__gt=1000) | Q(price__lt=100))
    # # print(ret)
    # ret = models.Book.objects.filter(Q(sold__gt=1000) | Q(price__lt=100), title__contains="python")
    # print(ret)

    author_obj = models.Author.objects.get(id=1)
    obj = author_obj.detail
    print(obj)
    print("爱好 {} 住址 {}".format(obj.hobby, obj.addr))
