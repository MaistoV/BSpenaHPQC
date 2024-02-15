import pandas
from lxml import etree as ET


if __name__=='__main__':

#1 Read test_list.csv file and saves the parameters in a dataframe
    dataframe = pandas.read_csv('test_list.csv',names = ['dfs.namenode.handler.count','dfs.datanode.handler.count','mapreduce.job.reduces'])
    dataframe.index = ['test1','test2']

# For each dataframe row are executed the other steps
    i = 1
    while i < 3 :
        test_num = 'test' + str(i)
        
#2 Configures the Hadoop clusters by setting **-site.xml* files
    tree = ET.parse('hdfs-site.xml')                                    # Parse the XML file
    root = tree.getroot()                                               # Get the root element

    # Effettuare la rimozione delle property già presenti

    # Aggingere controllo se il valore è un valore corretto


    property = ET.Element('property')                                     # Create property,name and value elements
    name = ET.Element('name')
    value = ET.Element('value')

    name.text = 'dfs.namenode.handler.count'                                          # Set the new tags
    value.text = str(dataframe.at[test_num,'dfs.namenode.handler.count'])

    root.append(property)                                               # Add the new elements to the root element
    property.append(name)
    property.append(value)

    tree.write('hdfs-site.xml', encoding="utf-8", xml_declaration=True,pretty_print=True)       # Write on xml file

#3 Start the cluster in pseudo-distributed mode
    # Stop hdfs and yarn deamons (va fatto per ogni test)
    # Format the filesystem (da commentare)
    # Start hdfs and yarn deamons (va fatto per ogni test)
    # Make the HDFS directories required to execute MapReduce jobs (va fatto per ogni test)

#4 Start the DFSIO test (in background) -- > prima fork
    # Start online test linuxperf (output elaborato prime colonne)
                
#5 Start the measurement scripts (offline test) (output secode colonne) and saves the results in *test_result.csv* file

#6 Clean up test results 
        
    i = i + 1                                                           # Increment