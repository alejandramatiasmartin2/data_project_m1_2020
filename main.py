import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre


def argument_parser():
    parser = argparse.ArgumentParser(description='indicate country...')
    parser.add_argument("-c", "--country", help="Select a specific country or all countries", default="all countries", type=str, required=True)
    args = parser.parse_args()

    return args


def main(arguments):

    print('starting pipeline...')
    data_base = mac.get_data()
    unique_jobs = mac.get_jobs_id(data_base)
    jobs_api = mac.get_jobs_api(data_base, unique_jobs)
    gender_c_cleaned = mwr.clean_gender(jobs_api)
    quantity_addition = man.get_quantity(gender_c_cleaned)
    data_merged = man.get_percentage(quantity_addition)
    countries_df = mac.get_country_codes(data_merged)
    final_data_merged = man.merged_final_data(data_merged, countries_df)
    exported = mre.export(final_data_merged, country_selection)
    print('pipeline is complete!')


if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)