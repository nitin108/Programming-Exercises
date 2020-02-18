#!/usr/bin/python3

import QE_App
import unittest



class TestQEApp(unittest.TestCase):

    def setUp(self):
        print("setup")


    @classmethod
    def setUpClass(cls):
        super(TestQEApp,cls).setUpClass()
        cls.fileargcsv = "sampletest_data.csv"
        cls.fileargjson = "sampletest_data.json"
        cls.input_file_csv = open(cls.fileargcsv)
        cls.input_file_json = open(cls.fileargjson)


    @classmethod
    def tearDownClass(cls):
        super(TestQEApp,cls).tearDownClass()

        cls.input_file_csv.close()
        cls.input_file_json.close()


    def test_timestamp(self):
        hour_val = int("-08")
        month = QE_App.convert_timestamp(601605300,hour_val,0)
        self.assertEqual('January',month)

        current_timestamp = 1582058547.2287254
        month = QE_App.convert_timestamp(current_timestamp,-5,0)
        self.assertEqual('February',month)


    def test_csv(self):
        avg_num_siblings,top_three,birthday_months = QE_App.compute_csv(self.input_file_csv)
        self.assertEqual(2,avg_num_siblings)
        self.assertEqual('Meatballs',top_three[0][0])
        self.assertEqual(6,birthday_months['January'])


    def test_json(self):
        avg_num_siblings,top_three,birthday_months = QE_App.compute_json(self.input_file_json)
        self.assertEqual(2,avg_num_siblings)
        self.assertEqual('Meatballs',top_three[0][0])
        self.assertEqual(6,birthday_months['January'])


    def tearDown(self):
        print("cleanup")



if __name__ == '__main__':
    unittest.main()

