import pandas as pd
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Page

"""
Gallery 使用 pyecharts 1.0.0
参考地址: https://gallery.echartsjs.com/editor.html?c=xSkGI6zLmb

目前无法实现的功能:

1、
"""
table = pd.read_excel('../data.xlsx', sheet_name="每日确诊")
row = table.iloc[[0]]
print(table.iloc[:,0].values)
date=[12345, 2000, 2005, 2010, 2015]

my_data=[]

data = [
    {
        "time": "123",
        "data": [
            {"name": "台湾", "value": [1000, 133, "台湾"]},
            {"name": "香港", "value": [432.47, 2, "香港"]},
            {"name": "江苏", "value": [319.8, 2, "江苏"]},
            {"name": "西藏", "value": [311.89, 2, "西藏"]},
            {"name": "山东", "value": [292.13, 2, "山东"]},
            {"name": "辽宁", "value": [281, 2, "辽宁"]},
            {"name": "西藏", "value": [2000, 2, "西藏"]},
            {"name": "广东", "value": [249.65, 2, "广东"]},
            {"name": "四川", "value": [229.31, 2, "四川"]},
            {"name": "河南", "value": [229.16, 2, "河南"]},
            {"name": "黑龙江", "value": [221, 2, "黑龙江"]},
        ],
    },
    {
        "time": 2000,
        "data": [
            {"name": "台湾", "value": [27435.15, 19.47, "台湾"]},
            {"name": "香港", "value": [14201.59, 10.08, "香港"]},
            {"name": "广东", "value": [10741.25, 7.62, "广东"]},
            {"name": "江苏", "value": [8553.69, 6.07, "江苏"]},
            {"name": "山东", "value": [8337.47, 5.92, "山东"]},
            {"name": "浙江", "value": [6141.03, 4.36, "浙江"]},
            {"name": "河南", "value": [5052.99, 3.59, "河南"]},
            {"name": "河北", "value": [5043.96, 3.58, "河北"]},
            {"name": "上海", "value": [4771.17, 3.39, "上海"]},
            {"name": "辽宁", "value": [4669.1, 3.31, "辽宁"]},
        ],
    },
    {
        "time": 2005,
        "data": [
            {"name": "台湾", "value": [30792.89, 12.52, "台湾"]},
            {"name": "广东", "value": [22527.37, 9.16, "广东"]},
            {"name": "江苏", "value": [18598.69, 7.56, "江苏"]},
            {"name": "山东", "value": [18366.87, 7.47, "山东"]},
            {"name": "香港", "value": [14869.68, 6.05, "香港"]},
            {"name": "浙江", "value": [13417.68, 5.46, "浙江"]},
            {"name": "河南", "value": [10587.42, 4.3, "河南"]},
            {"name": "河北", "value": [10043.42, 4.08, "河北"]},
            {"name": "上海", "value": [9247.66, 3.76, "上海"]},
            {"name": "辽宁", "value": [8047.3, 3.27, "辽宁"]},
        ],
    },
    {
        "time": 2010,
        "data": [
            {"name": "广东", "value": [46036.25, 9.49, "广东"]},
            {"name": "江苏", "value": [41425.48, 8.54, "江苏"]},
            {"name": "山东", "value": [39169.92, 8.08, "山东"]},
            {"name": "台湾", "value": [30205.64, 6.23, "台湾"]},
            {"name": "浙江", "value": [27747.65, 5.72, "浙江"]},
            {"name": "河南", "value": [23092.36, 4.76, "河南"]},
            {"name": "河北", "value": [20394.26, 4.21, "河北"]},
            {"name": "辽宁", "value": [18457.3, 3.81, "辽宁"]},
            {"name": "四川", "value": [17185.48, 3.54, "四川"]},
            {"name": "上海", "value": [17165.98, 3.54, "上海"]},
        ],
    },
    {
        "time": 2015,
        "data": [
            {"name": "广东", "value": [72812.55, 9.35, "广东"]},
            {"name": "江苏", "value": [70116.38, 9, "江苏"]},
            {"name": "山东", "value": [63002.3, 8.09, "山东"]},
            {"name": "浙江", "value": [42886, 5.51, "浙江"]},
            {"name": "河南", "value": [37010.25, 4.75, "河南"]},
            {"name": "台湾", "value": [32604.52, 4.19, "台湾"]},
            {"name": "四川", "value": [30103.1, 3.87, "四川"]},
            {"name": "河北", "value": [29806.1, 3.83, "河北"]},
            {"name": "湖北", "value": [29550.19, 3.8, "湖北"]},
            {"name": "湖南", "value": [29047.2, 3.73, "湖南"]},
        ],
    },
]


def get_year_chart(year: int):
    map_data = [
        [[x["name"], x["value"]] for x in d["data"]] for d in data if d["time"] == year
    ][0]
    min_data, max_data = (
        min([d[1][0] for d in map_data]),
        max([d[1][0] for d in map_data]),
    )
    map_chart = (
        Map()
            .add(
            series_name="",
            data_pair=map_data,
            label_opts=opts.LabelOpts(is_show=False),
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="中国每日确诊",
                subtitle="人",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=JsCode(
                    """function(params) {
                    if ('value' in params.data) {
                        return params.data.value[2] + ': ' + params.data.value[0];
                    }
                }"""
                ),
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="center",
                range_text=["最高", "最低"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    bar_x_data = [x[0] for x in map_data]

    # 这里注释的部分会导致 label 和 value 与 饼图不一致
    # 使用下面的 List[Dict] 就可以解决这个问题了。
    # bar_y_data = [x[1][0] for x in map_data]
    bar_y_data = [{"name": x[0], "value": x[1][0]} for x in map_data]
    bar = (
        Bar()
            .add_xaxis(xaxis_data=bar_x_data)
            .add_yaxis(
            series_name="",
            yaxis_index=1,
            y_axis=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b}: {c}"
            ),
        )
            .reversal_axis()
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="center",
                range_text=["gao", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
            graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(
                        rotation=JsCode("Math.PI / 4"),
                        bounding="raw",
                        right=110,
                        bottom=110,
                        z=100,
                    ),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(left="center", top="center", z=100),
                            graphic_shape_opts=opts.GraphicShapeOpts(width=400, height=50),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="rgba(0,0,0,0.3)"
                            ),
                        ),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(left="center", top="center", z=100),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text=f"{str(year)} 年",
                                font="bold 26px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="#fff"),
                            ),
                        ),
                    ],
                )
            ],
        )
    )


    grid_chart = (
        Grid()
            .add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="10", pos_right="45%", pos_top="70%", pos_bottom="5"
            ),
        )
            .add(map_chart, grid_opts=opts.GridOpts())
    )

    return grid_chart


# Draw Timeline

def get_timeline():
    time_list = date
    timeline = Timeline(
        init_opts=opts.InitOpts(height="900px", theme=ThemeType.DARK)
    )
    for y in time_list:
        g = get_year_chart(year=y)
        timeline.add(g, time_point=str(y))

    timeline.add_schema(
        orient="vertical",
        is_auto_play=True,
        is_inverse=True,
        play_interval=5000,
        pos_left="null",
        pos_right="5",
        pos_top="20",
        pos_bottom="20",
        width="50",
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )
    return timeline


def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)  # 简单布局
    # 将上面定义好的图添加到 page
    page.add(
        get_timeline()
    )
    page.render("../templates/homepage.html")


page_simple_layout()
