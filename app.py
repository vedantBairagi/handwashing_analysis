import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

plt.style.use('seaborn')

st.markdown('''
## 1. Meet Dr. Ignaz Semmelweis
<p><img style="float: left;margin:5px 20px 5px 1px" src="https://assets.datacamp.com/production/project_20/img/ignaz_semmelweis_1860.jpeg"></p>
<!--
<img style="float: left;margin:5px 20px 5px 1px" src="/home/vedant/Academics/datasets/ignaz_semmelweis_1860.jpeg">
-->
<p>This is Dr. Ignaz Semmelweis, a Hungarian physician born in 1818 and active at the Vienna General Hospital. If Dr. Semmelweis looks troubled it's probably because he's thinking about <em>childbed fever</em>: A deadly disease affecting women that just have given birth. He is thinking about it because in the early 1840s at the Vienna General Hospital as many as 10% of the women giving birth die from it. He is thinking about it because he knows the cause of childbed fever: It's the contaminated hands of the doctors delivering the babies. And they won't listen to him and <em>wash their hands</em>!</p>
<p>Here I have reanalyzed the data that made Semmelweis discover the importance of <em>handwashing</em>. Let's start by looking at the data that made Semmelweis realize that something was wrong with the procedures at Vienna General Hospital.</p>
''', unsafe_allow_html=True
)

yearly = pd.read_csv('datasets/yearly_deaths_by_clinic.csv')

st.dataframe(yearly)

st.markdown('''
## 2. The alarming number of deaths
<p>The table above shows the number of women giving birth at the two clinics at the Vienna General Hospital for the years 1841 to 1846. You'll notice that giving birth was very dangerous; an <em>alarming</em> number of women died as the result of childbirth, most of them from childbed fever.</p>
<p>We see this more clearly if we look at the <em>proportion of deaths</em> out of the number of women giving birth. Let's zoom in on the proportion of deaths at Clinic 1.</p>
''', unsafe_allow_html=True)

yearly['proportion_deaths'] = yearly['deaths'] / yearly.births
clinic_1 = yearly[yearly.clinic == 'clinic 1']
clinic_2 = yearly[yearly['clinic'] == 'clinic 2']

st.dataframe(clinic_1)

st.markdown('''
## 3. Death at the clinics
<p>If we now plot the proportion of deaths at both Clinic 1 and Clinic 2  we'll see a curious pattern…</p>
''', unsafe_allow_html=True)

fig, ax = plt.subplots()
ax.plot(clinic_1.year, clinic_1.proportion_deaths)
ax.plot(clinic_2.year, clinic_2.proportion_deaths)
ax.set_xlabel('Year')
ax.set_ylabel('Proportion of Deaths')
ax.legend(['Clinic 1', 'Clinic 2'])

st.pyplot(fig)

st.markdown('''
## 4. The handwashing begins
<p>Why is the proportion of deaths consistently so much higher in Clinic 1? Semmelweis saw the same pattern and was puzzled and distressed. The only difference between the clinics was that many medical students served at Clinic 1, while mostly midwife students served at Clinic 2. While the midwives only tended to the women giving birth, the medical students also spent time in the autopsy rooms examining corpses. </p>
<p>Semmelweis started to suspect that something on the corpses spread from the hands of the medical students, caused childbed fever. So in a desperate attempt to stop the high mortality rates, he decreed: <em>Wash your hands!</em> This was an unorthodox and controversial request, nobody in Vienna knew about bacteria at this point in time. </p>
<p>Let's load in monthly data from Clinic 1 to see if the handwashing had any effect.</p>
''', unsafe_allow_html=True)

monthly = pd.read_csv('datasets/monthly_deaths.csv', parse_dates=['date'])

monthly['proportion_deaths'] = monthly.deaths / monthly.births

st.dataframe(monthly)

st.markdown('''
## 5. The effect of handwashing
<p>With the data loaded we can now look at the proportion of deaths over time. In the plot below we haven't marked where obligatory handwashing started, but it reduced the proportion of deaths to such a degree that you should be able to spot it!</p>
''', unsafe_allow_html=True)
fig1, ax1 = plt.subplots()
ax1.plot(monthly.date, monthly.proportion_deaths)
ax1.set_xlabel('Date')
ax1.set_ylabel('Proportion of Deaths')
st.pyplot(fig1)

st.markdown('''
## 6. The effect of handwashing highlighted
<p>Starting from the summer of 1847 the proportion of deaths is drastically reduced and, yes, this was when Semmelweis made handwashing obligatory. </p>
<p>The effect of handwashing is made even more clear if we highlight this in the graph.</p>
''', unsafe_allow_html=True)
# Date when handwashing was made mandatory
handwashing_start = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
before_washing = monthly[monthly['date'] < handwashing_start]
after_washing = monthly[monthly['date'] >= handwashing_start]

fig2, ax2 = plt.subplots()
ax2.plot(before_washing.date, before_washing.proportion_deaths)
ax2.plot(after_washing.date, after_washing.proportion_deaths)
ax2.set_xlabel('Date')
ax2.set_ylabel('Proportion of Deaths')
ax2.legend(['Before Washing', 'After Washing'])
st.pyplot(fig2)

