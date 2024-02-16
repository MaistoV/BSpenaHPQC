# Environment Setup

Virtual machine running **Ubuntu 22.04 LTS** :
  * 8 GB of RAM 
  * 4 cores
  * 150 GB of memory

## Tools <a name="tool"></a>

### Java 1.8 <a name="java1.8"></a>
* Install
```bash
$ sudo apt install openjdk-8-jdk
```

* Setting JAVA_HOME environment variable 
```bash
$ sudo nano /etc/environment                    
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"   # Add this line to the end of the file
$ source /etc/environment                       
$ sudo reboot                                   
$ echo $JAVA_HOME                         
```

### Maven 3.6 <a name="maven3.6"></a>
```bash
sudo apt-get -y install maven
```

### Hadoop 3.3.5 <a name="hadoop3"></a>
* Install
```bash
$ git clone https://github.com/apache/hadoop.git --branch rel/release-3.3.5 --single-branch
```
* Setting HADOOP_HOME environment variable
```bash
$ nano ~/.bashrc                                      # Open the bashrc file
export HADOOP_HOME=/path/to/hadoop-3.3.5/directory    # Add at the end of the file
$ source  ~/.bashrc                                   # For changes to take effect
```

### Libraries <a name="l"></a>

* Native libraries
```bash
$ sudo apt-get -y install build-essential autoconf automake libtool cmake zlib1g-dev pkg-config libssl-dev libsasl2-dev
```

* Protocol Buffers 3.7.1 (required to build native code)
```bash
$ curl -L -s -S https://github.com/protocolbuffers/protobuf/releases/download/v3.7.1/protobuf-java-3.7.1.tar.gz -o protobuf-3.7.1.tar.gz
$ mkdir protobuf-3.7-src
$ tar xzf protobuf-3.7.1.tar.gz --strip-components 1 -C protobuf-3.7-src && cd protobuf-3.7-src
$ ./configure
$ make -j$(nproc)
$ sudo make install
```

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

### SSH and PDSH <a name="ssh"></a>
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

### Python Libraries <a name="pl"></a>
* pandas
```bash
$ pip install pandas
```
* requests ???
```bash
$ pip install requests
```

## Building Hadoop <a name="build"></a>
To build Hadoop from within the build enviroment run the following command :

```bash
$ mvn package -Pdist,native -DskipTests -Dtar
```
* **-DskipTests** flag : Makes a build without running the unit tests. 
* **-Pdist** and **-Dtar** flags :  Produce a distribution with a .tar.gz file extension.
* **native** flag : Build the native hadoop library.

## Setting up Hadoop Cluster <a name="cluster"></a>
The Hadoop Cluster supports three different modes  <sup>[[12]](References.md#singlenode)</sup> <sup>[[13]](References.md#clustermodes)</sup>:
* **Standalone Mode** : Hadoop is configured as a single java process where none of the deamons run.
* **Pseudo-Distributed Mode** : It is used on a single node and each deamon runs as a separate process on separate JVM.
* **Fully-Distributed Mode** : Hadoop runs on multiple nodes.