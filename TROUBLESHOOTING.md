# Problemi incontrati
## Setting up a Single Node Cluster
* "Permission denied" esguendo "$ sbin/start-dfs.sh" [Soluzione](https://stackoverflow.com/questions/42756555/permission-denied-error-while-running-start-dfs-sh) 
* "mkdir: Call From spena-VirtualBox/127.0.1.1 to localhost:9000 failed on connection exception: java.net.ConnectException: Connection refused;" eseguento "$ bin/hdfs dfs -mkdir -p /user/<username>" [Soluzione](https://stackoverflow.com/questions/28661285/hadoop-cluster-setup-java-net-connectexception-connection-refused)
* "resourcemanager is running as process 9365.  Stop it first and ensure /tmp/hadoop-spena-resourcemanager.pid file is empty before retry." eseguendo sbin/start-yarn.sh [Soluzione](https://stackoverflow.com/questions/14273620/error-in-namenode-starting) --> jps controlla i processi java in esecuzione
* "INFO retry.RetryInvocationHandler: java.net.ConnectException: Your endpoint configuration is wrong;" eseguendo "$ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.5.jar grep input output 'dfs[a-z.]+'" [Soluzione](https://stackoverflow.com/questions/50968183/java-net-connectexception-your-endpoint-configuration-is-wrong)


## Building Hadoop without running the tests
* 'build.plugins.plugin.version' for org.codehaus.mojo:findbugs-maven-plugin is missing. @ line 74, column 15 https://stackoverflow.com/questions/4123044/maven-3-warnings-about-build-plugins-plugin-version
