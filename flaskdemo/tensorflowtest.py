import tensorflow as tf
# message = tf.constant('welcom learn tensorflow') # 1节

# v1=tf.constant([1,2,3,4])  # 2节
# v2 = tf.constant([2,1,5,3])
# v3 = tf.add(v1,v2)

# sess = tf.InteractiveSession() #3节  默认session结合 .eval()使用
# v1 = tf.constant([1,2,3,4])
# v2= tf.constant([2,1,5,3])
# v_add = tf.add(v1,v2)
# print(v_add.eval())
# sess.close

# 常量相关
# v_zrro  = tf.zeros([3,2],tf.int32)
# v_one  = tf.ones([3,2],tf.int32)
# v_line = tf.linspace(2.0,5.0,5) #等差排布的序列
# v_range = tf.range(1,10) #数字序列，增量为 delta（默认值=1）
# v_random_normal = tf.random_normal([2,3],mean=2.0,stddev=1.0,seed=12) #形状为 [M，N] 的正态分布随机数组
# v_truncated_normal = tf.truncated_normal([2,3],mean=2.0,stddev=3.0,seed=12) #形状为 [M，N] 的截尾正态分布随机数组
# v_random_uniform = tf.random_uniform([2,5],maxval=4,seed=12) #形状为 [M，N] 的给定伽马分布随机数组
# v_crop = tf.random_crop(v_random_uniform,[2,3],seed=12) # 将给定的张量随机裁剪为指定的大小
# v_shuffle = tf.random_shuffle(v_random_uniform) # 沿着它的第一维随机排列张量
# tf.set_random_seed(54) #为所有随机产生的张量设置种子

# with tf.Session() as session:
#     print(session.run(v_a))
#变量相关

# v_value = tf.random_uniform([2,3],maxval=4,seed=12)
# v_a = tf.Variable(v_value)
# v_b = tf.Variable(v_value)
# sess = tf.InteractiveSession()
# init = tf.global_variables_initializer()
# sess.run(init)
# print(v_a.eval())
# print(v_b.eval())
#
# saver = tf.train.Saver() #使用 Saver 类来保存变量

