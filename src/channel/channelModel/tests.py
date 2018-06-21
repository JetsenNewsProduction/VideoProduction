# -*- coding: utf-8 -*-

from django.test import TestCase
from django.http import HttpResponse
from channelModel.models import PpnCdmChannel

# 数据库操作
def testdb(request):
    # 初始化
    response = ""

    # 获取单个对象
    response1 = PpnCdmChannel.objects.get(chan_id='A82D5050-4992-4052-BF1F-DEC053667CF2')
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = PpnCdmChannel.objects.filter(chan_id='A82D5050-4992-4052-BF1F-DEC053667CF2')
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    PpnCdmChannel.objects.order_by('chan_name')[0:2]
    # 数据排序
    PpnCdmChannel.objects.order_by("chan_code")
    # 上面的方法可以连锁使用
    PpnCdmChannel.objects.filter(chan_name="runoob").order_by("id")

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = PpnCdmChannel.objects.all()

    # 输出所有数据
    for var in list:
        response += var.chan_name + "； "
    return HttpResponse("<p>" + response + "</p>")
