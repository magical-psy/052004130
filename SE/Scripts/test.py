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
table = table.drop(['香港', "澳门", "台湾"], axis=1)
# print(table)


date = table.iloc[:, 0].values

my_data = []
for index, day in enumerate(date):
    data = []
    for province in table.columns.values[2:]:
        data.append({
            "name": province, "value": [float(table.loc[index, province]), 1, province]
        })
    dict = {
        "time": date[index],
        "data": data,
    }
    my_data.append(dict)



def get_year_chart(year: str):
    map_data = [
        [[x["name"], x["value"]] for x in d["data"]] for d in my_data if d["time"] == year
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
                range_color=["lightskyblue", "green", "yellow"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    bar_x_data = [x[0] for x in map_data]

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
                range_color=["lightskyblue",  "green", "yellow"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    grid_chart = (
        Grid()
            .add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="60", pos_right="55%", pos_top="20%", pos_bottom="10"
            ),
        )
            .add(
            map_chart, grid_opts=opts.GridOpts(pos_right="25%"),
        )
    )

    return grid_chart


# Draw Timeline

def get_timeline():
    time_list = date
    timeline = Timeline(
        init_opts=opts.InitOpts(height="700px",width="1800px", theme=ThemeType.DARK)
    )
    for y in time_list:
        g = get_year_chart(year=y)
        timeline.add(g, time_point=str(y))

    timeline.add_schema(
        orient="vertical",
        is_auto_play=True,
        is_inverse=True,
        play_interval=7000,
        pos_left="null",
        pos_right="5",
        pos_top="20",
        pos_bottom="20",
        width="50",
        # label_opts=opts.LabelOpts(is_show=True, color="#4c9812",font_weight="900"),
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
