1. App created using Streamlit (as st)
   

2. Analysis done using Jupyter

"""nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title('Participating Nations Over Years')
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df,'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title('Events over the years')
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Edition", y="Name")
    st.title('Athletes over time')
    st.plotly_chart(fig)


    st.title("No. of Events over time(every sport)")
    fig,ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax= sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a Sport',sport_list)
    x= helper.most_successful(df,selected_sport)
    st.table(x)"""


 st.title("Top 10 athletes of "+ selected_country)
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top10_df)


