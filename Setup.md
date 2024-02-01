# Environment Setup
## Overview
Virtual machine running **Ubuntu 22.04 LTS** :
  * 8 GB of RAM 
  * 4 cores
  * 150 GB of memory

## Tools
* **Java 1.8**
```bash
$ sudo apt install openjdk-8-jdk

# Setting the JAVA_HOME environment variable 
$ sudo nano /etc/environment                    # Open the /etc/environment
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"   # Add this line to the end of the file
$ source /etc/environment                       # To take effect the changes
$ sudo reboot                                   # Restart the system
$ echo $JAVA_HOME                               # To verify is the variable is set correctly
```
* **Maven 3.6**
```bash
sudo apt-get -y install maven
```
* **Hadoop 3.3.5**
```bash
$ git clone https://github.com/apache/hadoop.git --branch rel/release-3.3.5 --single-branch
```
* Other Libraries



sudo apt-get -y install openjdk-8-jdk
sudo apt-get -y install maven
sudo apt-get -y install build-essential autoconf automake libtool cmake zlib1g-dev pkg-config libssl-dev libsasl2-dev
curl -L -s -S https://github.com/protocolbuffers/protobuf/releases/download/v3.7.1/protobuf-java-3.7.1.tar.gz -o protobuf-3.7.1.tar.gz
mkdir protobuf-3.7-src
tar xzf protobuf-3.7.1.tar.gz --strip-components 1 -C protobuf-3.7-src && cd protobuf-3.7-src
./configure
make -j$(nproc)
sudo make install
# Optionals for native libraries
sudo apt-get install snappy libsnappy-dev
sudo apt-get install bzip2 libbz2-dev
sudo apt-get install fuse libfuse-dev
sudo apt-get install libzstd1-dev

mvn package -Pdist -Dtar -DskipTests
mvn compile -Pdist -Dtar -DskipTests