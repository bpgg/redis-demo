# Redis

`REmote DIctionary Server`

## Redis简介

+ 键值数据库，哈希存储。
+ 基于内存
+ 单进程单线程模型
+ 多路 I/O 复用技术


单进程单线程模型：避免了上下文切换和不必要的线程之间引起的资源竞争

多路 I/O 复用技术：多个 socket 网络连接，复用同一个线程。

## 数据类型

字符串、哈希、列表、集合、有序集合等

## 基本使用

### 字符串

+ 设置某个键的值

```sql
set key value
# 例
set name zhangfei
```

+ 获取某个键的值

```sql
get key
# 例
get name
```

### hash

+ 设置某个键的hash值

```sql
hset key field value
# 例
hset user1 username zhangfei
hset user1 age 28

# 批量添加
hmset key field value [field value...]
# 例
Hmset user1 username zhangfei age 28
```

+ 获取某个键的field字段

```sql
hget key field
# 例
hget user1 username
```

+ 获取某个键的多个 field 字段值

```sql
hmget key field[field...]
# 例
hmget user1 username age
```

### list

字符串列表（list）的底层是一个双向链表结构

+ 左侧增加元素

```sql
LPUSH key value [...]
# 例
LPUSH heroList zhangfei guanyu liubei
```

+ 右侧添加元素

```sql
RPUSH key value [...]
# 例
RPUSH heroList dianwei lvbu
```

+ 获取列表的范围内容

```sql
LRANGE key start stop
# 例
LRANGE heroList 0 4
```

### set

+ 在集合中添加元素

```sql
SADD key member [...]
# 例
SADD heroSet zhangfei guanyu liubei dianwei lvbu
```

+ 删除元素

```sql
SREM key member [...]
# 例
SREM heroSet liubei lvbu
```

+ 获取集合所有元素

```sql
SMEMBERS key
# 例
SMEMBERS heroSe
```

+ 判断集合中是否存在某个元素

```sql
SISMEMBER heroSet zhangfei
SISMEMBER heroSet liubei
```

### 有序集合

SortedSet，简称 `ZSET`

在集合的基础上增加了一个分数属性，这个属性在添加修改元素的时候可以被指定。每次指定后，ZSET 都会按照分数来进行自动排序，也就是说我们在给集合 key 添加 member 的时候，可以指定 score。

+ 添加元素和分数

```sql
ZADD key score member [...]
# 例
ZADD heroScore 8341 zhangfei 7107 guanyu 6900 liubei 7516 dianwei 7344 lvbu
```

+ 获取某个元素的Score

```sql
ZSCORE key member
# 例
ZSCORE heroScore guanyu
```

+ 删除一个或多元素

```sql
ZREM key member
# 例
ZREM heroScore gunyu
```

+ 获取某个范围的元素列表

WITHSCORES 是个可选项，如果使用 WITHSCORES 会将分数一同显示出来

```sql
# 从小到大
RANGE key start stop [WITHSCORES]

# 从大到小
ZREVRANGE key start stop [WITHSCORES]

# 例
ZREVRANGE heroScore 0 2 WITHSCORES
```

## redis连接池

在连接池的实例中会有两个 list，保存的是_available_connections和_in_use_connections，它们分别代表连接池中可以使用的连接集合和正在使用的连接集合。当我们想要创建连接的时候，可以从_available_connections中获取一个连接进行使用，并将其放到_in_use_connections中。如果没有可用的连接，才会创建一个新连接，再将其放到_in_use_connections中。如果连接使用完毕，会从_in_use_connections中删除，添加到_available_connections中，供后续使用

Redis 库提供了 Redis 和 StrictRedis 类，
它们都可以实现 Redis 命令，不同之处在于 Redis 是 StrictRedis 的子类，可以对旧版本进行兼容

## redis事务

Redis 不支持事务的回滚机制（Rollback），
这也就意味着当事务发生了错误（只要不是语法错误），
整个事务依然会继续执行下去，直到事务队列中所有命令都执行完毕

+ 为何不支持回滚呢？

因为只有当编程语法错误的时候，Redis 命令执行才会失败。这种错误通常出现在开发环境中，而很少出现在生产环境中，没有必要开发事务回滚功能。

### redis事务处理命令

1. MULTI：开启一个事务；
2. EXEC：事务执行，将一次性执行事务内的所有命令；
3. DISCARD：取消事务；
4. WATCH：监视一个或多个键，如果事务执行前某个键发生了改动，那么事务也会被打断；
5. UNWATCH：取消 WATCH 命令对所有键的监视。

## 出现问题

redis.exceptions.ConnectionError: Error 10061 connecting to localhost:6379. 由于目标计算机积极拒绝，无法连接。.

原来是我没有安装redis，我天真的以为python会自动安装启动。

windows的同学在这里下载：[redis](https://github.com/rgl/redis/downloads)

redis学习手册下载：[《Redis快速入门》](https://redis.io/topics/quickstart)

