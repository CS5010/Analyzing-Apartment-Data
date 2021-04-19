# ###########################################################################################################
# CS 5010 Semester Project
# Team members:
# David Ackerman (dja2dg)
# Jeremey Donovan (jdd5dw)
# Xin Huang (xh2jg)
# This code encompasses the advanced techniques used on this project and regression results
# ###########################################################################################################


# ###########################################################################################################
# Import libraries & set working directory
# ###########################################################################################################

import pandas as pd
from numpy import sin, cos, pi, arcsin, sqrt
import numpy as np
import sys  # helpful for sys.exit()
import time
from datetime import datetime
#import itertools
#import seaborn as sns
#import statsmodels.api as sm
import matplotlib.pyplot as plt
import scipy.stats as ss
#from sklearn import linear_model
#from sklearn.metrics import mean_squared_error
#from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
#from geopy.distance import geodesic  # not used since does not seem to be vector friendly
#import haversine  # created own version of this
#from mpl_toolkits.mplot3d import Axes3D
from os import chdir, getcwd
#import os # accessing directory structure
import statsmodels.formula.api as smf
from math import floor

# ###########################################################################################################
# Set up helper functions
# ###########################################################################################################
 
def sb_in_range_vec(lat, lon, pcode_lat, pcode_lon,rad_in_miles):
    """
    Find the distance between (lat,lon) and the reference point
    (pcode_lat,pcode_lon).
    Source: https://godatadriven.com/blog/the-performance-impact-of-vectorized-operations/
    """
    RAD_FACTOR = pi / 180.0  # degrees to radians for trig functions
    lat_in_rad = lat * RAD_FACTOR
    lon_in_rad = lon * RAD_FACTOR
    pcode_lat_in_rad = pcode_lat * RAD_FACTOR
    pcode_lon_in_rad = pcode_lon * RAD_FACTOR
    delta_lon = lon_in_rad - pcode_lon_in_rad
    delta_lat = lat_in_rad - pcode_lat_in_rad
    # Next two lines is the Haversine formula
    inverse_angle = (sin(delta_lat / 2) ** 2 + cos(pcode_lat_in_rad) *
                     cos(lat_in_rad) * sin(delta_lon / 2) ** 2)
    haversine_angle = 2 * arcsin(sqrt(inverse_angle))
    #EARTH_RADIUS = 6367  # kilometers
    EARTH_RADIUS = 3958  # miles
    distance=haversine_angle * EARTH_RADIUS
    in_range=(distance<=rad_in_miles)
    return in_range.astype(int)
    

def hasAmenity(amenity_list_vector,amenity):
    in_list=( (np.char.find(amenity_list_vector,amenity)) != -1)
    return in_list.astype(int)


def forward_selected(data, response):
    """Linear model designed by forward selection.

    Parameters:
    -----------
    data : pandas DataFrame with all possible predictors and response

    response: string, name of response column in data

    Returns:
    --------
    model: an "optimal" fitted statsmodels linear model
           with an intercept
           selected by forward selection
           evaluated by adjusted R-squared
    
    source: https://planspace.org/20150423-forward_selection_with_statsmodels/
    """
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {}".format(response,
                                           ' + '.join(selected + [candidate]))
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    
    formula = "{} ~ {}".format(response,
                                   ' + '.join(selected))
    model = smf.ols(formula, data).fit()
    return model


def cramers_v(x, y):
    """
    Parameters: x,y are 1-dimensional vectors
    Returns: Cramer's V test statistic which ranges from 0 to 1; 1 indicating high association
    Original source: https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9
    """
    confusion_matrix = pd.crosstab(x,y)
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r,k = confusion_matrix.shape
    phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
    rcorr = r-((r-1)**2)/(n-1)
    kcorr = k-((k-1)**2)/(n-1)
    return np.sqrt(phi2corr/min((kcorr-1),(rcorr-1)))

