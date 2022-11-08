### Question 1: Algorithm Understanding
How does the Prophet Algorithm differ from an LSTM?
Why does an LSTM have poor performance against ARIMA and Profit for Time Series?

### Answer to Question 1
- Prophet Algorithm is based on additive regression model with components such as trend, seasonality and holidays. It is specifically designed to be used in detecting patters in business time series forecasting (like stock predictions). Prophet is based on low complexity and prioritizes ease of use and tuning. Time series prediction is one of the many use cases where LSTM can be used. 
- ARIMA performs better when there is smaller datasets whereas LSTM performs better when dealing with large data. 

----------------------------------------------------------------
### Question 2: Interview Readiness
What is exponential smoothing and why is it used in Time Series Forecasting?

### Answer to Question 2
- It is a time series forecasting method for univariate (i.e. involving one variable quantity) where prediction uses an exponentially decreasing weighted sum of past predictions (as observations get older). This method gives more importance to the newer/recent data in the series. 

----------------------------------------------------------------
### Question 3: Interview Readiness
What is stationarity? What is seasonality? Why Is Stationarity Important in Time Series Forecasting?

### Answer to Question 3
- Stationarity is a time series whose properties don't depend on trend, periodic fluctions (seasonality) and has constant variance over time. For example, a linear function is a stationarity example where the change over time is constant. 
- Seasonality (seasonal variation) is the presence of variations that occur or repeat regularly (at regular intervals) over time. Example, sales volume around holidays. 
- Stationarity is important in time series forecasting because of the assumption that predicted statistical properties of the time series remain constant (or same) in the future as in the past. Non-stationarity can lead to erroneous and misleading forecasting (because of unpredictability). 

----------------------------------------------------------------
### Question 4: Interview Readiness
How is seasonality different from cyclicality? Fill in the blanks:
___ is predictable, whereas ___ is not.

### Answer to Question 4
- The seasonality is periodic movement associated with some aspect of calendar year. It is usually a fixed or known period (monthly, quarterly, weekly, etc). Example is houses for sale, usually see spike in houses for sale in the spring. Or electicity demand. 
- Cyclicality in data series (ups and downs) are not associated with a fixed term or period. Example is recession. 
- Seasonality is predictable, whereas cyclicality is not.

----------------------------------------------------------------