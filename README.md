# ece-4150-spark-project

**Note:** The template is the same file from Lab 5
The following is a how to run python code _spark-stocks.py_ on an EMR cluster and get the resulting matplot lib graph as a file. 

**Step 1**

Create the stack template on AWS using the yaml file. 

**Step 2: SSH Into the Master Node**

In AWS on the details of the EMR cluster, you should see a button titled **Connect to the Primary node using SSH**. Click on this button. On a local terminal run the command. It should look like the following 
```
ssh -i <path_to_pem_file> hadoop@<ec2-host-name>.compute-1.amazonaws.com
```
You should now be connected into the master node in the EMR. 

**Step 3: Code code to EMR**

Next you will be copying code onto the EMR. Run the following command where the _code_ directory is located in your local machine. 
```
scp -i <path_to_pem_file> -r code hadoop@<ec2-host-name>.compute-1.amazonaws.com:/home/hadoop/
```
The code directory, and data directory containing the AAPL.csv file should now be copied to the EMR. 

**Step 4: Install Libraries in EMR**

In the EMR cluster, navigate to the code directory. Run the following command to install the needed libraries to run the python code. 
```
pip install -r requirements.txt
```

**Step 5: Run the python code**

Run the code using the following command:
```
python spark-stocks.py
```

**Step 6: Moving File To Local Machine**
You will now see a file AAPL_Close_Plot.png. To get this file to your local machine to look at. Run the following command to bring the file to your local machine. Run the following command in a local terminal. Not on the EMR terminal. 

```
scp -i <path_to_pem_file> hadoop@<ec2-host-name>.compute-1.amazonaws.com:/home/hadoop/code/AAPL_Close_Plot.png . 
```
Congrats! You should now have the file on your local machine.



