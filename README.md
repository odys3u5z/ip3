# 🌐 Web Scraping Code for BIM/VDC Job Analysis

This repository contains a detailed web scraping implementation for analyzing job listings related to BIM/VDC professionals in English and German-speaking countries. The goal is to compare job requirements and skills between the two cultures, assessing their impact on intercultural collaboration. The project utilizes Google Chrome WebDriver for web scraping and provides code for data verification and visualization, including bar diagrams, reverse search, and heatmaps.

Step 1: Import necessary libraries
The program starts by importing the necessary libraries such as Selenium, Pandas, NumPy, Matplotlib, Geopy, and Folium, which facilitate web scraping, data processing, geocoding, and visualization.

Step 2: Define get_url() function
The get_url() function establishes a connection with the Google Chrome WebDriver, navigates through job listing websites, and collects URLs for each job posting related to BIM/VDC professionals. The function then saves these URLs in a CSV file named url.csv.

Step 3: Execute get_url() function
The program runs the get_url() function to collect the URLs of the job postings.

Step 4: Define get_data() function
The get_data() function connects to the WebDriver, reads the collected URLs from url.csv, and scrapes job information from the associated web pages. The scraped data is then saved in a CSV file named Data___(date).csv.

Step 5: Execute get_data() function
The program runs the get_data() function to extract the job information from the URLs collected in Step 3.

Step 6: Geocode job listings
The program uses the Geopy library and Nominatim geocoding service to georeference the job listing addresses, converting them into latitude and longitude coordinates.

Step 7: Create heatmap
The program uses the Folium library to create an interactive heatmap of job listings based on the georeferenced coordinates, visualizing the distribution of job listings by location.

Step 8: Generate bar diagrams
The program generates bar diagrams to visualize the number of results obtained per search, allowing for a comparison of job listing quantities across different sources.

Step 9: Perform reverse search
The program conducts a reverse search to verify the presence of specific keywords (BIM-Manager, BIM-Coordinator, and BIM-Specialist) in each dataset. The results are visualized using horizontal bar charts.

Step 10: Save and display results
The program saves the heatmap as an HTML file and displays the bar diagrams and reverse search results using Matplotlib.

Throughout the entire process, the program performs data verification and visualization, ensuring the accuracy and completeness of the collected data before proceeding with further analysis.
