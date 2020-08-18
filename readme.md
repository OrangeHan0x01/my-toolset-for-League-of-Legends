8.18更新：添加了英雄总胜率和登场率的数据；-n会额外显示英雄登场率和胜率信息，并在括号中显示克制/被克制英雄的登场率；克制得分计算中加入了通过登场率得到的权重；


考虑到这些工具并不是给技术人员使用的，我会尽量讲得简单些，爬虫工具暂时不在这里提供，担心有些人不会用结果被封ip。（毕竟低年龄段贪玩的玩家很多）
虽然这些工具代码量不多，作者可能依然要很久才会有心思更新一次，但是更新版本过几个星期后肯定会尽量更新一次数据。
之后的更新会考虑加入英雄装备胜率统计等功能，之后如果有时间作者可能会去申请拳头开发者api，做阵容胜率统计和策略分析（大概率会坑）

环境需求：(windows系统下)

python3（建议安装anaconda,可以通过visual studio安装，我的是visual studio2017，可以直接一键装anaconda，免去了很多步骤）
python库需求:（通过conda命令行中运行：pip install 库名 -i https://pypi.tuna.tsinghua.edu.cn/simple 可以通过国内镜像源安装，不然有些库可能下载不下来）(我就不写requirements文件了）

小地图放大工具：
	pyautogui
	tkinter
	pillow
	opencv-python
	
爬虫工具：
	BeautifulSoup
	
运行：conda命令行中跳转至目录下（cd），执行：python .py文件名 参数

工具及文件说明：

data_update.py:爬虫，不需要参数。通过op.gg获取英雄数据，保存至hero_data.py，建议不要经常更新，不然可能会被op.gg屏蔽ip，每次更新工具包时都会给上最新数据并附带日期
herohelper.py:英雄胜率查询工具，从hero_data.txt中统计数据，使用时可以用python herohelper.py -h查询参数
		python herohelper.py -n 英雄名
		python herohelper.py -s 位置的英文称呼（看一下hero_data.txt就知道了）	此外，该工具还有给出op.gg上英雄装备胜率统计的选项，但还没做（没爬）
lolScreen.py:小地图位置的像素放大并放在小窗口，可以拖到副屏，刷新频率和像素（放大前和放大后）应该在.py文件中根据自己的电脑调整，我的游戏界面分辨率是1920*1080的，不同分辨率也会导致小地图变化，要自己改

最新数据获取日期：2020/8/18



