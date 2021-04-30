# Demo01

#### 使用命令

创建项目 `scrapy startproject 项目名称`

创建爬虫 `scrapy genspider demo01 demo01.com`

创建爬虫 `scrapy genspider 爬虫名 允许爬取的主机名`

启动爬虫 `scrapy crawl 爬虫名`

#### 文件及文件夹解释

`scrapy.cfg` 项目配置文件

`items.py` 定义数据字段，防止数据字段出错

`pipelines.py` 管道，数据处理入库操作

`middlewares.py` 中间件，爬虫中间件和下载中间件

`settings.py` 爬虫配置文件

`spiders` 存放爬虫脚本文件的文件夹
