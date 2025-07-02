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

## ⚠️ Prerequisites
Forcing PostgreSQL to Simulate Disk I/O

**Observation:**

Running:
```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM employee WHERE salary > 100000 AND sex = 'm';
```

Outputted:
```
Buffers: shared hit=2467
```

**Interpretation**:
All data was served from PostgreSQL’s shared buffer (RAM). No disk reads occurred.

**Result**:
Query executed very fast (~25 ms), which is unrealistic for large datasets on spinning disks.
* **Average latency**: 25.368 ms
* **Latency stddev**: ±3.292 ms

**Goal:**
Force PostgreSQL to perform more disk I/O to simulate real-world latency on disk-based systems.

**Changes Made:**
Update `postgresql.conf` to reduce memory use and discourage caching:
```conf
shared_buffers = 128MB -> 32MB           # Reduce PostgreSQL shared cache
effective_cache_size = 4GB -> 256MB      # Lower OS cache estimation for planner
work_mem = 4MB -> 1MB                    # Limit memory for sorts/hashes to force spills
maintenance_work_mem = 64MB -> 16MB      # Reduce memory for maintenance operations
```
Optional: Flush OS disk cache before running tests

*Whilst these are aimed at trying to simulate real-world latency, my PC is setup to minimise this so these changes won't change much. However, benchmarks will be relative to the baseline, so improvements will be shown as a percentage.

Apply config changes:
```bash
sudo systemctl restart postgresql
```

Re-run the Query:
```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM employee WHERE salary > 100000 AND sex = 'm';
```

Check for:
```
Buffers: shared hit=XX, read=YY
```

* **Goal**: `read=YY` > 0
  → Confirms actual disk reads (slower, more realistic latency)

## 💻 Technology:
- **PostgreSQL** - RDBMS
- **DBeaver** - SQL IDE
- **Docker** - Local sandbox environment
- **Python** - For data generation
  * ```Faker``` has been used to help generate realistic data entries

## 📂 Documentation:
- Entity Relationship Diagrams (ERD)
- Database Schema
- Performance Benchmark Charts + Logs

## 📄 License:
