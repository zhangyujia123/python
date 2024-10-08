import json

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

f_china=open("D:/可视化案例数据/地图数据/疫情.txt",encoding="utf-8")
data=f_china.read()
f_china.close()
data_dict=json.loads(data)
data_dict=data_dict['areaTree'][0]['children']
data_list=[]
for i in data_dict:
    name=i['name']
    if name=='新疆':
        name='新疆维吾尔自治区'
    elif name=='西藏' or name=='内蒙古':
        name=name+'自治区'
    elif name=='重庆'or name=='北京' or name=='天津' or name=='上海':
        name=name+'市'
    else:
        name=name+'省'
    num=i['total']['confirm']
    data_list.append((name,num))
# print(data_list)
map=Map()
map.add("各省份确诊人数",data_list,"china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(is_show=True,
    is_piecewise=True,
    pieces=[
        {"min": 1, "max": 99, "lable": "1~99人", "color": "#CCFFFF"},
        {"min": 100, "max": 999, "lable": "100~9999人", "color": "#FFFF99"},
        {"min": 1000, "max": 4999, "lable": "1000~4999人", "color": "#FF9966"},
        {"min": 5000, "max": 9999, "lable": "5000~99999人", "color": "#FF6666"},
        {"min": 10000, "max": 99999, "lable": "10000~99999人", "color": "#CC3333"},
        {"min": 100000, "lable": "100000+", "color": "#990033"}
    ]
                                 )
)
map.render()

