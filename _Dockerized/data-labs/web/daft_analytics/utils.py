import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
import xgboost
import os.path
from django.conf import settings

# FILE PATHS
my_path = os.path.abspath(os.path.dirname(__file__))
cork_path = os.path.join(settings.BASE_DIR, "daft_analytics/datasets/cork_sales_2018.csv")
dublin_path = os.path.join(settings.BASE_DIR, "daft_analytics/datasets/dublin_sales_2018.csv")
galway_path = os.path.join(settings.BASE_DIR, "daft_analytics/datasets/galway_sales_2018.csv")
limerick_path = os.path.join(settings.BASE_DIR, "daft_analytics/datasets/limerick_sales_2018.csv")


def price_regressor(dataset, area, property_type, bedrooms, bathrooms):
    dataset = pd.read_csv(dataset)
    X = dataset.iloc[:, 1:5].values
    y = dataset.iloc[:, 5:6].values

    labelencoder_X_0 = LabelEncoder()
    X[:, 0] = labelencoder_X_0.fit_transform(X[:, 0])  ## transform county
    onehotencoder = OneHotEncoder(categorical_features=[0, 1])
    X = onehotencoder.fit_transform(X).toarray()
    X = X[:, 1:]  ## remove first column to avoid dummy variable trap

    ## fit regressors
    regressor = RandomForestRegressor(n_estimators=300, random_state=0)
    regressor.fit(X, y)

    xgb = xgboost.XGBRegressor(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75,
                               colsample_bytree=1, max_depth=7)
    xgb.fit(X, y)

    ## preidct price of a property

    home = np.array([[area, property_type, bedrooms, bathrooms]])
    home[:, 0] = labelencoder_X_0.transform(home[:, 0])
    home = onehotencoder.transform(home).toarray()
    home = home[:, 1:]

    rf_pred = int(regressor.predict(home))
    xgb_pred = int(xgb.predict(home))

    return [rf_pred, xgb_pred]


# Variables

types = ('House', 'Apartment')

cork_areas = (
    'Ballinlough', 'Ballintemple', 'Ballyphehane', 'Ballyvolane', 'Banduff', 'Bishopstown', 'Blackpool', 'Blackrock',
    'Blarney', 'Carrigrohane',
    'Clogheen', 'Cloghroe', 'Cork City', 'Curraheen', 'Dillons Cross', 'Donnybrook', 'Donoughmore', 'Douglas',
    'Dublin Pike', 'Fairhill', 'Farran',
    'Farranree', 'Fota', 'Frankfield', 'Glanmire', 'Glasheen', 'Grange', 'Gurranabraher', 'Hollyhill', 'Inniscarra',
    'Killeens', 'Lehenaghmore',
    'Little Island', 'Mahon', 'Mallow', 'Mayfield', 'Model Farm Road', 'Montenotte', 'Ovens', 'Passage West',
    'Rathpeacon',
    'Rochestown', 'Shanakiel',
    'Silversprings', 'St. Lukes', "Sunday's Well", 'The Lough', 'Tivoli', 'Togher', 'Togher (Cork City)',
    'Turners Cross', 'Victoria Cross', 'Waterfall', 'Western Road', 'Wilton')

