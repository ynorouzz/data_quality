# Data Quality
This script provides some statistics that can be used for data quality checks such as number of unique values, data range, and number of missed values.

## Dataset
Input data is provided as a csv file. We used a Kaggle dataset that is available [here](https://www.kaggle.com/datasets/iamsouravbanerjee/house-rent-prediction-dataset?resource=download).  The dataset provideds information on Houses/Apartments/Flats Available for Rent with different parameters.
The dataset includes the following fields:

* BHK: Number of Bedrooms, Hall, Kitchen.
* Rent: Rent of the Houses/Apartments/Flats.
* Size: Size of the Houses/Apartments/Flats in Square Feet.
* Floor: Houses/Apartments/Flats situated in which Floor and Total Number of Floors (Example: Ground out of 2, 3 out of 5, etc.)
* Area Type: Size of the Houses/Apartments/Flats calculated on either Super Area or Carpet Area or Build Area.
* Area Locality: Locality of the Houses/Apartments/Flats.
* City: City where the Houses/Apartments/Flats are Located.
* Furnishing Status: Furnishing Status of the Houses/Apartments/Flats, either it is Furnished or Semi-Furnished or Unfurnished.
* Tenant Preferred: Type of Tenant Preferred by the Owner or Agent.
* Bathroom: Number of Bathrooms.
* Point of Contact: Whom should you contact for more information regarding the Houses/Apartments/Flats.

## Script

The script uses *df_quality()* to provide the following information for each field:
* *null_count()*: number of missed values
* *dtypes()*: data types
* *uniqueness()*: number of distinct values
* *df_describe()*: field dattistics such as min, max, mean, std
