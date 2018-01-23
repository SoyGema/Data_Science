
## Exploration of dataset in PySpark 

##Inspect SparkContext ( important for configuration )
sc.version 
sc.master
sc.appName
sc.applicationId
sc.defaultParallelism
sc.defaultMinPartitions

#Configuration for local (changeable)
conf = (SparkConf()
        .setMaster("local")
        .setAppName("My app")
        .set("spark.executor.memory", "lg")

#Create a SparkContext and a sqlContext 
from pyspark.sql import SparkContext,SQLContext
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

#Use Spark-csv pakage and extract it into the home directory of Spark 
Data = sqlContext.read.format('com.databricks.spark.csv').options(header = True).load("Data.csv")

#Explore the first 5 rows of the dataset 
Data.take(5)  #Also Data.head(5)

#Count rows
Data.count()

#Print data-types 
Asteroid_data.printSchema()


#Drop missing values 
Data.na.drop().count()

#Analyzing numerical features
Data.describe().show()

#Analyzing categorical features 
Data.select('Class').distinct().count()

#Selecting sub-setting columns
Asteroid_data.select('Emoid').show()
