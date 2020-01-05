import tensorflow as tf
import matplotlib.pyplot as plt ,matplotlib.image as mimage
from tensorflow.examples.tutorials.mnist import input_data
mnistData = input_data.read_data_sets('MNIST_data/',one_hot=True)
X = tf.placeholder(tf.float32,[None,784],name='X')
Y = tf.placeholder(tf.float32,[None,10],name='Y')
#创建学习变量、权重和偏置
w = tf.Variable(tf.zeros([784,10]),name='w')
b = tf.Variable(tf.zeros([10],name='b'))
#创建逻辑回归模型。TensorFlow OP 给出了 name_scope（"wx_b"）
with tf.name_scope("wx_b") as scope:
    y_hat = tf.nn.softmax(tf.matmul(X,w)+b)
# 训练时添加 summary 操作来收集数据。使用直方图以便看到权重和偏置随时间相对于彼此值的变化关系。可以通过 TensorBoard Histogtam 选项卡看到
w_h = tf.summary.histogram('weight',w)
b_h = tf.summary.histogram('biases',b)
#定义交叉熵（cross-entropy）和损失（loss）函数，并添加 name scope 和 summary 以实现更好的可视化。使用 scalar summary 来获得随时间变化的损失函数。scalar summary 在 Events 选项卡下可见
with tf.name_scope("cross_entropy") as scope:
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=Y,logits=y_hat))
    tf.summary.scalar('cross_entropy',loss)
#采用 TensorFlow GradientDescentOptimizer，学习率为 0.01。为了更好地可视化，定义一个 name_scope：
with tf.name_scope("Train") as scope:
    optimizar = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
#为变量进行初始化
init = tf.global_variables_initializer()
#组合所有的 summary 操作：
merged_all_op = tf.summary.merge_all()
#现在，可以定义会话并将所有的 summary 存储在定义的文件夹中：
max_epochs = 100  #训练集个数
batch_size = 12 #单次训练用的样本数
with tf.Session() as sess:
    sess.run(init)
    graphs_op = tf.summary.FileWriter('graphs',sess.graph)
    for epoch in range(max_epochs):
        log_avg = 0
        num_of_batch = int(mnistData.train.num_examples/batch_size)
        for i in range(num_of_batch):
            batch_xs,batch_ys = mnistData.train.next_batch(100)
            _,l,summary_srt = sess.run([optimizar,loss,merged_all_op],feed_dict={X:batch_xs,Y:batch_ys})
            log_avg +=1
            graphs_op.add_summary(summary_srt,epoch * num_of_batch + i)
            log_avg = log_avg/num_of_batch
    # 取得y得最大概率对应的数组索引来和y_的数组索引对比，如果索引相同，则表示预测正确
    correct_prediction = tf.equal(tf.argmax(y_hat, 1), tf.arg_max(Y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print('Epoch {0}:Loss {1}'.format(epoch,log_avg))
    print('Done')
    print(sess.run(accuracy,feed_dict={X:mnistData.test.images,Y:mnistData.test.labels}))
