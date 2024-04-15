#!/bin/bash

# Stop HDFS deamons, YARN deamons and JobHistoryServer (if any)
echo "[INFO] Stopping DFS, YARN and JobHistoryServer"
$HADOOP_HOME/sbin/stop-dfs.sh                      
$HADOOP_HOME/sbin/stop-yarn.sh
$HADOOP_HOME/bin/mapred --daemon stop historyserver

# Clear the data directory
echo "[INFO] Clearing tmp data from DFS"
rm -rf /tmp/hadoop-$(whoami)/dfs/data/*

# Format the filesystem
echo "[INFO] Formatting DFS"
# echo Y | $HADOOP_HOME/bin/hdfs namenode -format > /dev/null

# Start HDFS deamons,YARN deamons and JobHistoryServer
echo "[INFO] Starting DFS, YARN and JobHistoryServer"
$HADOOP_HOME/sbin/start-dfs.sh                     
$HADOOP_HOME/sbin/start-yarn.sh
$HADOOP_HOME/bin/mapred --daemon start historyserver

# Deactivate NameNode Safemode for simplicity
echo "[INFO] Deactivating NameNode safemode"
hdfs dfsadmin -safemode leave

# Make the HDFS directories required to execute MapReduce jobs
# TODO: is this necessary?
$HADOOP_HOME/bin/hdfs dfs -mkdir /user             
$HADOOP_HOME/bin/hdfs dfs -mkdir /user/$(whoami)
