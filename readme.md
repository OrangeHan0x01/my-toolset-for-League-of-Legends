环境需求：
python3（建议安装anaconda,可以通过visual studio安装，我的是visual studio2017，可以直接装anaconda，免去了很多步骤）
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
		python herohelper.py -s 位置的英文称呼（看一下hero_data.txt就知道了）
lolScreen.py:小地图位置的像素放大并放在小窗口，可以拖到副屏，刷新频率和像素（放大前和放大后）应该在.py文件中根据自己的电脑调整，我的游戏界面分辨率是1920*1080的，不同分辨率也会导致小地图变化，要自己改
最新数据获取日期：2020/7/29



