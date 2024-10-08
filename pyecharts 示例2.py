import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts

# 打开文件
f_us=open("D:/可视化案例数据/折线图数据/美国.txt","r",encoding="utf-8")
f_jp=open("D:/可视化案例数据/折线图数据/日本.txt","r",encoding="utf-8")
f_in=open("D:/可视化案例数据/折线图数据/印度.txt","r",encoding="utf-8")
# 读出数据
us_date=f_us.read()
jp_date=f_jp.read()
in_data=f_in.read()
# 美国数据处理
us_date=us_date.replace("jsonp_1629344292311_69436(","")
us_date=us_date[:-2]
us_json=json.loads(us_date)
us_json=us_json['data'][0]['trend']
us_x_data=us_json['updateDate'][:314]
us_y_data=us_json['list'][0]['data'][:314]
# 日本数据处理
jp_date=jp_date.replace("jsonp_1629350871167_29498(","")
jp_date=jp_date[:-2]
jp_json=json.loads(jp_date)
jp_json=jp_json['data'][0]['trend']
jp_x_data=jp_json['updateDate'][:314]
jp_y_data=jp_json['list'][0]['data'][:314]
# 印度数据处理
in_data=in_data.replace("jsonp_1629350745930_63180(","")
in_data=in_data[:-2]
in_json=json.loads(in_data)
in_json=in_json['data'][0]['trend']
in_x_data=in_json['updateDate'][:314]
in_y_data=in_json['list'][0]['data'][:314]

line=Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国疫情",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本疫情",jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度疫情",in_x_data,label_opts=LabelOpts(is_show=False))
line.set_global_opts(
    title_opts=TitleOpts(title="美日印疫情图",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
line.render()
f_in.close()
f_us.close()
f_jp.close()