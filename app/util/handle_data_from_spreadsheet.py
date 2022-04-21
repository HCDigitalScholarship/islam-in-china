import pandas as pd
from pathlib import Path
from csv import writer


def get_data_from_csv(write_file=False):  # whether we want to write new files to disk or not
    manu_data_dir = Path.cwd() / 'data' / 'spreadsheet' / 'pilot.xlsx'

    # checking if the manuscript csv is available
    if (manu_data_dir.is_file()):
        manu_df = pd.read_excel(manu_data_dir, na_values=['Unidentified', 'N/A'], skip_blank_lines=True)
        manu_df.dropna(how="all", inplace=True)  # drop all empty lines
    else:
        raise FileNotFoundError("Manuscript file is missing")

    # renaming columns
    manu_df.columns = ['id', 'arab_title_script', 'arab_title', 'chinese_title', 'author', 'assembler', 'editor',
                       'scrivener', 'translator', 'type', 'place', 'publisher', 'year', 'stand_year', 'language',
                       'num_pages', 'description', 'notes']

    if write_file:
        # export each manuscript to an individual json file
        for i in manu_df.index:
            # the file is saved by their project ID
            ind_manu_dir = Path.cwd() / 'data' / 'metadata' / '{}.json'.format(manu_df.loc[i].id)
            manu_df.loc[i].to_json(ind_manu_dir)

    return len(manu_df.index)


def write_data_to_csv(new_row):
    manu_data_dir = Path.cwd() / 'data' / 'csv' / 'pilot_manuscript.csv'

    with open(manu_data_dir, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(new_row)


if __name__ == "__main__":
    get_data_from_csv(write_file=True)