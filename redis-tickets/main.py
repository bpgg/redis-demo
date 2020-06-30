import redis
import threading

# 创建线程池
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
# 初始化redis
r = redis.StrictRedis(connection_pool=pool)

# 设置key
KEY = "ticket_count"


# 模拟第i个用户进行抢票
def sell(i):
    # 初始化pipe
    pipe = r.pipeline()
    while True:
        try:
            # 监视票数
            pipe.watch(KEY)
            # 查看当前票数
            c = int(pipe.get(KEY))
            if c > 0:
                # 开启事务
                pipe.multi()
                c = c - 1
                pipe.set(KEY, c)
                pipe.execute()
                print('用户 {} 抢票成功，当前票数 {}'.format(i, c))
                break
            else:
                print('用户 {} 抢票失败，票售空了'.format(i))
        except  Exception as e:
            print('用户 {} 抢票失败，请重新尝试'.format(i))
            continue
        finally:
            pipe.unwatch()


if __name__ == "__main__":
    print('start========')
    # 初始化5张票
    r.set(KEY, 5)
    print(r)
    # 设置8个人抢票
    for i in range(8):
        t = threading.Thread(target=sell, args=(i,))
        t.start()
    print("end=========")

# if __name__ == "__main__": 确保不会调用导入模块里面的main方法
