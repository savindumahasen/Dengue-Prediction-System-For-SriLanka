
## Import the dataset

dengue_data <- read.csv("DataSet.csv")
dengue_data

View(dengue_data)
## print the first five records
head(dengue_data)


## check the data types
str(dengue_data)

## attach the data set with environment
attach(dengue_data)

## view the dataset
View(dengue_data)


## noramlity testing
## install the nortest package
install.packages("nortest")
## call the library
library("nortest")

## anderson darling testing for prognosis
ad.test(prognosis)
## lillifor testing forprognosis
lillie.test(prognosis)
## shapiro-wiki testing 
shapiro.test(prognosis)

## anderson darling testing for skin rash
ad.test(skin_rash)
## lillifor testing for skin rash
lillie.test(prognosis)
## shapiro wiki testing for skin rash
shapiro.test(prognosis)

## anderson darling testing for High fever
ad.test(high_fever)
## lillifor testing for High fever
lillie.test(high_fever)
## shapiro wiki testing for High fever
shapiro.test(high_fever)

## anderson darling testing for Headache
ad.test(headache)
## lillifor testing for Headache
lillie.test(headache)
## shapiro wiki testing for Headache
shapiro.test(headache)



## anderson darling testing for Nausea
ad.test(nausea)
## lillifor testing for Nausea
lillie.test(nausea)
## shapiro wiki testing for Nausea
shapiro.test(nausea)

# "loss_of_appetite", "pain_behind_the_eyes", "back_pain", "malaise", 
#"muscle_pain", "red_spots_over_body"]]

## anderson darling testing for loss_of_appetite
ad.test(loss_of_appetite)
## lillifor testing for loss_of_appetite
lillie.test(loss_of_appetite)
## shapiro wiki testing for loss_of_appetite
shapiro.test(loss_of_appetite)


## anderson darling testing for pain_behind_the_eyes
ad.test(pain_behind_the_eyes)
## lillifor testing for pain_behind_the_eyes
lillie.test(pain_behind_the_eyes)
## shapiro wiki testing for pain_behind_the_eyes
shapiro.test(pain_behind_the_eyes)


## anderson darling testing for back_pain
ad.test(back_pain)
## lillifor testing for back_pain
lillie.test(back_pain)
## shapiro wiki testing back_pain
shapiro.test(back_pain)

## anderson darling testing for malaise
ad.test(malaise)
## lillifor testing for malaise
lillie.test(malaise)
## shapiro wiki testing malaise
shapiro.test(malaise)

## anderson darling testing for muscle_pain
ad.test(muscle_pain)
## lillifor testing for muscle_pain
lillie.test(muscle_pain)
## shapiro wiki testing muscle_pain
shapiro.test(muscle_pain)



## anderson darling testing for red_spots_over_body
ad.test(red_spots_over_body)
## lillifor testing for red_spots_over_body
lillie.test(red_spots_over_body)
## shapiro wiki testing red_spots_over_body
shapiro.test(red_spots_over_body)

