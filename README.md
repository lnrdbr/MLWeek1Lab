# COM624 Machine Learning Lab Week 1 - Project Summary

## Overview
This project demonstrates data cleaning and preprocessing techniques using the Titanic dataset as part of COM624 Level 6 Software Engineering coursework. The focus is on preparing raw data for machine learning analysis through systematic cleaning procedures.

## Project Structure
```
MLWeek1/
├── script.py                    # Main data cleaning script
├── titanic_cleaned.csv          # Processed dataset output
├── COM624 MACHINE LEARNIG LAB WEEK 1.docx  # Lab instructions
└── PROJECT_SUMMARY.md           # This summary document
```

## Dataset Information
- **Source**: Titanic dataset from GitHub (datasciencedojo repository)
- **Original URL**: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- **Purpose**: Educational dataset for learning data cleaning techniques
- **Domain**: Historical passenger data from RMS Titanic

## Data Cleaning Process

### 1. Initial Data Exploration
- Loaded dataset using pandas from remote GitHub URL
- Examined data structure using `df.info()` and `df.head()`
- Identified missing values using `df.isnull().sum()`
- Created visualization of missing data before cleaning

### 2. Column Removal (`script.py:23`)
**Columns Dropped**: `PassengerId`, `Name`, `Ticket`, `Cabin`

**Rationale**:
- **PassengerId**: Arbitrary identifier with no predictive value
- **Name**: Individual names don't contribute to survival patterns
- **Ticket**: Ticket numbers are unique identifiers without analytical value
- **Cabin**: High percentage of missing values (>70%) making imputation unreliable

### 3. Missing Value Treatment

#### Age Column (`script.py:25`)
- **Method**: Median imputation
- **Rationale**: Age had moderate missing values (~20%); median is robust to outliers and maintains realistic age distribution
- **Alternative considered**: Mean imputation (rejected due to age distribution skewness)

#### Embarked Column (`script.py:26`)
- **Method**: Mode imputation (most frequent value)
- **Rationale**: Only 2 missing values; mode represents most common embarkation port
- **Result**: Missing values filled with 'S' (Southampton - most common port)

### 4. Categorical Encoding

#### Sex Variable (`script.py:28`)
- **Method**: Binary mapping (male=0, female=1)
- **Rationale**: Simple binary variable best handled with manual mapping for clarity

#### Embarked Variable (`script.py:29`)
- **Method**: One-hot encoding with `pd.get_dummies()`
- **Configuration**: `drop_first=True` to avoid multicollinearity
- **Result**: Created `Embarked_Q` and `Embarked_S` boolean columns

## Final Dataset Characteristics
- **Dimensions**: 891 rows × 9 columns (reduced from 12 original columns)
- **Missing Values**: 0 (all missing data handled)
- **Data Types**: All numeric (ready for ML algorithms)
- **Output File**: `titanic_cleaned.csv`

## Extension Task Implementation

### Visualization Component
The script includes matplotlib visualization to show missing values before cleaning:
- Bar chart displaying missing value counts per column
- Visual comparison tool for before/after cleaning assessment
- Helps demonstrate the impact of cleaning decisions

### Cleaning Decision Analysis

#### Strategic Decisions Made:

1. **Conservative Approach**: Chose imputation over deletion to preserve sample size
2. **Domain Knowledge**: Recognized that demographic variables (Age, Sex, Embarked) are important for survival analysis
3. **Statistical Soundness**: Used median for Age (skewed distribution) and mode for Embarked (categorical)
4. **ML Preparation**: Ensured all variables are numeric and properly encoded

#### Alternative Approaches Considered:

1. **Age Imputation**: Could have used regression imputation based on other variables, but median provides good balance of simplicity and accuracy
2. **Cabin Handling**: Could have extracted deck information from partial cabin data, but high missing percentage (>70%) made this unreliable
3. **Feature Engineering**: Could have created new features (e.g., family size from SibSp + Parch), but focused on core cleaning for this lab

## Learning Outcomes Achieved

✅ **Understanding Data Cleaning Importance**: Demonstrated how raw data requires systematic preprocessing

✅ **Python Techniques Applied**: Utilized pandas for missing value detection, imputation, and encoding

✅ **Dataset Preparation**: Successfully transformed raw data into ML-ready format

## Technical Implementation

### Key Libraries Used:
- `pandas`: Data manipulation and analysis
- `matplotlib.pyplot`: Data visualization

### Code Quality Features:
- Clear variable naming and comments
- Proper use of `inplace=True` for memory efficiency
- Systematic approach to data transformation
- Output validation with info() and missing value checks

## Repository Information
- **GitHub Repository**: [Your GitHub URL here]
- **Visibility**: Public (as requested in lab instructions)
- **Contents**: Complete source code, cleaned dataset, and documentation

## Future Applications
The cleaned dataset is now ready for:
- Exploratory Data Analysis (EDA)
- Machine Learning model training (survival prediction)
- Statistical analysis and hypothesis testing
- Advanced feature engineering

---
*This project summary demonstrates comprehensive data cleaning methodology and serves as documentation for the COM624 Machine Learning Lab Week 1 assignment.*