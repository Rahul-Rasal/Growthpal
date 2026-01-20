Project Overview
This project demonstrates a simple end-to-end data engineering pipeline that crawls company websites, stores raw HTML data, extracts structured content, transforms it into a standardized data model, and computes basic analytics. The pipeline is designed with clarity, modularity, and scalability in mind.

Design Decisions

Folder-based storage simulates an S3-like raw/processed/aggregated data lake

Each pipeline stage is isolated into its own module

The data model follows a normalized, section-based structure

Aggregations are stored separately to support analytics use cases

Orchestration
An Apache Airflow DAG is included to demonstrate pipeline orchestration, task boundaries, retries, and extensibility. Due to Windows environment constraints, the DAG was not executed locally, but all pipeline steps were validated independently.

Scaling Considerations

Easily extendable to N websites

Can be adapted to async crawling

Raw storage can be replaced with S3/GCS

Processing can scale using Spark or distributed execution