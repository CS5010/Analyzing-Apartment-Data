# CS 5010 Group Project
---
- David Ackerman (dja2dg)
- Jeremey Donovan (jdd5dw)
- Xin Huang (xh2jg)

## 1 Introduction
We set out to understand how apartments are priced in the United States. 
This has both applications for both tenants and landlords. 
Tenants would benefit from unbiased pricing information when signing or renewing lease agreements.
Landlords, especially those with limited property holdings, could ensure they are charging suitable rent. 
Moreover, landlords could determine which amenities would have the highest return-on-investment.

Beyond pricing, we also sought to understand how amenities vary in the ‘average’ apartment across cities. This is designed to help people moving to new cities decide where they are most likely to get the housing they desire.

## 2 The Data
Avoiding the need for web scraping, we were able to locate a recent (2019-12-28) apartment for rent dataset 1 containing 10,000 rows on the UCI Machine Learning Repository. 
Since the creator had not uploaded the data, we reached out to him ( fredrick_nilsson@yahoo.com ) directly and he kindly sent us his datafile. 
This data sets sampled apartment listings across 51 states.

The attributes we used from the apartments for rent dataset were as follows (with a discussion of how we cleaned the data to address outliers and missing data):

- Amenities
  - 3,549 missing values coded in the dataset as ‘null’; we have retained these records and have assumed ‘none’
- Bathrooms
   - Ranges from 1 to 8 with a mean of 1.38
   - 34 missing values; here, we set bathrooms=bedrooms (based on regression - not shown - with R 2 = 0.46)
- Bedrooms
  - Ranges from 1 to 9 with a mean of 1.78
  - 205 missing values (of which 7 are blank and 198 coded as “0” which is not possible). We dropped all 205 values.
- Pets_Allowed
  - Listed as none, cats, or ‘cats,dogs’. There are also 1748 coded as ‘null’ which we retained by assuming ‘none’.
- Price
  - Ranges from $200 to $52,500 with a mean of $1486; No missing values
  - The $52,500/month apartment, an outlier, was miscoded since the description lists price as $500/month. We dropped this (actually was dropped because it also had bedrooms = 0)
- Square_feet
  - Ranges from 101 to 40,000 with an average of 946; no missing values
- Latitude & Longitude
  - 10 missing values; we replaced the missing values with sentinel values for the North Pole
We also eliminated four records that appeared to be rooms for rent (discussed in
Appendix A).

One of the attributes we did not use but still wanted to investigate was the source from which the creator of the data scraped. As shown in the figure below, the vast majority were from RentLingo (69%) and RentDigs.com (28%).

In addition, we supplemented the primary apartment for rent dataset with an additional dataset 2 listing all Starbucks locations in the world in order to explore whether nearby coffee shops might be statistically significant in predicting apartment pricing. 
This data includes latitude and longitude which helped us in determining how many Starbucks lie within an x (ex: 5) mile radius of each apartment.

## 3 Experimental Design
The following is our step-by-step process from obtaining the data to finding
results.
1. Obtain data
We browsed several sources including the UCI Data Repository, Kaggle,
and Data.World to find a dataset that would allow us to apply a range of
data science techniques. As discussed above, we settled on apartment
rent data. Since the data had not been uploaded to the UCI Data
Repository, we obtained it directly from the individual who sourced it (that
individual employed web-scraping.)
2. Examine & clean the data
3. 
