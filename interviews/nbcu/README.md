

# People Analytics Case Study
Requisition #: 51501473
<br>

## Problem Statement: 
As a result of The Great Reshuffle, the Company has been hiring new employees at an increasingly fast rate. This continued growth in human capital has prompted the Laptop Allocation team to audit their inventory, ensuring we have enough laptops for new hires. 
The Laptop Allocation team has come to you asking to predict the number of new hires expected for the upcoming year. Thus, allowing them to be prepared and stocked with enough laptops for everyone.
Attached is data received from the reporting team regarding hires, terminations, time to fill/hire positions and headcount information. 

**Hint: Only Voluntary Resignations get replaced by New Hires**



## Instructions:
- Analyze and forecast how many new hires are expected for the upcoming year
- Prepare a brief statement/presentation including:
  - Recommended forecast
  - Method and tools used to forecast the data and why you chose them
  - Any assumptions made
- Send the presentation materials and backup code to NBCUniversal by end of day Sunday
During your second round of interviews, you’ll have 10 minutes to present with 5 minutes for Q&A.

Thank you for in advance for participating in the case study; we look forward to hearing your presentation!

---

## Data Key
<Br>

|Field |Description            |
|------|-----------------------|
|EID   |unique employee id     |
|DATE  | date of record action |
|HIRES | hire flag             |
|TERMINATIONS     |termination flag |
|TERMINATION TYPE	|type of termination|
|YEAR_MONTH	      |year and month concatenated|
|COMPANY HC	      |unique count of employees |
|TIME TO FILL	    |time it took (in days) to fill that employees position|


---
# Results
I created a model to predict the number of Net Hires by month over the next 12 months using [Meta's Prophet](https://facebook.github.io/prophet/docs/quick_start.html#python-api) 

## Steps to Solution:
- Combined each respective dataset using the POS_ID as the unique key
  - Used the POS_ID to retrieve the Fill Time for the Termination
  - Added the Fill Time to the Termination dates to determine hire dates
- Filtered the Termination table for only Voluntary Resignations
- Created a sheet with all dates between 1/1/2014 and 5/31/2023
- Used INDEX/MATCH to retrieve the number of Hires and Terminations for each date
- Subtracted Terminations from Hires to determine Net Hires
- Created a new column using EOMONTH to return the Month respective to the date


---
## Prophet Forecasting:

I used Meta/Facebook's "Prophet" library to forecast Net Hires on both a Daily and Monthly frequency. The daily visualizations were not terribly helpful or easy to digest, but the monthly plot yielded clear results. Prophet uses Linear Regression in its modeling. 


<img width="692" alt="Net Hires Over Time (Month)" src="https://github.com/charter-ab/career/assets/126614453/6dcd9146-74aa-483a-a006-49f992c1cffa">

