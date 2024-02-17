import pandas
import xml.etree.ElementTree as ET
import os
import subprocess

# xml and csv files path
path_to_hdfs_site = '/home/spena/Desktop/hdfs-site.xml'
path_to_mapred_site = '$HADOOP_HOME/etc/hadoop/mapred-site.xml'
path_to_yarn_site = '$HADOOP_HOME/etc/hadoop/yarn-site.xml'
path_to_test_list = '/home/spena/Desktop/test_list.csv'
#path_to_test_result = 

# Tuples with the parameters (same order as of test_list file)
hdfs_p = ('dfs.namenode.handler.count','dfs.datanode.handler.count')
mapred_p = ('mapreduce.job.reduces','mapreduce.reduce.cpu.vcores')
yarn_p = ('yarn.scheduler.minimum-allocation-vcores','yarn.scheduler.maximum-allocation-vcores','yarn.resourcemanager.scheduler.class')


# Function to configure di parameters, it receives :
# 1. the xml file root (configuration)
# 2. the name of the parameter
# 3. the value of the paramter
def update_tags(root,n,v):
    property = ET.Element('property')                               # Create property,name and value elements
    name = ET.Element('name')
    value = ET.Element('value')
    
    name.text = n                                                   # Set the new tags
    value.text = str(v)
    
    root.append(property)                                           # Add the new elements to the root element
    property.append(name)
    property.append(value)


# Function to Cofigure the xml file site, it receives :
# 1. the xml fila path
# 2. the dataframe row
# 3. the tuple with the configuration parameters
def update_xml(file,row,tuple):    
    tree = ET.parse(file)                                           # Parse the XML file
    root = tree.getroot()  

    for property in root.findall('property'):                       # Remove the previous tags
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
    #update_xml(path_to_mapred_site,row,mapred_p)
    #update_xml(path_to_yarn_site,row,yarn_p)


if __name__=='__main__':
    
    #1 Read test_list.csv file and saves the parameters in a dataframe
    print("Step 1 : Read test_list.csv \n")
    dataframe = pandas.read_csv(path_to_test_list)                  
    dataframe.index = ['test1','test2']

    # For each dataframe row are executed the the steps from 2 to 6
    for i,row in dataframe.iterrows():
        
        #2. Cluster configuration by setting **-site.xml* files
        print("Step 2 : Cluster Configuration \n")
        config_cluster(path_to_hdfs_site,hdfs_p,path_to_mapred_site,mapred_p,path_to_yarn_site,yarn_p,row)
        
        #3 Start the cluster in pseudo-distributed mode
            # Stop hdfs and yarn deamons (va fatto per ogni test)
            # Format the filesystem (da commentare)
            # Start hdfs and yarn deamons (va fatto per ogni test)
            # Make the HDFS directories required to execute MapReduce jobs (va fatto per ogni test)
        os.system('$HADOOP_HOME/sbin/start-dfs.sh')
        #os.system('$HADOOP_HOME/sbin/stop-dfs.sh')
        #subprocess.run('$HADOOP_HOME/sbin/stop-dfs.sh',shell = True ,capture_output=True)

        #4 Start the DFSIO test (in background) -- > prima fork
            # Start online test linuxperf (output elaborato prime colonne)
                    
        #5 Start the measurement scripts (offline test) (output secode colonne) and saves the results in *test_result.csv* file

        #6 Clean up test results 
