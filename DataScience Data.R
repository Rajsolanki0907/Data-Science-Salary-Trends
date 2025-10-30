#load libraries
library(ggplot2)

library(tidyverse)
library(lubridate)
library(readxl)
library(gridExtra)
library(magrittr)
library(scales)
library(summarytools)
library(plotrix)
library(RColorBrewer)
library(dplyr)
library(lattice)


DataScience_salaries_2024 <- read_csv("C:/Users/rajso/OneDrive/Desktop/archive/DataScience_salaries_2024.csv")
#View data in table
View(DataScience_salaries_2024)

# Inspect the data
head(DataScience_salaries_2024)
summary(DataScience_salaries_2024)
str(DataScience_salaries_2024)

# Summary statistics
summary(DataScience_salaries_2024)

#explore for missing variable or duplicated inputs
# count total missing values
mis <- sum(is.na(DataScience_salaries_2024))
print(paste("Count of total missing values is", mis))

#count total duplicate observation
dup <- sum(duplicated(DataScience_salaries_2024))
print(paste("Count of total duplicate observation is", dup))

#explore summary of each column
names(DataScience_salaries_2024)

#creating hiatogram using single attribute
histogram(~salary,data = DataScience_salaries_2024)
histogram(~salary_in_usd,data = DataScience_salaries_2024)
histogram(~remote_ratio,data = DataScience_salaries_2024)

#histogram using two attributes
histogram(salary~salary_in_usd,data = DataScience_salaries_2024)

#box plot
bwplot(~salary,data=DataScience_salaries_2024)

#Scatter plot
xyplot(salary~salary_in_usd,data=DataScience_salaries_2024)
bwplot(~salary   | remote_ratio ,data =DataScience_salaries_2024)
xyplot(salary~salary_in_usd | remote_ratio,data=DataScience_salaries_2024)
barchart(~salary,data = DataScience_salaries_2024)
barchart(salary~salary_in_usd,data = DataScience_salaries_2024)
densityplot(~salary,data=DataScience_salaries_2024)

#ggplot
ggplot(data = DataScience_salaries_2024,
       mapping = aes( x = salary ,
                      y = salary_in_usd))



