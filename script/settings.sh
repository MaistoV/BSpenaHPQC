echo "[INFO] Adding master SSH identity"
ssh-add ~/.ssh/master_id_rsa

# Setup Hadoop environment
# echo "[INFO] Setting up Hadoop environment"
# # Hadoop variables begin
# export HADOOP_HOME=/home/hadoop/hadoop_installations/hadoop-3.4.0   
# export HADOOP_INSTALL=$HADOOP_HOME
# export HADOOP_MAPRED_HOME=$HADOOP_HOME
# export HADOOP_COMMON_HOME=$HADOOP_HOME
# export HADOOP_HDFS_HOME=$HADOOP_HOME
# export YARN_HOME=$HADOOP_HOME
# export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
# export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
# export HADOOP_OPTS=-Djava.library.path=$HADOOP_HOME/lib/native
# export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.352.b08-2.el8_6.x86_64/jre/
# # Hadoop variables end

alias python=python3.11
echo "[INFO] python now aliases on python3.11"

# PDSH as SSH
export PDSH_RCMD_TYPE=ssh
echo "[INFO] PDSH remote command type is now ssh"
