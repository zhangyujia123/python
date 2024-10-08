from cProfile import label

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map=Map()
data=[
    ("北京市",99),
    ("上海市",199),
    ("天津市",100),
    ("重庆市",300),
    ("台湾省",799)
]
map.add("测试地图",data,"china")
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