# 📖 Space Biosciences Bibliometric Analysis - README

Welcome to the Space Biosciences Bibliometric Analysis repository. This repository includes Python scripts and Jupyter notebooks for performing a bibliometric analysis of the fields of Astrobiology (AB), Bioastronautics (BA), and Space Bioprocess Engineering (SBE).

## 🚀 Project Structure

### 📚 BibAnalysis 

This directory contains the Python scripts which are used for creating word clouds from the abstracts and parsing the bibliography.

### 📔 Cleaned Space Biosciences Analysis.ipynb 

A Jupyter notebook that presents the cleaned and prepared data from the Space Biosciences bibliometric analysis.

### 🗄️ Data 

This directory contains all the relevant data used and generated throughout the project. It is further categorized into three sub-directories: Geographic, Tabular, and Text.

#### 🌍 Geographic

Geospatial data, including shapely geometry files for each study area (AB, BA, SBE).

#### 📊 Tabular

All tabular data in CSV and Excel format, including bibliography data and affiliation count.

#### 📝 Text

Contains the textual data such as query statements and abstracts.

#### 🗃️ RIS

This directory contains RIS files that were used to create network graph visualizations in the manuscript using VOSviewer. These files are essential for reproducing the visualizations we created. If you'd like to recreate these network images, you can download VOSviewer from [here](http://www.vosviewer.com/download). 

To use VOSviewer with the provided RIS files, follow the instructions provided in the VOSviewer manual or follow the steps below:

1. Download and install VOSviewer.
2. Open VOSviewer and select 'Create' -> 'Create a map based on bibliographic data'.
3. Navigate to the 'Data/RIS' directory in this repository and select the RIS file you want to visualize.
4. Follow the prompts in VOSviewer to customize and create your visualization.

### 📊 Keyword Table Analysis.ipynb 

A Jupyter notebook containing the analysis code used to generate table 1.

### 📈 Results 

This directory contains the results obtained from the bibliometric analysis. Critically, the true positive sets are located here, as well as the extended csv version of table 1, contained in csv format. 

Please refer to the individual directories and files for more detailed descriptions and instructions.
