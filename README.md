# SQLAlchemy-challenge: Surf's Up!

<b><i>To help with trip planning to Honolulu, Hawaii, I did some climate analysis on the area.</i></b>
<br><br>
<b>Climate Analysis and Exploration</b><br>
<i>I used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.</i><br>
<br>
[x] Use SQLAlchemy create_engine to connect to your sqlite database.<br>
[x] Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.<br>
[x] Link Python to the database by creating an SQLAlchemy session.<br>
<br>
<b>Precipitation Analysis</b><br>
[x] Find the most recent date in the data set.<br>
[x] Retrieve the last 12 months of precipitation data by querying the 12 preceding months of data.<br>
[x] Select only the date and prcp values.<br>
[x] Load the query results into a Pandas DataFrame and set the index to the date column.<br>
[x] Sort the DataFrame values by date.<br>
[x] Plot the results using the DataFrame plot method.<br>
[x] Use Pandas to print the summary statistics for the precipitation data.<br>
<br>
<b>Station Analysis</b><br>
[x] Design a query to calculate the total number of stations in the dataset.<br>
[x] Design a query to find the most active stations (i.e. which stations have the most rows?).<br>
[x] List the stations and observation counts in descending order.<br>
[x] Using the most active station id, calculate the lowest, highest, and average temperature.<br>
[x] Design a query to retrieve the last 12 months of temperature observation data (TOBS).<br>
[x] Filter by the station with the highest number of observations.<br>
[x] Query the last 12 months of temperature observation data for this station.<br>
[x] Plot the results as a histogram with bins=12.<br>
[x] Close out your session.<br>
<br>
<br>
<b>Climate App</b><br>
<i>Design a Flask API based on the queries that you have just developed.</i><br>
<br>
[x] Use Flask to create your routes.<br>
[x] List all routes that are available.<br>
[x] Convert the query results to a dictionary using date as the key and prcp as the value.<br>
[x] Return the JSON representation of your dictionary.<br>
[x] Return a JSON list of stations from the dataset.<br>
[x] Query the dates and temperature observations of the most active station for the last year of data.<br>
[x] Return a JSON list of temperature observations (TOBS) for the previous year.<br>

<h1>References</h1><br>
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: <b>An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology</b>, 29, 897-910, https://doi.org/10.1175/JTECH-D-11-00103.1
