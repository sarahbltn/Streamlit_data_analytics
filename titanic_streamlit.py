import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Titanic Analysis')
st.text('Sarah Beltran')

st.header('Dataset', divider='gray')

df = pd.read_csv('C:/Users/sarah/apps/Data-Analysis/src/streamlit/titanic.csv')
df.columns = ['passenger_id', 'survived', 'class', 'name', 'sex', 'age', 'sib_spouses', 'parents_children', 'ticket', 'fare', 'cabin', 'embarked']
st.dataframe(df)
print('\n')

st.header('Survivors Histogram', divider='gray')

survived_group = df.groupby('survived')
fig, ax = plt.subplots(figsize = (6, 4) )
for i, survived_group in survived_group:
    ax.hist(survived_group['survived'], alpha = 0.5, bins = 2, label = str(i))
ax.set_title('Survivors', fontname = 'Times New Roman', fontsize = 15)
ax.set_xlabel('0: Did not survived & 1: Survived', fontname = 'Times New Roman', fontsize = 12 )
ax.legend()
st.pyplot(fig)
st.markdown('Histogram discovery')
st.markdown('About of 350 people survived the titanic, this is around 39.3%.')

st.header('Class Histogram', divider='gray')

class_group = df.groupby('class')
fig, ax = plt.subplots(figsize = (6, 4) )
for x, class_group in class_group:
    ax.hist(class_group['class'], alpha = 0.5, bins = 2, label = str(x))
ax.set_title('Ticket Class', fontname = 'Times New Roman', fontsize = 15)
ax.set_xlabel('1: First class, 2: Second class & 3: Third class', fontname = 'Times New Roman', fontsize = 12 )
ax.legend()
st.pyplot(fig)
st.markdown('Histogram discovery')
st.markdown('The 3rd class tickets was most of the population boarding the titanic.')

st.header('Sex Histogram', divider='gray')

sex_group = df.groupby('sex')
fig, ax = plt.subplots(figsize = (6, 4) )
for y, sex_group in sex_group:
    ax.hist(sex_group['sex'], alpha = 0.5, bins = 2, label = str(y))
ax.set_title('Sex', fontname = 'Times New Roman', fontsize = 15)
ax.legend()
st.pyplot(fig)
st.markdown('Histogram discovery')
st.markdown('There was almost as twice the male population than the female.')

st.header('Age Histogram', divider='gray')

# age_group = df.groupby('age')
# fig, ax = plt.subplots(figsize = (6, 4) )
# for a, age_group in age_group:
#     ax.hist(age_group['age'], alpha = 0.5, bins = 2, label = str(a))
# ax.set_title('Age', fontname = 'Times New Roman', fontsize = 15)
# ax.legend()
# st.pyplot(fig)

fig, ax = plt.subplots()
df['age'].plot(kind='hist', ax=ax)
plt.xlabel('Age')
plt.ylabel('# of people')
plt.title('Age histogram')
st.pyplot(fig)
st.markdown('Histogram discovery')
st.markdown('Theres way more people around 20-30 years old, and theres almost none 80 years old people.')

st.header('Parents/children Histogram', divider='gray')

pc_group = df.groupby('parents_children')
fig, ax = plt.subplots(figsize = (6, 4) )
for j, pc_group in pc_group:
    ax.hist(pc_group['parents_children'], alpha = 0.5, bins = 2, label = str(j))
ax.set_title('Parents & children', fontname = 'Times New Roman', fontsize = 15)
ax.legend()
st.pyplot(fig)
st.markdown('Histogram discovery')
st.markdown('Almost 77% of the population have no children.Theres way more people around 20-30 years old, and theres almost none 80 years old people.')

st.header('Siblings/spouses Histogram', divider='gray')

ss_group = df.groupby('sib_spouses')
fig, ax = plt.subplots(figsize = (6, 4) )
for s, ss_group in ss_group:
    ax.hist(ss_group['sib_spouses'], alpha = 0.5, bins = 2, label = str(s))
ax.set_title('Siblings & spouses', fontname = 'Times New Roman', fontsize = 15)
ax.legend()
st.pyplot(fig)
st.markdown('Histogram discovery')
st.markdown('Around 67.4% of the population had no spouses or siblings.')

st.header('Embarked', divider='gray')

embarked_group = df.groupby('embarked')
fig, ax = plt.subplots(figsize = (6, 4) )
for e, embarked_group in embarked_group:
    ax.hist(embarked_group['embarked'], alpha = 0.5, bins = 2, label = str(e))
ax.set_title('Embarked', fontname = 'Times New Roman', fontsize = 15)
ax.set_xlabel('C: Cherbourg, Q: Queenstown & S: Southampton', fontname = 'Times New Roman', fontsize = 12 )
ax.legend()
st.pyplot(fig)
st.markdown('Histogram discovery')
st.markdown('The southhampton port was where most people boarded.')

st.header('Survived-sex', divider='gray')

survived_gender = df.groupby(['survived', 'sex']).size().unstack()
fig, ax = plt.subplots()
survived_gender.plot(kind='bar', stacked=True, color=['pink', 'skyblue'], ax=ax)
plt.xlabel('Survived')
plt.ylabel('# of people')
plt.title('Survival Count by Gender')
st.pyplot(fig)
st.markdown('Histogram discovery')
st.markdown('There were more woman survivors than men')
