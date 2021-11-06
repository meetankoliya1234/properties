import statistics
import pandas as pd
import csv

df = pd.read_csv('C:/Users/Meet Ankoliya/Python/project-13/StudentsPerformance.csv')

WriteScore_list = df["writing score"].to_list()

ws_mean = statistics.mean(WriteScore_list)
ws_median = statistics.median(WriteScore_list)
ws_mode = statistics.mode(WriteScore_list)

print("Mean, Median and Mode of Write Score is {}, {} and {} respectively".format(ws_mean, ws_median, ws_mode))

ws_std_deviation = statistics.stdev(WriteScore_list)

ws_first_std_deviation_start, ws_first_std_deviation_end = ws_mean - ws_std_deviation, ws_mean + ws_std_deviation
ws_second_std_deviation_start,ws_second_std_deviation_end = ws_mean - (2 * ws_std_deviation), ws_mean + (2 * ws_std_deviation)
ws_third_std_deviation_start, ws_third_std_deviation_end = ws_mean - (3 * ws_std_deviation), ws_mean + (3 * ws_std_deviation)

ws_list_of_data_within_1_std_deviation = [result for result in WriteScore_list if result > ws_first_std_deviation_start and result < ws_first_std_deviation_end]
ws_list_of_data_within_2_std_deviation = [result for result in WriteScore_list if result > ws_second_std_deviation_start and result < ws_second_std_deviation_end]
ws_list_of_data_within_3_std_deviation = [result for result in WriteScore_list if result > ws_third_std_deviation_start and result < ws_third_std_deviation_end]

print("{}% of data for Write marks lies within 1 standard deviations".format(len(ws_list_of_data_within_1_std_deviation)*100.0/len(WriteScore_list)))
print("{}% of data for Write marks lies within 2 standard deviations".format(len(ws_list_of_data_within_2_std_deviation)*100.0/len(WriteScore_list)))
print("{}% of data for Write marks lies within 3 standard deviations".format(len(ws_list_of_data_within_3_std_deviation)*100.0/len(WriteScore_list)))