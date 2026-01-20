## Project Overview
This project demonstrates a simple end-to-end **data engineering pipeline** that crawls company websites, stores raw HTML data, extracts structured content, transforms it into a standardized data model, and computes basic analytics.

The pipeline is designed with a focus on **clarity, modularity, and scalability**, aligning with real-world data engineering practices rather than scraping complexity.

---

## Pipeline Architecture
The pipeline follows a clear, step-by-step workflow:



Each step is isolated to ensure reliability, maintainability, and easy extensibility.

---

## Design Decisions

- **Folder-based storage** is used to simulate an S3-like data lake structure:
  - `raw/` → original HTML data
  - `processed/` → extracted and transformed data
  - `aggregated/` → analytics-ready metrics

- **Modular pipeline stages**:
  - Each stage of the pipeline is implemented as a separate Python module to maintain clear separation of concerns.

- **Standardized data model**:
  - Extracted content is normalized into a section-based schema (e.g., navbar, homepage, footer, case study).

- **Separation of analytics**:
  - Aggregated metrics are stored independently from raw and processed data to support downstream analytics use cases.

---

## Orchestration

An **Apache Airflow DAG** is included to demonstrate:
- Task orchestration
- Clear task boundaries
- Retry logic
- Pipeline extensibility

Due to local Windows environment constraints, the DAG was not executed locally. However, each pipeline stage was validated independently, and the DAG accurately represents how the pipeline would be orchestrated in a production environment.

---

## Scaling Considerations

The pipeline is designed to scale with minimal changes:

- Easily extendable to **N websites**
- Crawling can be adapted to **asynchronous execution**
- Local file-based storage can be replaced with **S3 / GCS**
- Processing can scale using **Apache Spark** or other distributed data processing frameworks


