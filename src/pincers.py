# -*- coding: utf-8 -*-


import gzip
import re
import jieba


class BasePincer:
    """
    使用行政区划数据处理地址字符
    数据例子：
            "code": 110101017000,
            "name": "永定门外街道",
            "level": 4,
            "pcode": 110101000000
            "category": 110101000000
    """

    def __init__(self, gz_path="areas/area_code_2024.csv.gz"):
        """"""
        self.areas = self.areas_from_compressed_csv(gz_path)
        self.area_names = set([area[1] for area in self.areas if len(area[1]) > 1])

    def load_jieba_dict(self):
        for name in self.area_names:
            jieba.add_word(name)

    def jieba_split(self, address):
        """
        jieba地址分词
        """
        address = re.sub("\s+", "", address)
        result = list(jieba.cut(address))
        return result

    def re_split(self, address):
        """
        正则地址分词
        """
        address = re.sub("\s+", "", address)
        rule = re.compile("(?<=省|市|区|县|乡|镇|村|路|楼|号)")
        result = rule.split(address)
        return result

    def standard(self, split_address):
        """
        地址标准化
        """

    @staticmethod
    def areas_from_compressed_csv(gz_path):
        """
        文件每一列依次为：
            "code": 区划代码,
            "name": 名称,
            "level": 级别1-5,省市县镇村,
            "pcode": 父级区划代码,
            "category":城乡分类,
        """
        areas = []
        with gzip.open(gz_path, "rb") as f:
            for line in f.readlines():
                items = line.decode().strip().split(",")

                format_s = [
                    int(items[0]),
                    items[1],
                    int(items[2]),
                    int(items[3]),
                    int(items[3]),
                ]
                areas.append(format_s)

        return areas
