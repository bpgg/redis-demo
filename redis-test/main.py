import time

import redis

# 直接连接

# r = redis.Redis(host='localhost', port= 6379)


# 连接池连接
pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool=pool)

# 记录当前时间
time_start = time.time()

# 1万次写
for i in range(10000):
    data = {'username': 'bpgg', 'age': 28}

    # r.hmset("users" + str(i), data) 方法过时
    r.hset("users" + str(i), 'username', 'bpgg')

# 统计写时间
delta_time = time.time() - time_start
print(delta_time)

# 记录当前时间
time_start = time.time()

# 1万次读
for i in range(10000):
    # result = r.mhget("users" + str(i), ['username', 'age']) 方法不存在
    result = r.mget("users" + str(i), 'username')

# 统计读时间
delta_time = time.time() - time_start
print(delta_time)
