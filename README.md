# 1202 Final Assignment

## Problem Statment

<b>Using the `survey.csv` dataset perform data analytics operations to answer the following question</b>


> <h3>How does the frequency of mental health illness and attitudes towards mental health vary by geographic location?</h3>


## Data Preprocessing

<h3>We perform some retrospective inspection of the `survey.csv` dataset and decide to perform some important data preprocessing techniques in order to enhance its quality and make it easier and optimized to perform further operations on it</h3>

* Performing `df.info()` we realise that there are 26 columns where age is numerical and remaining all are categorical.
* `timestamp` is a useless column, since it only indicates the time when the user filled out the survey. Another useless column is `comments`.
```py
df = df.drop(['timestamp','comments'], axis = 1)
```
* Some columns are title cased and some are not. We convert all columns to small case so as not to run in any case sensitive errors later.
```py
df.columns = df.columns.str.lower()
```
* We also observe that most of the data of the survey originates from either <b>United States</b> and <b>United Kingdom</b>.
```py
df['country'].value_counts()
```
* Taking the means out of these counts we conclude that on an average 26 people participated. Thus we will only consider entities whose 26 or more entities participated in the survey for better understandability.
```py
df['country'].value_counts().mean()
```
* Also, the provinces that are listed are only of <b>United States</b>. Thus in order to conduct a more granular location based analysis a separate analysis on US provinces need to be conducted. This is realised by using the below code.
```py
df['state'].unique()
```
<b>Thus for every visualization created for the world countries another analysis on same parameters is conducted for the indivdual provinces of United States.</b>

## Data Analytics

<h2>The visualisations have been created considering both the employee and the employer</h2>

## Employee Specific Analysis

### <i>Determining Employees seeking treatment of their mental illness</i>

### US Province
> From the graph we observe that Illinois (IL) have the most percentage of employees seeking medical treatment with almost 68.97% and Tennessee the least with 40%. 
### World
> From the graph we observe that United States have the most percentage of employees seeking medical treatment with almost 54.59% and Netherlands the least with 33.33%. 
### <i>Determining Employees knowing options for mental care their employer provides</i>

### US Province
> Both Illinois (IL) and Pennsylvania (PA) shows the max percentage of 51.72% where the employee knows about their employer's mental health benefits. The least is shown by Tennessee (TN) 
### World
> Netherlands shows the least percentage (14.81%)of employees knowing about their meantal health care plan in the world. The United States showing the most percentage (41.41%) in this regard).
### <i>Determining Employees comfortable discussing their mental health with their coworkers </i>

### US Province
> Both Oregon (OR) and Ohio (OH) shows the least percentage (almost 10%) of employees open to discussing there mental health with their coworkers.Pennsylvania being the most at 27.59%. However, Illinois (IL) and Tennessee shows the most number (almost 72%) of employees where some aspect of the mental conditions were observed to be discussed amongst employees.
### World
> Ireland has the least percentage (11.11%) of people comfortable of discussing there mental health with their coworkers. The Netherlands being the most at (33.33%). However, Canada and Germany shows the most number (almost 68%) of employees where some aspect of the mental conditions were observed to be discussed amongst employees.
### <i>Determining Employees comfortable discussing their mental health with their direct supervisor</i>

### US Province
> Indiana (IN) shows the most number of employees (66.67%) comfortable discussing their mental health with their direct supervisor. Ohio (OH) being the least at (26%)
### World
> Although most of Netherlands shows the most number of employees (33.33%) who discuss their mental health with their supervisors, Canada has the most number of employees (68.06%) where some aspect of the mental health is discussed.
### <i>Determining Employers who put mental health as important as physical health as per employee</i>

### US Province
> Washington (WA) is the state where most number of employees (35.71%) give their mental health the same importance as their physical health, Ohio being the least at (13.33%).
### World
> Ireland has the least number of employees (14.81%) where employees put their mental health at par with their physical health. However, it is also the country where most of the employees at some level gives the importance to their mental health (44.44%). This is least observed in Canada (26.39%).

## Employer Specific Analysis

### <i>Determining Employers who provides mental health benefits</i>
## US Province
> Washington shows the most number of employees at (62.86%) where the employer provides them with health benefits. The least being Ohio (33.33%).
## World
> Ireland and Germany have the least number of employees having mental health benefits from their employers (almost 11%). The most are in United States at 53%.

### <i>Determining Employers who discuss mental health of their employee as per wellness program</i>
## US Province
> Texas (TX) has the least number of employees where the employer organizes discussion sessions with them at 6.82%, Washington being the most at 40%.
## World
> United States has the most number of employees discussing their mental health with their employers at 22.24%. The least is for Germany and United Kingdom at almost 9%.

### <i>Determining Employers who provides resources to seek help about mental health issues</i>
## US Province
> Texas is at least count when providing help to its employees for mental health issues at 13.64%. The most is Washington at 40%.
## World
> United States provides the most help for mental health issues to its employees at 25.17% through its employers. The least is for Ireland at 11.11%.


### <i>Easiness at which the medical leave can be taken by the employee due to mental state</i>
## US Province
> Washington has the easiest leave policy for mental health at 15.71% and Ohio the least at 3.33%.
## World
> United Kingdom has the easiest leave application policy at 22.7%. The least is for ireland at 3.7%.