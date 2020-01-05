import numpy as np
import tensorflow as tf
import tensorflow.contrib as tc
import matplotlib.pyplot as plt
#归一化数据
def normalize(x):
    mean = np.mean(x)
    std = np.std(x)
    x = (x-mean)/std
    return x
datas = tc.learn.datasets.load_boston()
x_train,y_trant = datas.data[:,5],datas.target

X = tf.placeholder(tf.float32,name='X')
Y = tf.placeholder(tf.float32,name='Y')

w =tf.Variable(0.0)
b =tf.Variable(0.0)

Y_hat = X*w + b
#定义损失函数
loss = tf.square(Y-Y_hat,name='loss')
#选择梯度下降优化器
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)
#声明初始化操作符
init_op = tf.global_variables_initializer()
#开始计算图，训练 100 次
with tf.Session() as sess:
    sess.run(init_op)
    writer = tf.summary.FileWriter('graph',sess.graph)
    for i in range(100):
        for x,y in zip(x_train,y_trant):
            _,l = sess.run([optimizer,loss],feed_dict={X:x,Y:y})
    writer.close()
    b_value,w_value = sess.run([b,w])
#查看结果
Y_pred = x_train * w_value + b_value
print("Done")
plt.plot(x_train,y_trant,'bo')
plt.plot(x_train,Y_pred,'r')
plt.show()
# print(x_train)
# print(y_trant)