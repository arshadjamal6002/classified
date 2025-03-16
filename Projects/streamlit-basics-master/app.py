import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title='Startup Funding Analysis', layout='wide')

# Load data
df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Title and subtitle
st.title("Startup Funding Analysis")
st.subheader("Analyze startup funding trends, investor activities, and industry insights")

# Sidebar navigation
st.sidebar.header("Select Analysis Type")
option = st.sidebar.selectbox('Analysis Type', ['Overall Analysis', 'Startup', 'Investor'])

# Overall Analysis
def load_overall_analysis():
    st.header("Overall Investment Analysis")
    
    # Metrics
    total_funding = round(df['amount'].sum())
    max_funding = df.groupby('startup')['amount'].max().max()
    avg_funding = round(df.groupby('startup')['amount'].sum().mean())
    num_startups = df['startup'].nunique()
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Investment", f"{total_funding} Cr")
    col2.metric("Max Investment", f"{max_funding} Cr")
    col3.metric("Avg Investment", f"{avg_funding} Cr")
    col4.metric("Funded Startups", num_startups)
    
    # Month-over-Month Analysis
    st.subheader("Month-over-Month Investment Analysis")
    selected_option = st.selectbox('Select Analysis Type', ['Total Investment', 'Investment Count'])
    
    if selected_option == 'Total Investment':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
    
    temp_df['x_axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(temp_df['x_axis'], temp_df['amount'], marker='o', color='b')
    ax.set_title('MoM Investment Analysis')
    ax.set_xlabel('Month-Year')
    ax.set_ylabel('Amount' if selected_option == 'Total Investment' else 'Investment Count')
    ax.tick_params(axis='x', rotation=45)
    
    st.pyplot(fig)

    col1, col2 = st.columns(2)

    with col1:
        # Sectors Invested
        vertical_investments = df.groupby('vertical')['amount'].sum().sort_values(ascending = False).head(10)
        st.subheader("Sector-Wise Investment Distribution")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        ax2.pie(vertical_investments, labels=vertical_investments.index, autopct="%0.01f%%", startangle=90)
        ax2.axis('equal')
        st.pyplot(fig2)

    with col2:
        # Sectors Invested
        round_investments = df.groupby('round')['amount'].sum().sort_values(ascending = False).head(10)
        st.subheader("Round-Wise Investment Distribution")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        ax2.pie(round_investments, labels=round_investments.index, autopct="%0.01f%%", startangle=90)
        ax2.axis('equal')
        st.pyplot(fig2)    

    with col1:
        # Sectors Invested
        city_investments = df.groupby('city')['amount'].sum().sort_values(ascending = False).head(10)
        st.subheader("City-Wise Investment Distribution")
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        ax1.bar(city_investments.index, city_investments.values, color='orange')
        ax1.set_title(f'City Wise')
        ax1.set_xlabel('Cities')
        ax1.set_ylabel('Investment Amount')
        st.pyplot(fig1)   
        

# Investor Analysis
def load_investor_details(investor):
    st.header(f"Investment Analysis: {investor}")
    
    # Most recent investments
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader("Most Recent Investments")
    st.table(last5_df)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Biggest Investments
        big_investments = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)
        st.subheader("Top 5 Investments")
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        ax1.bar(big_investments.index, big_investments.values, color='orange')
        ax1.set_title(f'Biggest Investments by {investor}')
        ax1.set_xlabel('Startup')
        ax1.set_ylabel('Investment Amount')
        st.pyplot(fig1)
    
    with col2:
        # Sectors Invested
        vertical_investments = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader("Sector-Wise Investment Distribution")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        ax2.pie(vertical_investments, labels=vertical_investments.index, autopct="%0.01f%%", startangle=90)
        ax2.axis('equal')
        st.pyplot(fig2)

    col3, col4 = st.columns(2)

    with col3:         
    
        # Year-over-Year Investment
        st.subheader("Year-over-Year Investment")
        year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
        fig3, ax3 = plt.subplots(figsize=(8, 5))
        ax3.plot(year_series.index, year_series.values, marker='o', color='g')
        ax3.set_title(f'YoY Investment by {investor}')
        ax3.set_xlabel('Year')
        ax3.set_ylabel('Total Investment Amount')
        st.pyplot(fig3)

    with col4:

        st.subheader("Similar Investors")
        st.subheader("Use Knn here")

# Sidebar selections
if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'Startup':
    selected_startup = st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    if st.sidebar.button('Show Startup Details'):
        st.header(f"Startup Analysis: {selected_startup}")
        startup_data = df[df['startup'] == selected_startup][['date', 'investors', 'amount', 'round', 'city', 'vertical']]
        st.table(startup_data)

elif option == 'Investor':
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    if st.sidebar.button('Show Investor Details'):
        load_investor_details(selected_investor)

# Footer
st.markdown("---")
st.write("Created by Arshad Jamal | [GitHub](https://github.com/arshadjamal6002)")
