# Hadoop-MapReduce-Purchase-Problem
Solve a Purchase Problem using Hadoop MapReduce
1. Mapper: 
- Purse the data file from HDFS with wrong format checking
- Generate the intermediate key-value pairs where the key is the store location and the value is the sales amount

2. Reducer:
- The key-value pairs pass to the reducer after shuffle and sort
- Iterate through each key-value record to accumulate the data (sales amount) for each key (store location)
- Generate the final output with each store location and its total sales amount

Notice: the program using Python because I used Hadoop Streaming to run the map/reduce jobs.