dublin_areas = (
    'Adamstown', 'Arbour Hill', 'Ard Na Greine', 'Artane', 'Ashtown', 'Aylesbury', 'Ayrfield', 'Balbriggan', 'Baldoyle',
    'Balgriffin', 'Ballinteer', 'Ballsbridge', 'Ballyboden', 'Ballybough',
    'Ballyboughal', 'Ballybrack', 'Ballycorus', 'Ballycullen', 'Ballyfermot', 'Ballymun', 'Balrothery', 'Bayside',
    'Beaumont', 'Blackrock', 'Blanchardstown', 'Bluebell', 'Booterstown',
    'Cabinteely', 'Cabra', 'Carrickmines', 'Castleknock', 'Chapelizod', 'Cherry Orchard', 'Christchurch', 'Churchtown',
    'Citywest', 'Clarehall', 'Clondalkin', 'Clonee', 'Clongriffin',
    'Clonshaugh', 'Clonsilla', 'Clonskeagh', 'Clontarf', 'Coolmine', 'Coolock', 'Crumlin', 'Dalkey', 'Darndale',
    'Dartry',
    'Deans Grange', 'Donabate', 'Donaghmede', 'Donnybrook',
    'Donnycarney', 'Drimnagh', 'Drumcondra', 'Dublin 1', 'Dublin 2', 'Dublin 4', 'Dublin 7', 'Dublin 8',
    'Dun Laoghaire',
    'Dundrum', 'East Wall', 'Fairview', 'Finglas', 'Firhouse',
    'Foxrock', 'Garristown', 'Glasnevin', 'Glasthule', 'Glenageary', 'Goatstown', 'Greenhills', "Harold's Cross",
    'Hartstown', 'Hollystown', 'Howth', 'IFSC', 'Inchicore', 'Islandbridge',
    'Kilbarrack', 'Killester', 'Killiney', 'Kilmainham', 'Kilmore', 'Kilnamanagh', 'Kilsallaghan', 'Kilternan',
    'Kiltipper',
    'Kimmage', 'Kingswood', 'Kinsealy', 'Knocklyon', 'Leopardstown',
    'Loughlinstown', 'Loughshinny', 'Lucan', 'Lusk', 'Malahide', 'Marino', 'Merrion', 'Milltown', 'Monkstown',
    'Mount Merrion', 'Mulhuddart', 'Naul', 'Navan Road (D7)', 'Newcastle',
    'North Circular Road', 'North Strand', 'Oldbawn', 'Oldtown', 'Ongar', 'Palmerstown', 'Park West', 'Perrystown',
    'Phibsborough', 'Poppintree', 'Porterstown', 'Portmarnock', 'Portobello',
    'Priorswood', 'Raheny', 'Ranelagh', 'Rathcoole', 'Rathfarnham', 'Rathgar', 'Rathmichael', 'Rathmines', 'Rialto',
    'Ringsend', 'Royal Canal Park', 'Rush', 'Saggart', 'Sallynoggin',
    'Sandycove', 'Sandyford', 'Sandymount', 'Santry', 'Shankill', 'Skerries', 'Smithfield', 'Stepaside', 'Stillorgan',
    'Stoneybatter', 'Sutton', 'Swords', 'Tallaght', 'Temple Bar',
    'Templeogue', 'Terenure', 'The Ward', 'Tyrrelstown', 'Walkinstown', 'Whitehall')

galway_areas = (
    'Ballybane', 'Ballybrit', 'Barna', 'Boleybeg', 'Bushy Park', 'Castlegar', 'Dangan', 'Doughiska', 'Galway City',
    'Headford Road', 'Killeen', 'Kingston', 'Knocknacarra', 'Menlo',
    'Merlin', 'Merlin Park', 'Mervue', 'Newcastle', 'Rahoon', 'Renmore', 'Roscam', 'Salthill', 'Shantalla',
    "Taylor's Hill",
    'Tirellan', 'Tuam Road', 'Wellpark', 'Woodquay')

limerick_areas = (
    'Annacotty', 'Ballinacurra', 'Ballynanty', 'Ballysimon', 'Caherdavin', 'Castleconnell', 'Castletroy', 'Clareview',
    'Corbally', 'Dooradoyle', 'Ennis Road', 'Garryowen',
    'Janesboro', 'Limerick City', 'Monaleen', 'Moyross', 'North Circular Road', 'Raheen', 'Rhebogue', 'Singland',
    'South Circular Road', 'Thomondgate')

