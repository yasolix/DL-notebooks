# DL-notebooks



## Spark on Keras and Elephas for Deep Learning Programing 
```bash
condauser@ubuntu-ibm-ust:~$ cat /etc/hosts
127.0.0.1    localhost
127.0.1.1    ubuntu-ibm-ust

10.1.34.235 ubuntu-ibm-ust
10.1.34.234 ubuntu-ibm-alt

##### The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```
 

Install Spark on master
```bash
wget https://d3kbcqa49mib13.cloudfront.net/spark-2.1.1-bin-hadoop2.7.tgz
tar -xvf spark-2.1.1-bin-hadoop2.7.tgz
ln -s spark-2.1.1-bin-hadoop2.7.tgz ~/spark
~/spark/sbin/start-master.sh 
spark/sbin/start-slave.sh spark://ubuntu-ibm-ust:7077
```
Install Spark on slave node(s)
```bash
wget https://d3kbcqa49mib13.cloudfront.net/spark-2.1.1-bin-hadoop2.7.tgz
spark/sbin/start-slave.sh spark://ubuntu-ibm-ust:7077
```
 

Install Python frame works for deep learning

elephas : https://github.com/maxpumperla/elephas
```bash
#Download Anaconda for the machine ( ppc for IBM powerPC only)
bash Anaconda3-4.4.0-Linux-ppc64le.sh
source .bashrc
conda install theano
pip install keras
# Update .keras/keras.json ; tensorflow -> theano
pip install elephas
```
 

Open Jupyter notebook on master node, specifying the GPU number and the spark master
```bash
condauser@ubuntu-ibm-ust:~$ THEANO_FLAGS=device=cuda0 MASTER="spark://ubuntu-ibm-ust:7077" SPARK_EXECUTOR_MEMORY="8G" PYSPARK_DRIVER_PYTHON=ipython PYSPARK_DRIVER_PYTHON_OPTS="notebook" ~/spark/bin/pyspark --master spark://ubuntu-ibm-ust:7077
```
