# Backend/DevOps Engineer @ xbird challenge

Below is how to run my solution, along with the answers to various questions.

# To run:
From the root dir....

## Build:
To build the docker app image:
    
    ./build
    
## Run:
To start the containers:

    ./start
    
## Migrate:
To migrate the database    
  
    ./migrate
    
## Send data:
You might want to create a virtual env.
Make sure that the requirements in the requirements.txt and installed e.g.

    pip install -r app/requirements.txt

To start sending data

    ./send_data
    
## To see the data in the db:
Visit http://localhost:8088/?pgsql=db&username=xbird&db=xbird&ns=public

# Questions:

## Explain your database choice:

I chose a relational sql database. 
While nosql databases can be useful in certain situations, relational databases have been depended on and optimized for decades.
The ability to define a schema, and change that schema over time, means you can reliably maintain data consistency.
The data that is defined in the protobuf format is easy to map into a relational schema.

I chose postgres because it is opensource and has a huge active community. It has great features such as json columns which allow for schemaless data if needed.
(I am also familiar with it!)

## How would you modify the system if the number of samples becomes really big?:

I would batch the samples and process them asynchronously using jobs and workers (e.g. celery) 

## How would you monitor the running services:

I would use logging aggregator such as prometheus or papertrail.
I would also have alerts set up do monitor things such as db cpu usage, etc. 


# Things I would have like to have done:
As I have not used python in a long time, I found this more time consuming than it should have been.
It took me a while to set up database migrations, etc. Most of the tools I had to use were not familiar to me. Thus I did not have the time to do many things I would have liked too e.g.

- Add various database indexes.
- Handle errors.
- Tests! (I usually use extensive testing, but haven't used a python test framework in over 2 years.)
- Kubernetes (Docker compose is a simple easy alternative - but not scalable.)
- Location type samples.
- etc.