areas = ('Adamstown', 'Annacotty', 'Arbour Hill', 'Ard Na Greine', 'Artane', 'Ashtown', 'Aylesbury', 'Ayrfield',
         'Balbriggan', 'Baldoyle', 'Balgriffin', 'Ballinacurra', 'Ballinlough', 'Ballinteer', 'Ballintemple',
         'Ballsbridge', 'Ballybane', 'Ballyboden', 'Ballybough', 'Ballyboughal', 'Ballybrack', 'Ballybrit',
         'Ballycorus', 'Ballycullen', 'Ballyfermot', 'Ballymun', 'Ballynanty', 'Ballyphehane', 'Ballysimon',
         'Ballyvolane', 'Balrothery', 'Banduff', 'Barna', 'Bayside', 'Beaumont', 'Bishopstown', 'Blackpool',
         'Blackrock', 'Blackrock', 'Blanchardstown', 'Blarney', 'Bluebell', 'Boleybeg', 'Booterstown', 'Bushy Park',
         'Cabinteely', 'Cabra', 'Caherdavin', 'Carrickmines', 'Carrigrohane', 'Castleconnell', 'Castlegar',
         'Castleknock', 'Castletroy', 'Chapelizod', 'Cherry Orchard', 'Christchurch', 'Churchtown', 'Citywest',
         'Clarehall', 'Clareview', 'Clogheen', 'Cloghroe', 'Clondalkin', 'Clonee', 'Clongriffin', 'Clonshaugh',
         'Clonsilla', 'Clonskeagh', 'Clontarf', 'Coolmine', 'Coolock', 'Corbally', 'Cork City', 'Crumlin', 'Curraheen',
         'Dalkey', 'Dangan', 'Darndale', 'Dartry', 'Deans Grange', 'Dillons Cross', 'Donabate', 'Donaghmede',
         'Donnybrook', 'Donnybrook', 'Donnycarney', 'Donoughmore', 'Dooradoyle', 'Doughiska', 'Douglas', 'Drimnagh',
         'Drumcondra', 'Dublin 1', 'Dublin 2', 'Dublin 4', 'Dublin 7', 'Dublin 8', 'Dublin Pike', 'Dun Laoghaire',
         'Dundrum', 'East Wall', 'Ennis Road', 'Fairhill', 'Fairview', 'Farran', 'Farranree', 'Finglas', 'Firhouse',
         'Fota', 'Foxrock', 'Frankfield', 'Galway City', 'Garristown', 'Garryowen', 'Glanmire', 'Glasheen', 'Glasnevin',
         'Glasthule', 'Glenageary', 'Goatstown', 'Grange', 'Greenhills', 'Gurranabraher', "Harold's Cross", 'Hartstown',
         'Headford Road', 'Hollyhill', 'Hollystown', 'Howth', 'IFSC', 'Inchicore', 'Inniscarra', 'Islandbridge',
         'Janesboro', 'Kilbarrack', 'Killeen', 'Killeens', 'Killester', 'Killiney', 'Kilmainham', 'Kilmore',
         'Kilnamanagh', 'Kilsallaghan', 'Kilternan', 'Kiltipper', 'Kimmage', 'Kingston', 'Kingswood', 'Kinsealy',
         'Knocklyon', 'Knocknacarra', 'Lehenaghmore', 'Leopardstown', 'Limerick City', 'Little Island', 'Loughlinstown',
         'Loughshinny', 'Lucan', 'Lusk', 'Mahon', 'Malahide', 'Mallow', 'Marino', 'Mayfield', 'Menlo', 'Merlin',
         'Merlin Park', 'Merrion', 'Mervue', 'Milltown', 'Model Farm Road', 'Monaleen', 'Monkstown', 'Montenotte',
         'Mount Merrion', 'Moyross', 'Mulhuddart', 'Naul', 'Navan Road (D7)', 'Newcastle', 'Newcastle',
         'North Circular Road', 'North Circular Road', 'North Strand', 'Oldbawn', 'Oldtown', 'Ongar', 'Ovens',
         'Palmerstown', 'Park West', 'Passage West', 'Perrystown', 'Phibsborough', 'Poppintree', 'Porterstown',
         'Portmarnock', 'Portobello', 'Priorswood', 'Raheen', 'Raheny', 'Rahoon', 'Ranelagh', 'Rathcoole',
         'Rathfarnham', 'Rathgar', 'Rathmichael', 'Rathmines', 'Rathpeacon', 'Renmore', 'Rhebogue', 'Rialto',
         'Ringsend', 'Rochestown', 'Roscam', 'Royal Canal Park', 'Rush', 'Saggart', 'Sallynoggin', 'Salthill',
         'Sandycove', 'Sandyford', 'Sandymount', 'Santry', 'Shanakiel', 'Shankill', 'Shantalla', 'Silversprings',
         'Singland', 'Skerries', 'Smithfield', 'South Circular Road', 'St. Lukes', 'Stepaside', 'Stillorgan',
         'Stoneybatter', "Sunday's Well", 'Sutton', 'Swords', 'Tallaght', "Taylor's Hill", 'Temple Bar', 'Templeogue',
         'Terenure', 'The Lough', 'The Ward', 'Thomondgate', 'Tirellan', 'Tivoli', 'Togher', 'Togher (Cork City)',
         'Tuam Road', 'Turners Cross', 'Tyrrelstown', 'Victoria Cross', 'Walkinstown', 'Waterfall', 'Wellpark',
         'Western Road', 'Whitehall', 'Wilton', 'Woodquay')
