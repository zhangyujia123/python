import json

from pyecharts.charts.basic_charts.map import MapMixin, Map
from pyecharts.options import VisualMapOpts

f_hn=open("D:/可视化案例数据/地图数据/疫情.txt","r",encoding="utf-8")
data=json.loads(f_hn.read())
f_hn.close()
hn_data=data['areaTree'][0]['children'][3]['children']
hn_list=[]
for i in hn_data:
    name=i['name']+'市'
    num=i['total']['confirm']
    hn_list.append((name,num))
map=Map()
map.add("河南省疫情地图",hn_list,"河南")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(is_show=True,
    is_piecewise=True,
    pieces=[
        {"min": 1, "max": 9, "lable": "1~9人", "color": "#CCFFFF"},
        {"min": 10, "max": 99, "lable": "10~99人", "color": "#FFFF99"},
        {"min": 100, "max": 499, "lable": "100~499人", "color": "#FF9966"},
        {"min": 500, "max": 999, "lable": "500~999人", "color": "#FF6666"},
        {"min": 1000, "max": 9999, "lable": "1000~9999人", "color": "#CC3333"},
        {"min": 10000, "lable": "10000+", "color": "#990033"}
    ]
                                 )
)
map.render()