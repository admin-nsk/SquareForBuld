#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
from models import db
from logger_config import get_logger

log = get_logger('import_logger')
log.setLevel('DEBUG')


class ImportFile:

    def __init__(self, input_file, table_name):
        """python 3.9
        Class for split one file to many
        :param input_file: File for import to DB
        """
        self.input_file = input_file
        self.all_data_frame = pd.DataFrame()
        self.column_names = ''
        self.sheet_names = ''
        self.table_name = table_name

    def check_extension(self):
        log.debug('check_extension')
        _file_extension = os.path.splitext(self.input_file)[1]
        if _file_extension == '.xls' or _file_extension == '.xlsx':
            self.import_xls(self.input_file)
        elif _file_extension == '.csv':
            self.import_csv(self.input_file)
        else:
            log.error('Wrong file extension')
            raise TypeError('Wrong file extension')

    def import_xls(self, file):
        try:
            log.debug('Try read xls')
            self.all_data_frame = pd.read_excel(file, encoding='cp1251')
            print(self.all_data_frame)
            log.debug('write to db')
            self.all_data_frame.to_sql(self.table_name, db, if_exists='append', index=False)
        except Exception as ex:
            log.debug(f'Don\'t import file: {ex}')
            return 'Don\'t import file'

    def import_csv(self, file):
        try:
            log.debug('Try read csv')
            self.all_data_frame = pd.read_csv(self.input_file, encoding='cp1251', delimiter=";")
            print(self.all_data_frame)
            log.debug('write to db')
            self.all_data_frame.to_sql(self.table_name, db, if_exists='append', index=False)
        except Exception as ex:
            log.debug(f'Don\'t import file: {ex}')
            return 'Don\'t read file'

    def run(self):
        log.debug('Run')
        print('run')
        self.check_extension()


path = 'input_files/vtor_case2.csv'

if __name__ == '__main__':
    write_to_db = ImportFile(path, 'flats')
    write_to_db.run()

