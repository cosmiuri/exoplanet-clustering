# Exoplanet Clustering Project

This project builds an end-to-end data pipeline and performs clustering analysis on exoplanet data from the NASA Exoplanet Archive.

## Overview

The goal is to explore whether exoplanets form natural groups based on their physical properties such as mass, radius, orbital period, and host star characteristics.

The project includes data ingestion, storage, cleaning, feature engineering, and clustering.

## Pipeline

1. Data ingestion from NASA Exoplanet Archive using API queries  
2. Storage of raw data in PostgreSQL  
3. Cleaning and transformation using SQL  
4. Feature engineering in Python  
5. Clustering using KMeans and DBSCAN  
6. Visualization using PCA  

## Data

The dataset contains exoplanet and host star parameters including:
- Planet mass (Earth masses)
- Planet radius (Earth radii)
- Orbital period (days)
- Star effective temperature (Kelvin)
- Star mass (solar masses)

## Feature Engineering

Additional features were created to better represent physical relationships:

- Density (mass / radius³)
- Log-transformed mass, radius, and orbital period
- Scaled temperature (relative to Sun)

## Methods

Two clustering approaches were used:

- KMeans, which assumes spherical clusters and requires a predefined number of clusters  
- DBSCAN, which identifies dense regions and labels outliers as noise  

## Results

The analysis shows that exoplanets do not form clearly separated clusters. Instead, the data exhibits a continuous distribution with a dominant population and several smaller dense regions.

DBSCAN was more effective than KMeans in identifying outliers and local structures.

## Tech Stack

- Python (pandas, numpy, scikit-learn)
- PostgreSQL
- SQLAlchemy
- Matplotlib


