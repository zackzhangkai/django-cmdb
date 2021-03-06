#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django import forms

class UploadFile(models.Model):
  #title = models.CharField(max_length=50,default="")
  #上传至年月日目录下
  #upload = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True)
  #上传至指定目录下
  upload = models.FileField(upload_to='uploads/',blank=True) #文件上传是key-value形式的，key为upload，value为上传的内容
class UploadFileForm(forms.ModelForm):
  class Meta:
    model = UploadFile
    fields=('upload',)

class LoadToDB(models.Model):
  loadtodb = models.FileField(upload_to='uploads/',blank=True)
class LoadToDBForm(forms.ModelForm):
  class Meta:
    model = LoadToDB
    fields=('loadtodb',)


class CmdbInfo(models.Model):
  ip=models.GenericIPAddressField()
  hostname=models.CharField(max_length=250)
  password=models.CharField(max_length=250)
  lable=models.CharField(max_length=250)
  IDC = 'IDC'
  SH = 'SH'
  WH = 'WH'
  area_choice = (
    (IDC, 'IDC'),
    (SH, 'SH'),
    (WH, 'WH'),
  )
  area=models.CharField(
    max_length=3,
    choices=area_choice,
    default=IDC,
  )
  Centos7 = 'Centos7'
  Centos6 = 'Centos6'
  Windows = 'Windows'
  os_choice = (
    (Centos7,'Centos7'),  
    (Centos6,'Centos6'),
    (Windows,'Windows'),
  )
  os=models.CharField(
    max_length=250,
    choices=os_choice,
    default=Centos7,
  )
  info=models.CharField(max_length=250,blank=True) 
# null针对数据库而言，若null=True，则数据库的该字段可以为空，blank针对表单而言，若blank=true，则在表单填写时可以为空
  def __unicode__(self):
    return self.ip  

class CmdbInfoForm(forms.ModelForm):
  class Meta:
    model = CmdbInfo
    fields = ('ip','hostname','password','lable','info','os','area',) # 使用DRY原则

class Article(models.Model):
  title=models.CharField(u'标题',max_length=256)
  context=models.TextField(u'内容')
 
  pub_date=models.DateTimeField(u'发表时间',auto_now_add=True,editable=True)
  update_time=models.DateTimeField(u'更新时间',auto_now_add=True,null=True)

  def __unicode__(self):
    return self.title


class Person(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  
  def my_property(self):
    return self.first_name + ' ' + self.last_name
  my_property.shor_description="Full name of the person"

  full_name=property(my_property)


