# 1202 Final Assignment

## Problem Statment

<b>Using the `survey.csv` dataset perform data analytics operations to answer the following question</b>


```
How does the frequency of mental health illness and attitudes towards mental health vary by geographic location?
```

## Data Preprocessing

<h3>We perform some retrospective inspection of the `survey.csv` dataset and decide to perform some important data preprocessing techniques in order to enhance its quality and make it easier and optimized to perform further operations on it</h3>

* Performing `df.info()` we realise that there are 26 columns where age is numerical and remaining all are categorical.
* `timestamp` is a useless column, since it only indicates the time when the user filled out the survey. Another useless column is `comments`.
```
df = df.drop(['timestamp','comments'], axis = 1)
```
* Some columns are title cased and some are not. We convert all columns to small case so as not to run in any case sensitive errors later.
```
df.columns = df.columns.str.lower()
```
* We also observe that most of the data of the survey originates from either <b>United States</b> and <b>United Kingdom</b>.
```
df['country'].value_counts()
```
* Also, the provinces that are listed are only of <b>United States</b>. Thus in order to conduct a more granular location based analysis a separate analysis on US provinces need to be conducted. This is realised by using the below code.
```
df['state'].unique()
```
<b>Thus for every visualization created for the world countries another analysis on same parameters is conducted for the indivdual provinces of United States.</b>

## Data Analytics

<h2>The visualisations have been created considering both the employee and the employer</h2>

## <u>Employee Specific Analysis</u>

### <u><i>Determining Employees seeking treatment of their mental illness in US</i></u>

### US Province

### World
### <u><i>Determining Employees seeking treatment of their mental illness in World</i></u>

### US Province

### World
### <u><i>Determining Employees knowing options for mental care their employer provides in US</i></u>

### US Province

### World
### <u><i>Determining Employees knowing options for mental care their employer provides in World</i></u>

### US Province

### World
### <u><i>Determining Employees comfortable discussing their mental health with their coworkers in US</i></u>

### US Province

### World
### <u><i>Determining Employees comfortable discussing their mental health with their coworkers in World</i></u>

### US Province

### World
### <u><i>Determining Employees comfortable discussing their mental health with their direct supervisor in US</i></u>

### US Province

### World
### <u><i>Determining Employees comfortable discussing their mental health with their direct supervisor in World</i></u>

### US Province

### World
### <u><i>Determining Employers who put mental health as important as physical health as per employee</i></u>

### US Province

### World
### <u><i>Determining Employers who put mental health as important as physical health as per employee</i></u>

### US Province

### World