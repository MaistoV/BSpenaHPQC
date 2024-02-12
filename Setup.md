# Environment Setup

## Overview <a name="Overview"></a>
Virtual machine running **Ubuntu 22.04 LTS** :
  * 8 GB of RAM 
  * 4 cores
  * 150 GB of memory

## Tools
### Java 1.8
* Install
```bash
$ sudo apt install openjdk-8-jdk
```

* Setting the JAVA_HOME environment variable 
```bash
$ sudo nano /etc/environment                    
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"   # Add this line to the end of the file
$ source /etc/environment                       
$ sudo reboot                                   
$ echo $JAVA_HOME                               
```

### Maven 3.6
```bash
sudo apt-get -y install maven
```

> [!NOTE]
> [Here](https://maven.apache.org/guides/getting-started/index.html) the Maven doc.

### Hadoop 3.3.5 <a name="hadoop_3.3.5"></a>
```bash
$ git clone https://github.com/apache/hadoop.git --branch rel/release-3.3.5 --single-branch
```

### Native libraries
```bash
$ sudo apt-get -y install build-essential autoconf automake libtool cmake zlib1g-dev pkg-config libssl-dev libsasl2-dev
```

### Protocol Buffers 3.7.1
It is required to build native code
```bash
$ curl -L -s -S https://github.com/protocolbuffers/protobuf/releases/download/v3.7.1/protobuf-java-3.7.1.tar.gz -o protobuf-3.7.1.tar.gz
$ mkdir protobuf-3.7-src
$ tar xzf protobuf-3.7.1.tar.gz --strip-components 1 -C protobuf-3.7-src && cd protobuf-3.7-src
$ ./configure
$ make -j$(nproc)
$ sudo make install
```
### Other Packages
* Snappy compression (only used for hadoop-mapreduce-client-nativetask)
```bash
$ sudo apt-get install snappy libsnappy-dev
```
* Bzip2
```bash
$ sudo apt-get install bzip2 libbz2-dev
```
* Linux FUSE
```bash
$ sudo apt-get install fuse libfuse-dev
```
* ZStandard compression
```bash
$ sudo apt-get install libzstd1-dev
```

### SSH and PDSH
* Install 
```bash
$ sudo apt-get install ssh
$ sudo apt-get install pdsh
```
* Setup passphraseless ssh

```bash
# Check that you can ssh to the localhost without a passphrase
$ ssh localhost

# If you cannot ssh to localhost without a passphrase, execute the following commands
$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
$ chmod 0600 ~/.ssh/authorized_keys
```

## Build ???
```bash
$ mvn package -Pdist -Dtar -DskipTests
$ mvn compile -Pdist -Dtar -DskipTests
$ mvn package -Pdist,native -DskipTests -Dtar   # https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/NativeLibraries.html
```


* hadoop/hadoop-dist/target/hadoop-3.3.5/

## EC 
bin/hdfs ec -listPolicies  --> Lists all (enabled, disabled and removed) erasure coding policies registered in HDFS. Only the enabled policies are suitable for use with the setPolicy command.