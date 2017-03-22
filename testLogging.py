#_*_ coding:utf-8 _*_
#Logging to a file
import os
import logging
FILE = os.getcwd()          #返回当前目录的路径
#logging基础配置，文件名为 os.path.join里面的两个值想加个，输出等级为≥DEBUG级别
logging.basicConfig(filename = os.path.join(FILE,'log.txt'),level = logging.DEBUG,
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

# 2017-03-22 16:19:41,269 test.py[line:16]DEBUG 调试
#日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
logging.critical('致命的')
logging.error('错误')
logging.warning('警告')
logging.info('信息')
logging.debug('调试')
