# Data Science 
# Project to Predict the Average Temperature for the Next Year Across various Cities

## Resources
https://www.kaggle.com/sudalairajkumar/daily-temperature-of-major-cities - Dataset
## Exploratory Data Analysis
![](images/dist_avg_temp.png)

-Trend of average temperature is increasing with time.The middle of the year experiences the hottest of average temperature.There is a huge -spike at the end of every month

![](images/avg_temp_year.png)

### Finding a relatio between the calculated lattitudes, longitudes, distance from the poles with average temperature
-Very less variance of average temperature between 8000 to 12000 km 
-Very less variance of average temperature between -15 to +15

![](images/avg_temp_lat.png)

1. These 4 Cities have multiple entries as there are two different cities with the same name as their states are different :
   - Charleston :  ['South Carolina' 'West Virginia'],
   - Columbus :    ['Georgia' 'Ohio'],
   - Portland :    ['Maine' 'Oregon'],
   - Springfield:  ['Illinois' 'Missouri'].
2. The Region shows a change in trend when one goes from south to northern hemisphere as the season cycle changes

![](images/avg_temp__region_month.png)

3. North America and Europe have very less Average Temperature across the year.
4. South America, Middle East and Africa have above average temperature.

![](images/avg_temp_region.png)

## Data CLeaning and Preprocessing

1. Dropping duplicates
2. Removing 2020  data as it is fairly recently and may contain imputed data
3. Removing outliers as temperatures below -50
4. Merging the City data that has the latitude and longitudes of the cities and their distances from the north and south pole
5. Drop State as it has 50% null values and is of no use to the model
6. Creating Date column from the Day ,Month, Year for identifying time based patterns
7.Sorting values by Date and saving the preprocessed dataframe in a csv for use in the future


## Baseline model and metrics for evaluation 

1. Base model with target encoded features and two level features is built.
2. The features used are :
   - Month.
   - Longitudinal position of the city.
   - Distance from North.
   - The average temperature of the city a year ago.
   - The average temperature of the city 2 years ago.
   - The average temperature of the city 3 years ago.
   - The mean average temperature of a city in a prticular month in the past.
   - 30 days rolling mean city wise.
   - 1 year rolling mean city wise.
   - percentage of temperature in each city that is below 0 
   - the mean temperature of a city in a particular season   
3. Lag features created.
4. Metrics decided are :
   - Distribution of actual vs predicted values.
   - RMSE and MAE of 4,9,3.6 respectively
   - Percentage of predictions having an error of 
      - SPOT ON % :  10.42181508308479
      - +-3 % :  55.67106945036217
      - +-5 % :  74.92969748615253
      - +-7 % :  85.89902002556455
      - +-10 % :  94.30762675756284

5. Distribution of Prediction and Actual:

![](images/dist_of_pred_act.png)

6. Scatter plot of  actual and predicted:

![](images/scatterplot.png)

7. Feature Importance:

![](images/features.png)

## Clusters need to be created

1. We need to create 2 seperate models for the 2 zones of average temperatures.
2. Create seperate model NA as they have different trends of Average Temperature.
   - SPOT ON % :  7.281493819584465
   - +-3 % :  40.52599281143158
   - +-5 % :  60.27702288068729
   - +-7 % :  74.05803454019461
   - +-10 % :  86.0383974752345

For NA the feature importances and the scatterplots are as follows:
![](images/features1.png)

![](images/scatter1.png)

![](images/dist_act_pres_1.png)

## Forward chaining cross validation