def association_test(df_assoc,print_high=False,high_threshold=0.7):
    """
    conducts association test for all columns in a dataframe
    
    Parameters
    ----------
    df_assoc : TYPE
        DESCRIPTION.
    print_high : TYPE, optional
        DESCRIPTION. The default is False. If true, prints out high association pairs.
    high_threshold : TYPE, optional
        DESCRIPTION. The default is 0.75. Threshold for what constitutes high association.

    Returns
    -------
    df_ret : dataframe
        DESCRIPTION.  DF with low half filled with Cramer's Vs

    """
    
    if (print_high):
        print('... outputting categorical variable pairs with Cramers V above {}'.format(high_threshold))
    
    # create the return dataframe with column and index labels equal to the input DF
    df_ret=pd.DataFrame(columns=df_assoc.columns,index=df_assoc.columns)
    
    # loop through the original DF to populate Cramer's Vs
    for index1 in range(df_assoc.shape[1]):
        col1=df_assoc.iloc[:,index1]
        for index2 in range(index1+1,df_assoc.shape[1]):
            col2=df_assoc.iloc[:,index2]
            cv=cramers_v(col1,col2)  # compute Cramer's V for this pair
            df_ret[df_assoc.columns[index1]][df_assoc.columns[index2]]=cv
            if (print_high):
                if (cv>=high_threshold):
                    print  ("high association: {} , {} {:.2f}".format(df_assoc.columns[index1],df_assoc.columns[index2],cv))
    return df_ret
    

def radius_is_valid(radius):
    '''
    Returns true if an integer is a positive, non-zero float
    Parameters
    ----------
    radius : TYPE
        accepts numbers as integers, numeric strings, or floats

    Returns
    -------
    bool

    '''
    # ignore the initial sentinal value
    if radius=="initial_not_valid":
        return False
    
    
    try:
        radius=float(radius) # must convert to float or this will throw a TypeError
        if radius>0:
            return True
        else:
            print ("... try again, the radius must be >0")
            return False
              
    except ValueError:
        print ("... try again, the radius must be a number")
        return False
    

    
