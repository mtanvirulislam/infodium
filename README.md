[![Architecture](media/logo.png)](https://github.com/mtanvirulislam/infodium)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-ready-brightgreen.svg?style=flat-square&logo=docker) ![Apache Flink](https://img.shields.io/badge/Flink-latest-e6526f?style=flat-square&logo=Apache-Flink) ![Apache Spark](https://img.shields.io/badge/Spark-3.1.2-e35a16?style=flat-square&logo=Apache-Spark) ![Apache Kafka](https://img.shields.io/badge/Kafka-5.4.1-000000?style=flat-square&logo=Apache-Kafka) ![Elasticsearch](https://img.shields.io/badge/Elasticsearch-7.12.1-f3d337?style=flat-square&logo=Elasticsearch) ![Kibana](https://img.shields.io/badge/Kibana-7.12.1-3bbfb1?style=flat-square&logo=Kibana) ![AWS S3](https://img.shields.io/badge/Localstack_S3-latest-8c3123?style=flat-square&logo=Amazon-s3) ![MySql](https://img.shields.io/badge/MySql-latest-00758f?style=flat-square&logo=mysql)

## Overview
Infodium (info + podium) is a lambda architecture demo for data processing and analysis.

The objective of this project is to demonstrate an analytical platform model that is capable of processing data in real time and batch and visualizing the result using different types of technologies..


## Architecture
![Architecture](media/platform.jpg)

## Components

- ### Data Generator:
    It is a process developed in Python that reads a soccer game event dataset and sends the events to Kafka every 0.5 seconds. In addition, it reads some datasets (data of the matches, types of events, etc.), and saves it in MySql.

- ### MySql:
    MySql stores the data received from the Data Generator to consume it later in the Spark and Flink process.

- ### Apache Kafka:
    It receives the events in a topic to consume from the Flink process and stores them in S3 using Kafka connect.


- ### AWS S3 (localstack):
    S3 stores the data received from Kafka connect in a bucket to consume it later in batch processes (Spark).

- ### Apache Flink:
    The Flink process consumes Kafka topic and MySql tables (queries every 30 min) to analyze events in real time and inserts into Elasticsearch indexes.

- ### Apache Spark (Pending to implement):
    Spark reads data stored in S3 and MySql to analyze in batch mode and stores in Elasticsearch indexes.

- ### Elasticsearch:
    Elasticsearch stores the data analyzed in real time and batch mode.

- ### Kibana:
    Visualizes Elasticsearch data in a Dashboard.

## Run demo

### Requirements:
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [docker](https://docs.docker.com/get-docker/)
* [docker-compose](https://docs.docker.com/compose/install/)

Clone repository
```
git clone https://github.com/mtanvirulislam/infodium.git
```

Move to project directory
```
cd infodium
```

Set execute permission to start and stop script
```
chmod +x start

chmod +x stop
```

Start infodium
```
./start

#or
bash start
```

Stop infodium
```
./stop

#or
bash stop
```

## Credits for docker images:
- [The Apache Software Foundation](https://github.com/apache)
- [Confluent Inc.](https://github.com/confluentinc)
- [LocalStack](https://github.com/localstack)
- [Bitnami](https://github.com/Bitnami)
- [Elastic](https://github.com/elastic)
