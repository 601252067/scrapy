# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KczjItem(scrapy.Item):
    # 卡车之家全国经销商数据

    # 商家名称
    shop_name = scrapy.Field()
    # 标签信息1
    shop_tag_1 = scrapy.Field()
    # 标签信息2
    shop_tag_2 = scrapy.Field()
    # 标签信息3
    shop_tag_3 = scrapy.Field()
    # 商铺地址
    shop_addr = scrapy.Field()
    # 商铺电话
    shop_tel = scrapy.Field()


    # 车名
    # car_name = scrapy.Field()
    # car_tag_1 = scrapy.Field()
    # car_tag_2 = scrapy.Field()
    # car_tag_3 = scrapy.Field()
    # car_tag_4 = scrapy.Field()
    # car_hot = scrapy.Field()
    # car_factory_price = scrapy.Field()
    # car_location_price = scrapy.Field()
    # # 价格
    # car_price = scrapy.Field()
    # # 车的型号
    # car_type = scrapy.Field()
    # # 驱动形式
    # car_power = scrapy.Field()
    # # 轴距
    # car_wheelbase = scrapy.Field()
    # # 发动机
    # car_engine = scrapy.Field()
    # # 变速箱
    # car_gearbox = scrapy.Field()
    # # 后桥速比
    # car_ratio = scrapy.Field()
    # # 车身长度
    # car_long = scrapy.Field()
    # # 车身宽度
    # car_width = scrapy.Field()
    # # 车身高度
    # car_height = scrapy.Field()
    # # 轮距
    # car_track = scrapy.Field()
    # # 整车重量
    # car_weight = scrapy.Field()
    # # 总重量
    # total_weight = scrapy.Field()
    # # 牵引总重量
    # traction_total_weight = scrapy.Field()
    # # 最高车速
    # max_speed = scrapy.Field()
    # # 产地
    # car_origin = scrapy.Field()
    # # 吨位
    # tonnage_level = scrapy.Field()
    # # 气缸数量
    # car_cylinder_num = scrapy.Field()
    # # 燃料种类
    # fuel_type = scrapy.Field()
    # # 气缸排列
    # cylinder_range = scrapy.Field()
    # # 排量
    # car_displacement = scrapy.Field()
    # # 排放标准
    # emission_standards = scrapy.Field()
    # # 最大马力
    # car_max_power = scrapy.Field()
    # # 最大输出功率
    # car_max_output_power = scrapy.Field()
    # # 扭矩
    # car_torque = scrapy.Field()
    # # 最大扭矩转速
    # max_torque_speed = scrapy.Field()
    # # 额定转速
    # rated_speed = scrapy.Field()
    # # 准乘人数
    # ride_num = scrapy.Field()
    # # 座位类型
    # seat_type = scrapy.Field()
    # # 换挡方式
    # shift_mode = scrapy.Field()
    # # 前进档位
    # forward_gear =scrapy.Field()
    # # 倒档数量
    # reverse_gear =scrapy.Field()
    # # 轮胎数
    # tire_num = scrapy.Field()
    # # 油箱容量
    # tank_capacity = scrapy.Field()