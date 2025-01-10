import tensorflow as tf

print(tf.version)

n = tf.zeros([5,5,5,5])

n = tf.reshape(n , [125 , -1])

print(n)

print()