def get_R2(df1_local,df2_local,radius):
    '''
    Parameters
    ----------
    df1_local : TYPE
        DESCRIPTION.
    df2_local : TYPE
        DESCRIPTION.
    radius : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''

    
    # rest Starbucks count to 0
    df1.loc[:,'starbucksCount']=0
    
    
    #starbucksDfRowCount=len(df2_local.index)  # compute before the loop for efficiency
    #start_time=time.time()
    for rowS in df2_local.itertuples():
        
        # output progress as a percentage
        #try:
        #    if ((rowS[0] %1000)==0):
        #        remaining_time_mins=(time.time()-start_time)/(rowS[0])*(starbucksDfRowCount-rowS[0])/60
        #        print("Complete {:.0%} Remaining: {:.2f} mins".format(rowS[0]/starbucksDfRowCount,remaining_time_mins))
        #except:
        #    pass        
        
            
        df1_local['sLat']=getattr(rowS,'latitude')
        df1_local['sLon']=getattr(rowS,'longitude')    
        
        
        # This works and is FAST!!! Full run is 12 seconds
        df1_local['starbucksCount']+= sb_in_range_vec(df1_local['latitude'].values,
                                                df1_local['longitude'].values,
                                                df1_local['sLat'].values,
                                                df1_local['sLon'].values,
                                                radius)
        
    
    X_local = df1.drop(columns = ['id','category','title','body','amenities','currency','fee','has_photo',
                        'pets_allowed','price_display','price_type','address','cityname',
                        'state','latitude','longitude','source','time','radius_to_starbucks_in_miles',
                        'sLat','sLon','Dogs','Refrigerator'], axis = 1)
    
    # Fill any remaining NAs with zeros (though there should not be any at this point)
    X_local=X_local.fillna(0)
    
    # Fix column label formats since ' ' and '/' throw off the modeling
    X_local.columns=X_local.columns.str.replace(' ','_')
    X_local.columns=X_local.columns.str.replace('/','_')
    
    # Run the forward selection model
    model=forward_selected(X_local,'price')
    
    return(model.rsquared_adj)
    
    
    
    
    
# ######################################################################################    
# These helper functions are old and slow so not used
# ######################################################################################    

# def starbucksInRange(tLat,tLon,sLat,sLon,radiusInMiles):
#     try: 
#         if ((geodesic((tLat,tLon),(sLat,sLon)).miles)<=radiusInMiles):
#             return 1
#         else:
#             return 0
#     except:
#         return 0


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here

    do_optimal_radius_calc = True #Whether to find the optimal radius. Warning long calculation
    # ###########################################################################################################
    # Let user know program has started
    # ###########################################################################################################
    print("Starting...")
    
    
    # ###########################################################################################################
    # Collect user input 
    # ###########################################################################################################
    
    # Set the radius around the apartment to count the # of Starbucks
    # R^2 actually peaks at 49.5% at 80 miles, all else constant; we use 5 miles for testing
    # start by setting to invalid sentinal value
    radius_to_starbucks_in_miles="initial_not_valid"
    while not radius_is_valid(radius_to_starbucks_in_miles):
        radius_to_starbucks_in_miles=input("Enter radius in miles to search for Stabucks locations around each apartment: ")
    radius_to_starbucks_in_miles=float(radius_to_starbucks_in_miles)
    
    
    # ###########################################################################################################
    # Read the data and handle missing data & outliers
    # ###########################################################################################################
    
    # read data into dataframe
    # Encoding issue: https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python
    
    # Read in the apartment data (note: it is semicolon separated)
    df1 = pd.read_csv('../data/apartments_for_rent_classified_10K.csv', sep=';',encoding = "ISO-8859-1")
    
    # Read in the starbucks store location data
    df2 = pd.read_csv('../data/starbucks_data.csv', sep=',',encoding = "ISO-8859-1")
    
    
    # replace null/missing amenities with 'none"
    df1['amenities'].fillna('none',inplace=True); # clean for vector math
    
    
    # replace missing bathrooms by setting equal to # of bedrooms
    df1['bathrooms'].fillna(df1['bedrooms'],inplace=True)
    
    # remove rows where bedrooms are blank or equal to 0
    nan_value = float("NaN")
    df1.replace(0, nan_value, inplace=True)
    df1.dropna(subset=["bedrooms"],inplace=True)
    
    # Remove the apartment with ID=5666447277 since price is miscoded at $52,500
    # don't need to do this since also had bedrooms=0
    
    # replace missing lat & long in both files with sentinel values that are
    # as far apart geographically as possible.  This is necessary since geodesic expects
    # well-formed data inputs. 
    df1.fillna({'latitude':90,'longitude':0},inplace=True)  # sentinel value of North Pole
    df2.fillna({'latitude':-90,'longitude':0},inplace=True)   # sentinel value of South Pole
    
    
    
    
    
    # ######################################################################################    
    # Append the # of Starbucks locations within an X (ex: 5) mile radius
    # of each apartment
    # ######################################################################################    
    
    print ("\nAppending starbucks count...")
    
    
    # Append this as a column in apartment dataframe (not strictly necessary)
    df1['radius_to_starbucks_in_miles']=radius_to_starbucks_in_miles
    
    
    # Append a column of 0s to the apartment dataframe to hold count of Starbucks
    df1.loc[:,'starbucksCount']=0
    
    
    starbucksDfRowCount=len(df2.index)  # compute before the loop for efficiency
    start_time=time.time()
    for rowS in df2.itertuples():
        
        # output progress as a percentage
        try:
            if ((rowS[0] %1000)==0):
                remaining_time_mins=(time.time()-start_time)/(rowS[0])*(starbucksDfRowCount-rowS[0])/60
                print("Complete {:.0%} Remaining: {:.2f} mins".format(rowS[0]/starbucksDfRowCount,remaining_time_mins))
        except:
            pass        
        
            
        df1['sLat']=getattr(rowS,'latitude')
        df1['sLon']=getattr(rowS,'longitude')    
        
        
        # This works and is FAST!!! Full run is 12 seconds
        df1['starbucksCount']+= sb_in_range_vec(df1['latitude'].values,
                                                df1['longitude'].values,
                                                df1['sLat'].values,
                                                df1['sLon'].values,
                                                radius_to_starbucks_in_miles)
        
        # slow since not vactorized; takes 446 mins to run
        # df1['starbucksCount']+=list(map(starbucksInRange,df1['latitude'].values,df1['longitude'].values,df1['sLat'].values,df1['sLon'].values,df1['radius_to_starbucks_in_miles'].values))
        
        # slow since not vactorized; slower than map version; this takes 485 mins to run
        # df1['starbucksCount']+=df1.apply(lambda row: starbucksInRange(row['latitude'],row['longitude'],row['sLat'],row['sLon'],row['radius_to_starbucks_in_miles']),axis=1)
        
        
        
        
    # ######################################################################################    
    # Create indicator variables for each amenity
    # ######################################################################################    
    
    print ("\nDetermining amenities...")
     
    # Create word count df of amenities
    # source: https://stackoverflow.com/questions/49189903/word-count-in-a-dataframe-column
    dfAmenities=(df1['amenities'].str.split(',',expand=True)
                  .stack()
                  .value_counts()
                  .rename_axis('amenity')
                  .reset_index(name='count'))    
    
    
    for amenity in list(dfAmenities['amenity']):
        df1[amenity]=hasAmenity(df1['amenities'].values.astype(str),amenity)
    try:
        del df1['none']  # we put "none" in so taking it out
    except:
        pass
    
    
    # ###################################################################################### 
    # create indicator variables for pets (cat, dogs)
    # ###################################################################################### 
       
    print ("\nDetermining pets...")
     
    # Create word count df of amenities
    # source: https://stackoverflow.com/questions/49189903/word-count-in-a-dataframe-column
    df1['pets_allowed'].fillna('None',inplace=True)
    dfPets=(df1['pets_allowed'].str.split(',',expand=True)
                  .stack()
                  .value_counts()
                  .rename_axis('pet')
                  .reset_index(name='count'))    
    
    
    for pet in list(dfPets['pet']):
        df1[pet]=hasAmenity(df1['pets_allowed'].values.astype(str),pet)
    try:
        del df1['None']  # removing none since don't want to regress on that
    except:
        pass
    
    
    # ######################################################################################   
    # Understand the data by executing several queries
    # ######################################################################################   
    
    print ("Performing some queries...")
    
    # 1. What is the average price of an apartment
    meanPrice=df1['price'].mean(axis=0,skipna=True)
    print ("\nThe mean apartment price is: {:.1f}".format(meanPrice))
    
    # 2. What percentage of apartments have wood floors
    print ("\nPercent of apartments with wood floors: {:.2%}"
           .format(df1[df1['Wood Floors']==1].shape[0]/df1.shape[0]))
    
    # 3. What is the median number of starbucks nearby
    print("\nThe median number of Starbucks within a {} mile radius is: {}"
          .format(radius_to_starbucks_in_miles,
                  df1['starbucksCount'].median(axis=0,skipna=True)))
    
    # 4. What is the average sq ft by # number of bedrooms 
    print("\nThe average sq ft by # of bedrooms is as follows:")
    df_bedroom_sqft=df1.sort_values(by=['bedrooms']).groupby('bedrooms',as_index=False).square_feet.mean()
    print(df_bedroom_sqft)
    
    df_bedroom_sqft.plot(kind='scatter',x='bedrooms',y='square_feet')
    
    
    
    # ######################################################################################   
    # Find the linear model using forward selection
    # ######################################################################################   
    
    # Initialize variables; start by dropping columns we do not want to regress on
    X = df1.drop(columns = ['id','category','title','body','amenities','currency','fee','has_photo',
                            'pets_allowed','price_display','price_type','address','cityname',
                            'state','latitude','longitude','source','time','radius_to_starbucks_in_miles',
                            'sLat','sLon'], axis = 1)
    
    # investigate multicollinearity in quant variables
    print("\nInvestigating multicollinearity in quant predictors...")
    df_quant=X.filter(['bedrooms','bathrooms','square_feet','starbucks_count'],axis=1)
    print(pd.DataFrame.corr(df_quant))
    # no major concerns about multicollinearity though r(bedrooms,bathrooms)=0.71
    
    
    # investigate association in categorical variables
    print("\nInvestigating associate in categorical predictors...")
    df_categOnly=X.iloc[:,5:]
    association_test(df_categOnly,True)
    # concerns here between cats&dogs; dishwasher&Refrigerator
    # drop dogs & Refridgerator
    X.drop(columns=['Dogs','Refrigerator'],axis=1,inplace=True)
    
    print ("\nDetermining linear model using forward selection...")
    
    # Fill any remaining NAs with zeros (though there should not be any at this point)
    X=X.fillna(0)
    
    # Fix column label formats since ' ' and '/' throw off the modeling
    X.columns=X.columns.str.replace(' ','_')
    X.columns=X.columns.str.replace('/','_')
    
    # Run the forward selection model
    model=forward_selected(X,'price')
    
    # output the results
    print (model.model.formula)
    #print(model.params)  # no need to do this since we will get the values in the summary
    print(model.summary())
    print ("Rsq = {:.2%}".format(model.rsquared_adj))
    
    
    # ######################################################################################   
    # Repeat forward selection WITHOUT starbucks counts; just output R^2
    # ######################################################################################   
    
    print ("\nDetermining R^2 without starbucksCount using forward selection...")
    
    X2=X.drop(columns=['starbucksCount'],axis=1,inplace=False)
    # Run the forward selection model
    model2=forward_selected(X2,'price')
    print ("Rsq without starbucksCount = {:.2%}".format(model2.rsquared_adj))
    
    # ######################################################################################   
    # Determine the radius that maximizes R^2
    # Using binary search seeking smallest positive difference between adjacent points
    # we are searching for the max of what we assume to be an inverted parabola
    # hence, we can look at adjacent points and move in the direction of whichever
    # has a higher R^2    
    # inspired by: https://leetcode.com/problems/find-peak-element/discuss/50232/find-the-maximum-by-binary-search-recursion-and-iteration
    # ######################################################################################   
    if do_optimal_radius_calc:
        print ("\nDetermining starbucks radius that maximizes R^2...")
        
        # Set up dataframe to store the intermediate results
        df_optimal_radius=pd.DataFrame(columns=['radius','R2'])
        
        # set low and high radius in miles for binary search
        low=1
        high=1000
        
        # set sentinal values for the optimal radius and optimal R^2
        optimal_R2=-1
        optimal_radius=-1
        
        while low<high:
            # get radius at midpoint and point right-adjacent to mid-point
            mid1=floor((high+low)/2)
            mid2=mid1+1
            print('... checking radii of {} miles and {} miles'.format(mid1,mid2))
            
            # compute the R^2 for the two points
            r2_mid1=get_R2(df1,df2,mid1)
            r2_mid2=get_R2(df1,df2,mid2)
            
            # store every value tested; there may be duplicates
            df_optimal_radius=df_optimal_radius.append({'radius':mid1,'R2':r2_mid1},ignore_index=True)
            df_optimal_radius=df_optimal_radius.append({'radius':mid2,'R2':r2_mid2},ignore_index=True)
            
            # update search location & optimal value
            if (r2_mid1<r2_mid2):
                low=mid2
                if (r2_mid2>=optimal_R2):
                    optimal_R2=r2_mid2
                    optimal_radius=mid2
            else: 
                high=mid1
                if (r2_mid1>=optimal_R2):
                    optimal_R2=r2_mid1
                    optimal_radius=mid1
            
            # output the current optimal values
            print ("... current optimal radius is {} miles with R^2 of {:.2%}".format(optimal_radius,optimal_R2))
            
            
        print("The FINAL optimal radius is {} miles with an R^2 of {:.2%}".format(optimal_radius,optimal_R2))
    
    # ######################################################################################   
    # output final DF to CSV including new indicator variables.  Dropped rows will NOT be included
    # ######################################################################################   
    df1.to_csv('out_vec' + datetime.now().strftime("%Y%m%d-%H%M%S")+ '.csv',index=False,encoding='utf-8')
    if do_optimal_radius_calc:
        df_optimal_radius.to_csv('../data/out_radius' + datetime.now().strftime("%Y%m%d-%H%M%S")+ '.csv',index=False,encoding='utf-8')
        radius_to_starbucks_in_miles = optimal_radius
    # ######################################################################################   
    # Finsh up
    # ######################################################################################   
    
    print ("\nDone Starbucks")

#%%
print("\nAttempt to use KNN to predict if a listing is in New York, San Francisco, or other")
data=df1
data["location"] = ["other"] * len(data) #Create a basic data column prepopulated with other
data.loc[data['cityname'] == 'New York', 'location'] = "New York"
data.loc[data['cityname'] == 'San Francisco', 'location'] = "San Francisco"

#We use a labelencoder to convert our 3 categories into numbers
le = preprocessing.LabelEncoder()
encoded_location=le.fit_transform(data["location"])
list(le.classes_)
data["encodedloc"] = encoded_location
data["hasAmenities"] = [1] * len(data)
data.loc[pd.isna(data['amenities']), 'hasAmenities'] = 0

#The features of the neighbors are hasAmenities and Price
features=list(zip(data["hasAmenities"][0:1000],data["price"][0:1000]))
model = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training sets, the first 1000 listings
model.fit(features,data["encodedloc"][0:1000])

#predict for the test set
actuals = list(zip(data["hasAmenities"][1000:9795],data["price"][1000:9795]))
predicted = model.predict(actuals)
correct_values = data["encodedloc"][1000:9795].tolist()

test_all_other = [2] * len(correct_values)
print("The Accuracy of the predicted model:", metrics.accuracy_score(correct_values, predicted))
print("The Accuracy if we only guessed other would be:", metrics.accuracy_score(correct_values, test_all_other))
#Having so much "other blows out the dataset, need to reevaluate

#%%
#Lets try and predict the number of bedrooms now based on location, amenities, and price
print("\nNow we will attempt to predict bedrooms instead")
features=list(zip(data["hasAmenities"][0:1000],data["price"][0:1000],data["bathrooms"][0:1000]))
model = KNeighborsClassifier(n_neighbors=3)
# Train the model using the training sets
actuals = list(zip(data["hasAmenities"][1000:9795],data["price"][1000:9795],data["bathrooms"][1000:10000]))
model.fit(features,data["bedrooms"][0:1000])
predicted = model.predict(actuals)
correct_values = data["bedrooms"][1000:9795].tolist()
print("Accuracy of bedroom predictions:", metrics.accuracy_score(correct_values, predicted))

#%%
#Let's find the top cities
sorted_counts_frame = data.groupby("cityname").size().reset_index(name='counts').sort_values(by=['counts'],ascending=False)
print(sorted_counts_frame.head(10))
print("\nThe top 4 cities are all in Texas, lets make a dataframe with only the Texas entries")
print("Now lets try to predict which city a listing is for in Texas")
texas_cities = ["Austin","Dallas", "Houston", "San Antonio"]
texas_data = data[data["cityname"].isin(texas_cities)]
city_encoder = preprocessing.LabelEncoder()
encoded_city=city_encoder.fit_transform(texas_data["cityname"])
features=list(zip(texas_data["price"][0:300],texas_data["square_feet"][0:300]))
city_model = KNeighborsClassifier(n_neighbors=3)
city_model.fit(features,encoded_city[0:300])
actual_city_features = list(zip(texas_data["price"][300:1107],texas_data["square_feet"][300:1107]))
predicted_encoded = city_model.predict(actual_city_features)
predicted_cities = city_encoder.inverse_transform(predicted_encoded.astype(int))
correct_encoded = encoded_city[300:1107]
correct_values = city_encoder.inverse_transform(encoded_city[300:1107])
all_austin = ["Austin"] * len(correct_values) #If we just guessed the most common city
print("Accuracy:", metrics.accuracy_score(correct_values, predicted_cities))
print("Accuracy if guessing most common city:", metrics.accuracy_score(correct_values, all_austin))

#%%
#Let's find the top cities
print("Now lets try to predict which city a listing is for in Texas with  starbucks in {0} mile radius".format(str(radius_to_starbucks_in_miles)))
texas_cities = ["Austin","Dallas", "Houston", "San Antonio"]
texas_data = data[data["cityname"].isin(texas_cities)]
city_encoder = preprocessing.LabelEncoder()
encoded_city=city_encoder.fit_transform(texas_data["cityname"])
features=list(zip(texas_data["price"][0:300],texas_data["square_feet"][0:300],texas_data["starbucksCount"][0:300]))
city_model = KNeighborsClassifier(n_neighbors=3)
city_model.fit(features,encoded_city[0:300])
actual_city_features = list(zip(texas_data["price"][300:1107],texas_data["square_feet"][300:1107],texas_data["starbucksCount"][300:1107]))
predicted_encoded = city_model.predict(actual_city_features)
predicted_cities = city_encoder.inverse_transform(predicted_encoded.astype(int))
correct_encoded = encoded_city[300:1107]
correct_values = city_encoder.inverse_transform(encoded_city[300:1107])
all_austin = ["Austin"] * len(correct_values) #If we just guessed the most common city
print("Accuracy:", metrics.accuracy_score(correct_values, predicted_cities))
print("Accuracy if guessing most common city:", metrics.accuracy_score(correct_values, all_austin))
