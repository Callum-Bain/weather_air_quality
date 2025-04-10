CREATE DATABASE weather_aqi;

CREATE TABLE weather_data (
    datetime_stamp TEXT PRIMARY KEY,
    datetime TIME,
    temp DECIMAL,
    feelslike DECIMAL,
    humidity DECIMAL,
    dew DECIMAL,
    precip DECIMAL,
    precipprob DECIMAL,
    snow DECIMAL,
    snowdepth DECIMAL,
    preciptype DECIMAL,
    windgust DECIMAL,
    windspeed DECIMAL,
    winddir DECIMAL,
    pressure DECIMAL,
    visibility DECIMAL,
    cloudcover DECIMAL,
    solarradiation DECIMAL,
    solarenergy DECIMAL,
    uvindex DECIMAL,
    severerisk DECIMAL,
    conditions TEXT,
    icon TEXT,
    source TEXT,
    date DATE
);

CREATE TABLE air_quality (
    datetime_stamp TEXT PRIMARY KEY,
    co DECIMAL,
    h DECIMAL,
    no2 DECIMAL,
    o3 DECIMAL,
    p DECIMAL,
    pm10 DECIMAL,
    pm25 DECIMAL,
    so2 DECIMAL,
    t DECIMAL,
    w DECIMAL,
    date DATE,
    datetime TIME,
    AQI DECIMAL,
    AQI_Category TEXT,
    FOREIGN KEY (datetime_stamp) REFERENCES weather_data(datetime_stamp)
);
