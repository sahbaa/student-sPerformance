# Student Performance Analysis

## Project Overview

This project focuses on analyzing and preprocessing a dataset containing information about students' academic performance and related factors. The dataset has been prepared for exploratory data analysis (EDA) and machine learning applications.

## Dataset Description

The dataset contains 10,000 records with the following attributes:

**Hours Studied**: Number of hours a student studied.

**Previous Scores**: Academic scores from prior assessments.

**Extracurricular Activities**: Participation in extracurricular activities (Yes/No).

**Sleep Hours**: Average daily hours of sleep.

**Sample Question Papers Practiced**: Number of sample question papers practiced.

**Performance Index**: A computed score representing the student's overall performance.

## Preprocessing Steps

The dataset underwent several preprocessing steps to ensure it is clean and ready for further analysis:

### Handling Missing Values:

Checked for missing values in all columns.

Since no missing values were found, this step was not required.

### Encoding Categorical Data:

Converted the Extracurricular Activities column from categorical (Yes/No) to binary (1/0).

### Outlier Detection and Removal:

Identified and removed outliers in numerical columns such as Hours Studied and Performance Index using the IQR method.

### Feature Scaling:

Applied Min-Max Scaling to numeric columns to ensure all features are on the same scale for modeling.

### Feature Engineering:

Created a composite feature combining Hours Studied and Sample Question Papers Practiced to represent study effort.

Tools and Libraries

The following tools and Python libraries were used for this project:

### Python: Programming language.

### pandas: Data manipulation and analysis.

### numpy: Numerical computing.

### matplotlib & seaborn: Data visualization.
