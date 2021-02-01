def merged_final_data(data_merged, countries_df):
    data_list2 = [data_merged, countries_df]
    data_merged = reduce(lambda left, right: pd.merge(left, right, on='country_code'), data_list2)
    column_order = ['Country', 'Job Title', 'Gender', 'Quantity', 'Percentage']