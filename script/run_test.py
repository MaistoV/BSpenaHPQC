import pandas
import xml.etree.ElementTree as ET
import os
import requests
import subprocess
import time

# Function to configure di parameters, it receives :
    # 1. the xml file root (configuration)
    # 2. the name of the parameter
    # 3. the value of the paramter
def update_tags(root,n,v):
    if v != '*':                                                    # Check for missing values
        property = ET.Element('property')                           # Create property,name and value elements
        name = ET.Element('name')
        value = ET.Element('value')
        name.text = n                                               # Set the new tags
        value.text = str(v)
        root.append(property)                                       # Add the new elements to the root element
        property.append(name)
        property.append(value)


# Function to Cofigure the xml file site, it receives :
    #1. the xml fila path
    #2. the dataframe row
    #3. the tuple with the configuration parameters
def update_xml(file,row,tuple):    
    tree = ET.parse(file)                                           # Parse the XML file
    root = tree.getroot()  

    for property in root.findall('property'):                       # Remove the previous tags
        name = property.find('name').text                           # Find the tags with the parameters configured for the pseudo-distributed mode 
        if name != 'mapreduce.framework.name' and name != 'mapreduce.application.classpath' and name != 'yarn.nodemanager.aux-services' and name != 'yarn.nodemanager.env-whitelist':
            root.remove(property)

    for t in tuple:
        update_tags(root,t,row[t])                                  # Configure the parameters

    tree.write(file, encoding="utf-8", xml_declaration=True)        # Write on xml file


# Function for the cluster configuration, it takes:
    #1. the path to the hdfs-site.xml
    #2. the tuple with hdfs parameters
    #3. the path to the mapred-site.xml
    #4. the tuple with mapred parameters
    #5. the path to the yarn-site.xml
    #6. the tuple with yarn parameters
    #7. the dataframe row
def config_cluster(path_to_hdfs_site,hdfs_p,path_to_mapred_site,mapred_p,path_to_yarn_site,yarn_p,row):
    update_xml(path_to_hdfs_site,row,hdfs_p)
    update_xml(path_to_mapred_site,row,mapred_p)
    update_xml(path_to_yarn_site,row,yarn_p)


# Function to start the cluster cluster
def start_cluster():
    os.system('$HADOOP_HOME/sbin/stop-dfs.sh')                      # Stop HDFS deamons,YARN deamons and JobHistoryServer
    os.system('$HADOOP_HOME/sbin/stop-yarn.sh')
    os.system('$HADOOP_HOME/sbin/mr-jobhistory-daemon.sh --config $HADOOP_HOME/etc/hadoop stop historyserver')
    time.sleep(2)
    os.system('$HADOOP_HOME/bin/hdfs namenode -format')             # Format the filesystem
    time.sleep(2)
    os.system('$HADOOP_HOME/sbin/start-dfs.sh')                     # Start hdfs and yarn deamons 
    os.system('$HADOOP_HOME/sbin/start-yarn.sh')
    os.system('$HADOOP_HOME/sbin/mr-jobhistory-daemon.sh --config $HADOOP_HOME/etc/hadoop start historyserver')
    os.system('$HADOOP_HOME/bin/hdfs dfs -mkdir /user')             # Make the HDFS directories required to execute MapReduce jobs
    os.system('$HADOOP_HOME/bin/hdfs dfs -mkdir /user/$(whoami)')


# Function to create (using the paramters from test_list.csv) and start the dfsio test, it takes:
    #1. the dataframe row
    #2. the tuple with dfsio parameters
def start_dfsio(row,dfsio_t):
    s = '$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -' + str(row['operation'])
    for t in dfsio_t:
        if row[t] != '*' :                                          # Check for missing values
            s = s + ' -' + t + ' ' + str(row[t])  

    os.system(s)

    # Start online test like linuxperf (not implemented yet)



if __name__=='__main__':

    # xml and csv files path
    path_to_hdfs_site = '/home/spena/hadoop/hadoop-dist/target/hadoop-3.3.5/etc/hadoop/hdfs-site.xml'
    path_to_mapred_site = '$HADOOP_HOME/etc/hadoop/mapred-site.xml'
    path_to_yarn_site = '$HADOOP_HOME/etc/hadoop/yarn-site.xml'
    path_to_test_list = '/home/spena/Desktop/test_list.csv'
    #path_to_test_result = 

    # Tuples with the parameters (same order as of test_list file)
    hdfs_p = ('dfs.namenode.handler.count','dfs.datanode.handler.count')
    mapred_p = ('mapreduce.job.reduces','mapreduce.reduce.cpu.vcores')
    yarn_p = ('yarn.scheduler.minimum-allocation-vcores','yarn.scheduler.maximum-allocation-vcores','yarn.resourcemanager.scheduler.class')
    dfsio_t = ('nrFiles','fileSize','resFile','bufferSize')


    #1. Read test_list.csv file and saves the parameters in a dataframe
    print("Step 1 : Read test_list.csv \n")
    dataframe = pandas.read_csv(path_to_test_list)                  
    dataframe.index = ['test1']


    for i,row in dataframe.iterrows():
        
        #2. Cluster configuration by setting **-site.xml* files
        print("Step 2 : Cluster Configuration \n")
        config_cluster(path_to_hdfs_site,hdfs_p,path_to_mapred_site,mapred_p,path_to_yarn_site,yarn_p,row)
        
        #3. Start the cluster in Pseudo-Distributed Mode
        print("Step 3 : Start the cluster in pseudo-distributed mode")
        start_cluster()
        print("\n")

        #4. Start the DFSIO test
        print("Step 4 : Start the TestDFSIO")
        start_dfsio(row,dfsio_t)
                                
        #5. Start the measurement scripts (offline test) (output secode colonne) and saves the results in *test_result.csv* file
        #response = requests.get('http://localhost:19888/ws/v1/history/mapreduce/jobs')
        #data = response.text
        #print(data)
        #subprocess.run('$HADOOP_HOME/sbin/stop-dfs.sh',shell = True ,capture_output=True)
        print("\n")

        #6 Clean up test results 
        print("Step 6 :Clean up test results")
        os.system('$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -clean')