# Map-Reduce-Assignment

**Introduction**
You were introduced to the MapReduce Optional Assignment, where you practised writing MapReduce codes using a relatively small data set. In this assignment, you will use the NYC TLC yellow taxi data set for the year 2017 and perform various operations using the big data tools that you have learnt about so far.

This session contains the following segments -

Introduction
Dataset Description
Tasks
Evaluation Rubric
Final Submission
In addition, optional sessions are also included, in which you will be reintroduced to some of the concepts covered in the course. You will learn all about MRJob, a popular library created by Yelp for simplifying the process of writing MapReduce code. You will use Apache Sqoop and Apache HBase. You will learn how to work with AWS RDS (Relational Database Service).
 

The data set for the assignment can be downloaded from these links:

https://nyc-tlc-upgrad.s3.amazonaws.com/yellow_tripdata_2017-01.csv
https://nyc-tlc-upgrad.s3.amazonaws.com/yellow_tripdata_2017-02.csv
https://nyc-tlc-upgrad.s3.amazonaws.com/yellow_tripdata_2017-03.csv
https://nyc-tlc-upgrad.s3.amazonaws.com/yellow_tripdata_2017-04.csv
https://nyc-tlc-upgrad.s3.amazonaws.com/yellow_tripdata_2017-05.csv
https://nyc-tlc-upgrad.s3.amazonaws.com/yellow_tripdata_2017-06.csv
 

NOTE: The size of each individual csv file is huge. Since processing all the files is cumbersome, we recommend using just one csv file for testing your MapReduce queries and debugging your code. You can then use the final code with all the datasets above to find the analytical queries.

Tasks
You will use the following big data tools for working with the assignment - Hadoop Framework, Apache HBase and Apache Sqoop. You'll be required to use an AWS EMR instance with all the services and install additional services depending on the tasks.

 

You will need to complete the following tasks after downloading the files onto your EMR Cluster. We recommend that you use the m4.xlarge cluster with ample storage size, since you will be working with a huge data set.

NOTE: It's not required that you work with a multi-node EMR cluster for this assignment. Launching a multi-node cluster will lead to more credit consumption.

 

Once the dataset has been downloaded onto your instance, perform the following tasks:

 

**Tasks:**
**Data Ingestion Tasks:**

Task 1. Create an RDS instance in your AWS account and upload the data to the RDS instance.

Since the dataset is huge, you need to upload the data from only two files (i.e. yellow_tripdata_2017-01.csv & yellow_tripdata_2017-02.csv) from the dataset.

IMPORTANT NOTE: You will need to create an appropriate schema before uploading the data sets to AWS RDS (you can find the data dictionary in the previous segments). The steps on how to create an AWS RDS instance can be found in the Additional content of the 'Introduction to Cloud Computing and AWS Setup' module and the steps to work with RDS in the link shared in the next segment)

 

Task 2. Use Sqoop command to ingest the data from RDS into the HBase Table.

 

Task 3. Bulk import data from next two files in the dataset on your EMR cluster to your HBase Table using the relevant codes.

Note: For the above task 3, you just need to import data from the subsequent 2 csv files (i.e. yellow_tripdata_2017-03.csv & yellow_tripdata_2017-04.csv) on your EMR cluster.

 

**MapReduce Tasks:**

Task 4. Write MapReduce codes to perform the tasks using the files you’ve downloaded on your EMR Instance:

Which vendors have the most trips, and what is the total revenue generated by that vendor?
 
Which pickup location generates the most revenue? 
 
What are the different payment types used by customers and their count? The final results should be in a sorted format.
 
What is the average trip time for different pickup locations?
 
Calculate the average tips to revenue ratio of the drivers for different pickup locations in sorted format.
 
How does revenue vary over time? Calculate the average trip revenue per month - analysing it by hour of the day (day vs night) and the day of the week (weekday vs weekend).
 
NOTE: It's recommended to use MRJob for completing the MapReduce tasks above.

**Optional Task:**

Task 5. Use Sqoop export command to export the results of each MapReduce tasks above to your RDS instance. Use the RDS connection string connection to visualise the dataset using a dashboarding tool (Google Data Studio, Tableau or PowerBI) (Optional)

NOTE: Please note that Task 5 is optional and purely to demonstrate how RDS and Sqoop.

NOTE: The Data Ingestion tasks and the MapReduce tasks are separate. The MapReduce tasks must be run with the local data downloaded to the cluster.


