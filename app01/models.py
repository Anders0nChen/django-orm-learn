from django.db import models
import datetime
# Create your models here.
class Publisher_list(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=68, null=False, unique=True)
    addr = models.CharField(max_length=128, default="No address here.")

    def __str__(self):
        return "<Publisher Object: {}>".format(self.name)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    kucun = models.IntegerField(default=1000)
    sold = models.IntegerField(default=0)
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
    name = models.CharField(max_length=16, null=False)
    book = models.ManyToManyField(to="Book")
    phone = models.IntegerField(default=None)
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
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=18)
    birthday = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = "person_table"

class AuthorDetail(models.Model):
    hobby = models.CharField(max_length=32)
    addr = models.CharField(max_length=128)


# 自己创建作者和书的关联表
# 此时在ORM层面，作者和书就没了多对多关系
# class Author2Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     author_id = models.ForeignKey(to="Author")
#     book_id = models.ForeignKey(to="Book")
#