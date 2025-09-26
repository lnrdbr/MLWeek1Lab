import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

print(df.head())
df_before = df.copy()

missing_before = df_before.isnull().sum().sort_values(ascending=False)
plt.figure()
missing_before.plot(kind="bar")
plt.title("Missing Values per Column  BEFORE Cleaning")
plt.xlabel("Column")
plt.ylabel("Count of missing")
plt.tight_layout()
plt.show()

print("\nINFO (before)")
df.info()
print("\nMissing counts (before)")
print(df.isnull().sum())

df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

print("\nINFO (after)")
df.info()
print("\nMissing counts (after)")
print(df.isnull().sum())


df.to_csv('titanic_cleaned.csv', index=False)
print("\nSaved: titanic_cleaned.csv")
