# CS 5010 Group Project
---
- David Ackerman (dja2dg)
- Jeremey Donovan (jdd5dw)
- Xin Huang (xh2jg)
---
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

![Figure 1](https://github.com/JudFox/Analyzing-Apartment-Data/blob/main/Report/figures/fig1.jpg)

The attributes we used from the apartments for rent dataset were as follows (with a discussion of how we cleaned the data to address outliers and missing data):

- Amenities
  - 3,549 missing values coded in the dataset as ‘null’; we have retained these records and have assumed ‘none’
- Bathrooms

![Figure 2](https://github.com/JudFox/Analyzing-Apartment-Data/blob/main/Report/figures/fig2.jpg)

   - Ranges from 1 to 8 with a mean of 1.38
   - 34 missing values; here, we set bathrooms=bedrooms (based on regression - not shown - with R 2 = 0.46)
- Bedrooms
  - Ranges from 1 to 9 with a mean of 1.78
  - 205 missing values (of which 7 are blank and 198 coded as “0” which is not possible). We dropped all 205 values.

![Figure 3](https://github.com/JudFox/Analyzing-Apartment-Data/blob/main/Report/figures/fig3.jpg)

- Pets_Allowed
  - Listed as none, cats, or ‘cats,dogs’. There are also 1748 coded as ‘null’ which we retained by assuming ‘none’.

![Figure 4](https://github.com/JudFox/Analyzing-Apartment-Data/blob/main/Report/figures/fig4.jpg)

- Price
  - Ranges from $200 to $52,500 with a mean of $1486; No missing values
  - The $52,500/month apartment, an outlier, was miscoded since the description lists price as $500/month. We dropped this (actually was dropped because it also had bedrooms = 0)

![Figure 5](https://github.com/JudFox/Analyzing-Apartment-Data/blob/main/Report/figures/fig5.jpg)

- Square_feet
  - Ranges from 101 to 40,000 with an average of 946; no missing values

![Figure 6](https://github.com/JudFox/Analyzing-Apartment-Data/blob/main/Report/figures/fig6.jpg)

- Latitude & Longitude
  - 10 missing values; we replaced the missing values with sentinel values for the North Pole
We also eliminated four records that appeared to be rooms for rent (discussed in
Appendix A).

One of the attributes we did not use but still wanted to investigate was the source from which the creator of the data scraped. As shown in the figure below, the vast majority were from RentLingo (69%) and RentDigs.com (28%).

![Figure 7](https://github.com/JudFox/Analyzing-Apartment-Data/blob/main/Report/figures/fig7.jpg)

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
   1. The primary source data contained 22 attributes and 10,000 rows. As discussed above and in the Appendix, we retained the 8 of the attributes we felt would be most useful for analysis. We examined and addressed missing data and outliers.
   2. The secondary source data continued Starbucks locations with latitude and longitude. We obtained this from Data.World.
3. Read the two CSV files into 2 dataframes in Python
4. Append a column to the dataframe with the number of Starbucks within an x (ex: 5) mile radius of each apartment.
5. Query and analyze the data (including Unit Testing of our code) in the
following ways:
   1. Regression analysis with price as the dependent variable
   2. Visualize and descriptive statistics
   3. Prediction models for determining which city a listing is in based on price, bedrooms, bathrooms, and square feet
   4. Prediction models for the number of bedrooms based on price and bathrooms
   5. Determine general relationship between the number of bedrooms and number of bathrooms in apartments
   6. General bar and scatter plots to understand relationship between variables using df display GUI
6. Write up our results with tables & visualizations

## 4 Beyond the Original Specification
Here, we provide a high-level description of the ways we went above and beyond
the original project specification. We outline the techniques here and provide
deeper analysis and insights in the subsequent Results section.

## 5 Results
We began with a number of interesting queries as follows:
1. What is the mean price of an apartment?

![Figure 5-1](https://github.com/JudFox/Analyzing-Apartment-Data/blob/main/Report/figures/fig5-1.jpg)
![Figure 5-2](https://github.com/JudFox/Analyzing-Apartment-Data/blob/main/Report/figures/fig5-2.jpg)

2. What percentage of apartments have wood floors?
3. What is the median number of starbucks nearby?
4. What is the average sq ft by # number of bedrooms?

Next we built a regression model to predict price for the potential regressors,
including many categorical variables for amenities.
We were worried about multicollinearity of quantitative independent variables as
well as association between qualitative independent variables. The correlation
matrix (shown below) reveals a high correlation between bedrooms and
bathrooms. We left both variables in to allow our forward selection model to
choose the better of the two.

Using the Cramer’s V test to explore categorical variable association, we found
(shown below) high association between (Dishwasher, Refrigerator) and between
(cats, dogs). We dropped regressors for Dogs, and Refrigerator.

Next, we built a regression model using forward selection given a radius of 5
miles from each apartment to determine the number of local Starbuck stores.

The resulting coefficients with radius = 5 miles were as follows:

We were particularly interested in whether or not the number of local Starbucks
would be a statistically significant predictor. Indeed, forward selection found it to
be the second strongest factor (behind bathrooms). Each local Starbucks within a
5 mile radius is associated with a $17.07 increase in monthly rent. We do not
necessarily think there is a causal relationship here; instead, our hypothesis is
that Starbucks are cited highly desirable locations. Moreover, there are more
Starbucks locations in areas with higher population density and it is the
population that ‘causes’ the increase in demand.

As noted above, the adj $R^2$ with radius=5 miles is 41.8%. By comparison, we
repeated the forward selection algorithm excluding the starbucksCount variable
and found adj $R^2$ drops to 28.6%. This strengthened our conviction in using the
Starbucks count as a predictor.

## Conclusions
1. Key Findings and Use Cases
   1. Given an adj R 2 = 49.57% (moderately high), we would recommend our model as directionally correct for landlords and tenants to use when signing & renewing leases.
   2. In the presence of other factors (to confirm we would recommend simple linear regression), the following are positively correlated with pricing and are therefore recommended improvements for landlords to make: bathrooms; citing near Starbucks; larger sq. ft; elevator; bedrooms; wood floor; view; dishwasher; internet access. Notably, most of these are ‘interior to the apartment’ improvements.
   3. In the presence of other factors (to confirm we would recommend simple linear regression), the following are negatively correlated with pricing and therefore not recommended: playground; fireplace; AC (investigate further); doorman (investigate further); garbage disposal; basketball; washer/dryer (investigate further); gated (investigate further). Most of these are external and/or generate noise (garbage disposal) or risk (fireplace). We suspect those we labeled as “investigate further” would turn positive in simple linear regression and are thus conflated with other factors in the multiple regression.
2. Future Improvements (if we had more time)
   1. Integrate additional predictors into our regression model Including but not limited to 4 : population density; city ranking; median household income; racial composition; crime rates; etc.
   2. More carefully explore non-linearity and/or interactions between independent variables in our regression model
   3. Test the validity of our pricing model with out-of-sample data
   4. Implement a vectorized version of the geodesic algorithm (more accurate than Haversine)
   5. Explore more sophisticated regression models beyond forward selection to predict price
   6. Implement natural language processing to extract keywords from the “body” attribute (a free form text description of each apartment)
