# Rational in using Firebase for NutriHelp.  

Contributed by Chin Tho (John) Leong T3 2023

## **Types of databases considered:**  

Relational database 
- Stores information in tables where relationships can be established to link multiple tables together.
- Uses columns to define the information being stored and rows for actual record keeping.
- The commonest way to interact with a relational database is with Structured Query Language (SQL).

Non-Relational database
- Is a database that is the opposite of a relational database such that it does not use tables, fields, and columns to store data. It stores data by document format commonly JSON-like, by key and value, by nodes in graph databases or by wide columns like relational databases.
- This type of database is designed with cloud networking in mind.

## **Advantages and Disadvantages**  

![Table RD vs NRD.png](https://github.com/Gopher-Industries/Nutrihelp/blob/d7dbe9a57b547b25dedbd284ba0fb6cd176edcb6/database/Docs/Table%20RD%20vs%20NRD.png)  
Table taken from: <https://www.mongodb.com/compare/relational-vs-non-relational-databases>

As NutriHelp is designed as a 2-component product (android app and web app) requiring high flexibility and performance, the best database type to use is non-relational databases.

## **What non-relational databases are available on the market:**  

|**Features**|**MongoDB**|**\*Firebase**|
| :-: | :-: | :-: |
|**Common Features**|<p>- Fully Managed/automated database service</p><p>- Global Clusters</p><p>- Monitoring and Alerts</p><p>- Serverless Triggers</p>|<p>- Fully Managed/automated database service</p><p>- Global Clusters</p><p>- Monitoring and Alerts</p><p>- Serverless Triggers</p>|
|**Backups**|Automated backups with incremental data recovery and consistent, cluster-wise snapshots.|Scheduled export manually with no failure recovery.|
|**Security**|Uses own port through SSL/TLS|Use HTTPS request API|
|**Realtime Updates**|None|Available|
|**Offline Support**|Good for local development as it can be deployed locally|Out of the box in Firestore but can’t be disconnected from the cloud entirely.|

*\*Best choice to use for NutriHelp*

## **In Firebase, there are 2 types of document databases available:**  

||**Cloud Firestore**|**Realtime Database**|
| :-: | :-: | :-: |
|**Role of database**|Primarily Synchronising data with basic querying|Advanced querying, sorting and transactions.|
|**Operations on data**|A few GBs|Hundreds of GBs to TBs|
|**Data model**|A simple JSON Tree|Documents organise into collections|
|**Availability**|Guarantee at 99.999% uptime|At least 99.95% uptime|
|**Offline queries on local data**|Frequently|Rarely or never|
|**Use case for NutriHelp**|Early development|Mid to late development|

