# SQL Optimisation Project
A personal project to see the improvements certain optimisation techniques can have on a large, mock company database.

## 📖 Contents:
- [Standard SQL](docs/01_baseline_sql.md)
- [Indexing](docs/02_indexing.md)
- [Optimising Queries](docs/03_query_optimisation.md)
- [Advanced Aggregations](docs/04_advanced_aggregations.md)
- [Materialised Views](docs/05_materialised_views.md)
- [Stored Procedures](docs/06_stored_procedures.md)
- [Partitioning & Transactions](docs/07_partitioning_and_transactions.md)
- [Concurrency & Transactions](docs/08_concurrency_and_transactions.md)
- [Temporal & Time-Series SQL](docs/09_temporal_timeseries.md)
- [Triggers](docs/10_triggers.md)
- [Fragmentation & Maintenance](docs/11_fragmentation_and_maintenance.md)
- [Caching & Buffer](docs/12_caching_and_buffer.md)
- [Data Compression](docs/13_data_compression.md)
- [Parallel Query Execution](docs/14_parallel_query_execution.md)
- [Data Modelling Optimisations](docs/15_data_modelling_optimisations.md)

## ℹ️ Overview:
The purpose of this project is to explore how various optimisation techniques in SQL can be used to speed up the querying of an SQL database in a realistic setting.
In this project, I have made an **employee** database, which you can find the documentation for below. It is designed to replicate a production-scale system. Key attributes of this project include:
- Intentionally Oversized Design:
  * More tables are created than what might be required to experiment better with optimisations.
  * Allows for more extensive testing of these strategies.
- Random entries are generated:
  * This is to simulate the size of a real production-level database and real-world workload.
- Database is normalised:
  * Whilst this is an experiment, I still want to ensure the database still follows database design principles.
  * It follows standard normalisation principles to ensure data integrity and design clarity.
- Well designed:
  * All of the documentation for the design can be found below.
  * It is still designed with proper checks, foreign keys and appropriate constraints. - no cutting corners here.

I will benchmark and test with the database using just standard SQL queries. No fancy optimisations, just pure SQL to see the baseline performance of the database.

Once there is a baseline benchmark, I will test each of the optimisations individually, seeing how they can improve the performance statistics alone. Then I will run a combined test to see how all of these optimisations combined (where possible) will speed up the performance. Charts can be found below in documentation.

## 💻 Technology:
- **PostgreSQL** - RDBMS
- **DBeaver** - SQL IDE
- **Docker** - Local sandbox environment
- **Python** - For data generation
  * Libraries like ```Faker```, ```psycopg2```, and ```SQLAlchemy``` may be used

## 📂 Documentation:
- Entity Relationship Diagrams (ERD)
- Database Schema
- Performance Benchmark Charts + Logs

## 📄 License:
