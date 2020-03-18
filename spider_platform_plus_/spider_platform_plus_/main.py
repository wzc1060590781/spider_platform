from spider_platform_plus_.config import con
from spider_platform_plus_.core.engine import Engine

if __name__ == '__main__':
    engin = Engine(con)
    engin.start_engine()