# CS 5010 Group Project
---
- David Ackerman (dja2dg)
- Jeremey Donovan (jdd5dw)
- Xin Huang (xh2jg)

## Introduction
We set out to understand how apartments are priced in the United States. 
This has both applications for both tenants and landlords. 
Tenants would benefit from unbiased pricing information when signing or renewing lease agreements.
Landlords, especially those with limited property holdings, could ensure they are charging suitable rent. 
Moreover, landlords could determine which amenities would have the highest return-on-investment.

Beyond pricing, we also sought to understand how amenities vary in the ‘average’ apartment across cities. This is designed to help people moving to new cities decide where they are most likely to get the housing they desire.

## The Data
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
