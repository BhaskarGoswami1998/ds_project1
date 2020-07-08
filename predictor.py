import pandas as pd
import joblib
model_not_NA = joblib.load(r'C:\Users\Venom\Documents\ds_project1\model.pkl')
model_NA = joblib.load(r'C:\Users\Venom\Documents\ds_project1\modelNA.pkl')
def predictions(data):
	selected = ['Month', 'Longitude', 'dist_from_north', 'prev_year','prev_2year','prev_3year','city_month_mean',
            'days_rolling_mean','years_rolling_mean','is_neg_percent','city_season_mean']
	city_agg = pd.read_csv(r'C:\Users\Venom\Desktop\694560_1215964_bundle_archive\agg\city_agg.csv')
	city_month_agg = pd.read_csv(r'C:\Users\Venom\Desktop\694560_1215964_bundle_archive\agg\city_month_agg.csv')
	city_season_agg = pd.read_csv(r'C:\Users\Venom\Desktop\694560_1215964_bundle_archive\agg\city_season_agg.csv')
	ymd_agg = pd.read_csv(r'C:\Users\Venom\Desktop\694560_1215964_bundle_archive\agg\ymd_agg.csv')
	city_season_agg['combined'] = city_season_agg.City.astype(str)+"_"+city_season_agg.Season.astype(int).astype(str)
	city_month_agg['combined1'] = city_month_agg.City.astype(str)+"_"+city_month_agg.Month.astype(int).astype(str)
	#need to write code form two seperate models
	na_flag = data['NA']
	temp = {}
	temp['City'] = data['City']
	temp['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y')
	temp['Day'] =temp['Date'].day
	temp['Month'] = temp['Date'].month
	temp['Year'] =temp['Date'].year
	temp['Season'] = (temp['Month']%12 + 3)//3

	temp['prev_year'] = ymd_agg[(ymd_agg.City==temp['City'])&(ymd_agg.Month==temp['Month'])&(ymd_agg.Day==temp['Day'])&(ymd_agg.Year==(temp['Year']-1))]['AvgTemperature'].iloc[0]
	temp['prev_2year']= ymd_agg[(ymd_agg.City==temp['City'])&(ymd_agg.Month==temp['Month'])&(ymd_agg.Day==temp['Day'])&(ymd_agg.Year==(temp['Year']-2))]['AvgTemperature'].iloc[0]
	temp['prev_3year']= ymd_agg[(ymd_agg.City==temp['City'])&(ymd_agg.Month==temp['Month'])&(ymd_agg.Day==temp['Day'])&(ymd_agg.Year==(temp['Year']-3))]['AvgTemperature'].iloc[0]
	temp['combined1'] = str(temp['City'])+"_"+str(temp['Month'])
	temp['combined'] = str(temp['City'])+"_"+str(temp['Season'])
	test_data = pd.DataFrame({'x':temp}).transpose()
	test_data = test_data.merge(city_season_agg[['combined','city_season_mean']], on = 'combined')
	test_data = test_data.merge(city_month_agg[['combined1','city_month_mean']], on = 'combined1')
	test_data = test_data.merge(city_agg, on = 'City')
	test_data['Month'] = test_data['Month'].astype(int)
	test_data['prev_year'] = test_data['prev_year'].astype(float)
	test_data['prev_2year'] = test_data['prev_2year'].astype(float)
	test_data['prev_3year'] = test_data['prev_3year'].astype(float)
	#print(test_data[selected].dtypes)
	if na_flag==0:	
		print(model_not_NA.predict(test_data[selected])[0])
	else:
		print(model_NA.predict(test_data[selected])[0])
d = {'City':'Sapporo','Date':'01-01-2020',"NA":0}
predictions(d)
