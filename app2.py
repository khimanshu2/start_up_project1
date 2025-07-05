import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
df = pd.read_csv("startup_clean.csv")
df["amount"]=df["amount"].abs()
df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year


st.sidebar.title("start funding analysis")
option=st.sidebar.selectbox("select one",["overall analysis",'startup','investor'])

def load_overall_detail():
    st.title("overall analysis")
    col1,col2,col3,col4=st.columns(4)
    with col1:
        total = round(df["amount"].sum())
        st.metric("total" ,str(total)+"cr")
    with col2:
        max = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
        st.metric("Max", str(max) + "cr")
    with col3:
        avg = round(df["amount"].mean())
        st.metric("avg", str(avg) + "cr")
    with col4:
        count=df.groupby('startup')['amount'].count().sum()
        st.metric('count',str(count))


    st.header('Month on Month Graph')
    selectd_option =st.selectbox('select type',["total",'count'])
    if selectd_option=='total':
        tdf = df.groupby(['year', 'month'])["amount"].sum().reset_index()
        tdf['tdfx'] = tdf['month'].astype('str') + '-' + tdf['year'].astype('str')
        fig7, ax7 = plt.subplots()
        ax7.plot(tdf['tdfx'], tdf['amount'])
        st.pyplot(fig7)

    else:
        tdf = df.groupby(['year', 'month'])["amount"].count().reset_index()
        tdf['tdfx'] = tdf['month'].astype('str') + '-' + tdf['year'].astype('str')
        fig7, ax7 = plt.subplots()
        ax7.plot(tdf['tdfx'], tdf['amount'])
        st.pyplot(fig7)
    # Sector Analysis Pie -> top sectors(Count + Sum)

    st.header('Sector Analysis')
    selectd_option2=st.selectbox("sector analysis type",["total",'count'])
    if selectd_option2=='total':
        tdf2 = df.groupby("vertical")["amount"].sum().sort_values(ascending=False).head(5)
        fig9, ax9 = plt.subplots()
        ax9.pie(tdf2.values, labels=tdf2.index, autopct='%1.1f%%')
        st.pyplot(fig9)
    else:
        tdf2 = df.groupby("vertical")["amount"].count().sort_values(ascending=False).head(5)
        fig9, ax9 = plt.subplots()
        ax9.pie(tdf2.values, labels=tdf2.index, autopct='%1.1f%%')
        st.pyplot(fig9)
    # types of funding



#load the recent 5 investment of investor

def load_investor_detail(investor):
    st.title(investor)
    last5_df=df[df["investor"].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader("most resent investment")
    st.dataframe(last5_df)

    col1,col2=st.columns(2)
    with col1:
        big_df = df[df["investor"].str.contains(investor)].groupby("startup")["amount"].sum().sort_values(
            ascending=False).head(5)
        st.subheader("Biggest investment")
        fig, ax = plt.subplots()
        ax.bar(big_df.index, big_df.values)
        st.pyplot(fig)
    with col2:
        vertical_ser=df[df["investor"].str.contains(investor)].groupby("vertical")["amount"].sum().sort_values(ascending=False).head(5)
        st.subheader("sector wise investment")
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_ser.values, labels=vertical_ser.index, autopct='%1.1f%%')
        st.pyplot(fig1)
    col3, col4 = st.columns(2)
    with col3:
        round_ser=df[df["investor"].str.contains(investor)].groupby("round")["amount"].sum().sort_values(ascending=False).head(5)
        st.subheader("round wise investment")
        fig2, ax2 = plt.subplots()
        ax2.pie(round_ser.values, labels=round_ser.index, autopct='%1.1f%%')
        st.pyplot(fig2)
    with col4:
        city_ser = df[df["investor"].str.contains(investor)].groupby("city")["amount"].sum().sort_values(
            ascending=False).head(5)
        st.subheader("city wise investment")
        fig3, ax3 = plt.subplots()
        ax3.pie(city_ser.values, labels=city_ser.index, autopct='%1.1f%%')
        st.pyplot(fig3)

    year_series = df[df['investor'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('YoY Investment')
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index, year_series.values)

    st.pyplot(fig4)














if option=='overall analysis':
    load_overall_detail()



elif option=='startup':
    st.sidebar.selectbox("select startup",df["startup"].unique().tolist())
    btn1=st.sidebar.button('find startup list')
    st.title("startup analysis")
else:
    select_investor =st.sidebar.selectbox("select investor", sorted(set(df["investor"].str.split(",").sum())))
    btn2 = st.sidebar.button('find investor list')
    if btn2:
        load_investor_detail(select_investor)


