USE bodyfat_project;

SELECT* FROM bodyfat_data;

SELECT AVG(age) AS AverageAge FROM bodyfat;

SELECT MIN(BodyFat) as MinBodyFat, MAX(BodyFat) AS MaxBodyFat FROM bodyfat;

ALTER TABLE bodyfat_data
ADD COLUMN weight_kg DECIMAL(10, 2) 
GENERATED ALWAYS AS (round((weight/2.2),2)) STORED;

SELECT height,round((height*2.54)/100,2) AS height_m
FROM bodyfat_data;

ALTER TABLE bodyfat_data
ADD COLUMN height_m DECIMAL(10, 2) 
GENERATED ALWAYS AS (round((height*2.54)/100,2)) STORED;

SELECT* FROM bodyfat_data;

# Now lets calculate the body mass index based on weight_kg and height_kg and create a new column called BMI.

SELECT ROUND(weight_kg / (height_m * height_m),2) AS BMI
FROM bodyfat_data;

ALTER TABLE bodyfat_data
ADD COLUMN BMI DECIMAL(10, 2) 
GENERATED ALWAYS AS (round(weight_kg / (height_m * height_m),2)) STORED;

select* from bodyfat_data;

# Now lets create a new column called obesity_cat to show the category of each individual.
# If your BMI is less than 18.5, it falls within the underweight range.
# If your BMI is 18.5 to <25, it falls within the healthy weight range.
# If your BMI is 25.0 to <30, it falls within the overweight range.
# If your BMI is 30.0 or higher, it falls within the obesity range.Obesity is frequently subdivided into categories:
# Class 1: BMI of 30 to < 35
# Class 2: BMI of 35 to < 40
# Class 3: BMI of 40 or higher.

ALTER TABLE bodyfat_data
ADD COLUMN obesity_cat VARCHAR(50);

SET SQL_SAFE_UPDATES = 0;

UPDATE bodyfat_data
SET obesity_cat = 
    CASE
        WHEN BMI < 18.5 THEN 'UW'
		WHEN BMI >= 18.5 AND BMI < 24.99 THEN 'HW'
        WHEN BMI >= 25 AND BMI < 29.99 THEN 'OW'
        WHEN BMI >= 30 AND BMI < 34.99 THEN 'OC1'
        WHEN BMI >= 35 AND BMI < 39.99 THEN 'OC2'
        ELSE 'OC3'
    END;

SELECT* FROM bodyfat_data; # All good. Now lets play around and find out how big is each category.

# Let's find out how many underweight people we have in the dataset.
SELECT* 
FROM bodyfat_data
WHERE obesity_cat='UW'
ORDER BY BMI ASC; 

SELECT* 
FROM bodyfat_data
WHERE obesity_cat='HW'
ORDER BY BMI ASC;

SELECT* 
FROM bodyfat_data
WHERE obesity_cat='OW'
ORDER BY BMI ASC;

SELECT* 
FROM bodyfat_data
WHERE obesity_cat='OC1'
ORDER BY BMI ASC;

SELECT* 
FROM bodyfat_data
WHERE obesity_cat='OC2'
ORDER BY BMI ASC;

SELECT* 
FROM bodyfat_data
WHERE obesity_cat='OC3'
ORDER BY BMI ASC;

