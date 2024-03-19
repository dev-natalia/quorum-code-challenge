1. Discuss your strategy and decisions implementing the application. Please, considertime complexity, effort cost, technologies used and any other variable that you understand important on your development process. 
My hardest time was using and integrating django with html, cause its not something that I have worked with. I used some videos and a little help of chatgpt in some of the configs of the htmls. Tha backend part was easy to do, although I'm more used to use FastAPI in the last three years. I would change a lot of the structure, creating a SQL database to insert the csv data in it. In that case, it would change a lot of the code, using SQLAlchemy to manipulate and access the data. It would prevent the code repetition that happened, cause I needed to access the csv data all times. I though about having the csv data in cache, but it would need some way of cleaning the cache from time to time, like a cronjob. Also, I'm more familiar with the front and backend split, and thats why I had the problemas with the integration. It's something that I can do, but would have a leanirng curve.


2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”? 
As I will explain below, I would start not using csv as a database. I would add the data to a SQL database. So, for future columns it would be used like that. If its common to add more columns, or tables, than a NoSQL db like Mongo would be better, cause it is not structured as SQL. But, a NoSQL its not the best approach cause its not mean to be a db to make lots requests to get data, or change it often.


3. How would you change your solution if instead ofreceiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for? 
First, I wouldn't use the csv. Receiving a csv, I would prefer to work with the data to a structured sql database. This will prevent the loops that I had to use to access the csv data every time I had to use it. So, with or without csv, I would use an ETL tool to work with the data, adding it to a SQL database (like Postgres) and change my aproach on the code using SQLAlchemy to connect to the database, using the ORM to access the data. I dont know exactly which tool, I know about Glue on AWS tha does that, but also know that there are others tools for this purpose.


4. How long did you spend working on the assignment? 
Around 4.5 hours