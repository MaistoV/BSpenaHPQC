# Troubleshooting

## Error 1
* **Error Cause** : Building Hadoop without running the tests
```bash
$ mvn package -Pdist -DskipTests -Dtar
```
* **Error Message** : Failed to execute goal com.github.eirslett:frontend-maven-plugin:1.6:yarn (yarn install)
* **Solution** : Check the output of the command. If there is this kind of messagge "error triple-beam@1.4.1: The engine "node" is incompatible with this module. Expected version ">= 14.0.0". Got "12.22.1" [INFO] error Found incompatible module.", go to the pom.xml file 
```bash

```

## Error 2
* **Error Cause** : 
```bash

```
* **Error Message** : 
* [**Solution**]() : 
```bash

```

## Error 3
* **Error Cause** : Start NameNode daemon and DataNode daemon in order to run a MapReduce job locally (Hadoop cluster in **Pseudo-Distributed Mode**)
```bash
$ sbin/start-dfs.sh
```
* **Error Message** : Permission denied
* [**Solution**](https://stackoverflow.com/questions/42756555/permission-denied-error-while-running-start-dfs-sh) : 
```bash
# Check if your pdsh's default rcmd is rsh
$ pdsh -q -w localhost

# Modify pdsh's default rcmd to ssh
$ nano ~/.bashrc
export PDSH_RCMD_TYPE=ssh
$ source ~/.bashrc
```

## Error 4
* **Error Cause** : Copy the input files into the distributed filesystem in order to run a MapReduce job locally (Hadoop cluster in **Pseudo-Distributed Mode**)
```bash
$ bin/hdfs dfs -mkdir -p /user/<username>
```
* **Error Message** : mkdir: Call From <username>-VirtualBox/127.0.1.1 to localhost:9000 failed on connection exception: java.net.ConnectException: Connection refused
* [**Solution**](https://stackoverflow.com/questions/28661285/hadoop-cluster-setup-java-net-connectexception-connection-refused) : 
```bash
$ sbin/stop-all.sh                  # All deamons will stop
$ bin/hadoop namenode -format
$ sbin/start-all.sh                 # All deamons will start
```

## Error 5
* **Error Cause** : Start ResourceManager daemon and NodeManager daemon in order to run a MapReduce job on YARN in a pseudo-distributed mode (Hadoop cluster in **Pseudo-Distributed Mode**)
```bash
$ sbin/start-yarn.sh
```
* **Error Message** : resourcemanager is running as process 9365.  Stop it first and ensure /tmp/hadoop-spena-resourcemanager.pid file is empty before retry
* [**Solution**](https://stackoverflow.com/questions/14273620/error-in-namenode-starting) : 
```bash
$ sbin/stop-all.sh
$ jps                   # Check java processes running
$ sbin/start-all.sh
$ jps

# If NameNodes doesn't appear in java processes running list, check the error through
$ bin/hadoop namenode
```


### 
WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable spena@spena-VirtualBox:~/hadoop/hadoop-dist/targe  

$ mvn package -Pdist,native -DskipTests -Dtar

https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/NativeLibraries.html