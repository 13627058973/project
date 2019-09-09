# coding:utf-8

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def get_category():
    category_list = [
        # {
        #     "name": "神经系统用药",
        #     "code": "AB"
        # },
        {
            "name": "抗菌药物",
            "code": "AA"
        },
        {
            "name": "消化系统用药",
            "code": "AC"
        },
        {
            "name": "心脑血管药",
            "code": "AD"
        },
        {
            "name": "泌尿生殖系统用药",
            "code": "AE"
        },
        {
            "name": "呼吸系统用药",
            "code": "AF"
        },
        {
            "name": "血液系统药物",
            "code": "AG"
        },
        {
            "name": "解热镇痛抗炎抗痛风",
            "code": "AH"
        },
        {
            "name": "激素类用药",
            "code": "AI"
        },
        {
            "name": "肝胆用药",
            "code": "AJ"
        },
        {
            "name": "清热药",
            "code": "AK"
        },
        {
            "name": "一般外用药",
            "code": "AL"
        },
        {
            "name": "滋补养生",
            "code": "AM"
        },
        {
            "name": "维生素和矿物质",
            "code": "AN"
        },
        {
            "name": "妇科用药",
            "code": "AO"
        },
        {
            "name": "儿科用药",
            "code": "AP"
        },
        {
            "name": "其他",
            "code": "AQ"
        },
        # {
        #     "name": "普通诊察器械",
        #     "code": "BA"
        # },
        # {
        #     "name": "康复理疗",
        #     "code": "BB"
        # },
        # {
        #     "name": "家庭健身用品",
        #     "code": "BC"
        # },
        # {
        #     "name": "成人用品",
        #     "code": "BD"
        # },
        # {
        #     "name": "医疗专用",
        #     "code": "BE"
        # },
        # {
        #     "name": "贵细滋补",
        #     "code": "CA"
        # },
        {
            "name": "中药饮片",
            "code": "CB"
        },
        # {
        #     "name": "保健外用品",
        #     "code": "B111"
        # },
        # {
        #     "name": "女士保健食品",
        #     "code": "DA"
        # },
        # {
        #     "name": "男士保健食品",
        #     "code": "DB"
        # },
        # {
        #     "name": "儿童保健食品",
        #     "code": "DC"
        # },
        # {
        #     "name": "中老年保健食品",
        #     "code": "DD"
        # },
        # {
        #     "name": "综合养生",
        #     "code": "DE"
        # },
        # {
        #     "name": "维矿物质",
        #     "code": "DF"
        # },
        # {
        #     "name": "进口保健食品",
        #     "code": "H"
        # },
        # {
        #     "name": "进口保健食品",
        #     "code": "I"
        # },
        # {
        #     "name": "护肤用品",
        #     "code": "EA"
        # },
        # {
        #     "name": "口腔护理",
        #     "code": "EB"
        # },
        # {
        #     "name": "身体护理",
        #     "code": "EC"
        # },
        # {
        #     "name": "儿童用品",
        #     "code": "ED"
        # },
        # {
        #     "name": "女性用品",
        #     "code": "EE"
        # },
        # {
        #     "name": "男性用品",
        #     "code": "EF"
        # },
        # {
        #     "name": "日用百货",
        #     "code": "FA"
        # },
        # {
        #     "name": "日用食品",
        #     "code": "FB"
        # }
    ]
    return category_list
