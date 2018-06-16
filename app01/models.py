from django.db import models
import datetime
# Create your models here.
class Publisher_list(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=68, null=False, unique=True, verbose_name="出版社名")
    addr = models.CharField(max_length=128, default="No address here.", verbose_name="地址")

    def __str__(self):
        return "<Publisher Object: {}>".format(self.name)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True, verbose_name="书名")
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, verbose_name="售价")
    kucun = models.IntegerField(default=1000, verbose_name="库存")
    sold = models.IntegerField(default=0, verbose_name="售出")
    # 和出版社关联的外键
    publisher = models.ForeignKey(
        to="Publisher_list",
        on_delete=models.CASCADE, # 表示级联操作，软关联
        db_constraint=False,
        related_name="books",
        related_query_name="xxoo", # 反向双下划线查询
    )

    def __str__(self):
        return "<Book Object: {}>".format(self.title)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False, verbose_name="姓名")
    # book = models.ManyToManyField(to="Book", through="Author2Book", through_fields=("author", "book",))
    book = models.ManyToManyField(to="Book")
    phone = models.IntegerField(default=None, verbose_name="电话")
    detail = models.OneToOneField(to="AuthorDetail", null=True, on_delete=models.DO_NOTHING,)

    def __str__(self):
        return "<Author Object: {}>".format(self.name)


class FixedCharField(models.Model):
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(FixedCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' % self.max_length


class Person(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")
    age = models.IntegerField(default=18, verbose_name="年龄")
    birthday = models.DateField(auto_now_add=True, verbose_name="生日")


    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = "person_table"

class AuthorDetail(models.Model):
    hobby = models.CharField(max_length=32, verbose_name="爱好")
    addr = models.CharField(max_length=128, verbose_name="住址")


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    salary = models.IntegerField()
    province = models.CharField(max_length=32)
    dept = models.CharField(max_length=16)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "employee"


class EmployeeB(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    salary = models.IntegerField()
    province = models.CharField(max_length=32)
    dept = models.ForeignKey(to="Dept", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "employeeb"


class Dept(models.Model):
    name = models.CharField(max_length=16, unique=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "dept"

# class Author2Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     author = models.ForeignKey(to="Author", on_delete=models.DO_NOTHING)
#     book = models.ForeignKey(to="Book", on_delete=models.DO_NOTHING)
#     memo = models.CharField(max_length=64, null=True)

# 自己创建作者和书的关联表
# 此时在ORM层面，作者和书就没了多对多关系
# class Author2Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     author_id = models.ForeignKey(to="Author")
#     book_id = models.ForeignKey(to="Book")
#

# git test
# lalala


# git test
# 修复bug 18点43分


# =======

# git test
# 开发功能中。。。。 50% 18点41分

# git test
# 开发完成！！！ 100% 20点19分

# github test
# github提交测试！！！