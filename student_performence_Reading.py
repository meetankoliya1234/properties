import statistics
import pandas as pd
import csv

df = pd.read_csv('C:/Users/Meet Ankoliya/Python/project-13/StudentsPerformance.csv')

readScore_list = df["rriting score"].to_list()

rs_mean = statistics.mean(readScore_list)
rs_median = statistics.median(readScore_list)
rs_mode = statistics.mode(readScore_list)

print("Mean, Median and Mode of read Score is {}, {} and {} respectively".format(rs_mean, rs_median, rs_mode))

rs_std_deviation = statistics.stdev(readScore_list)

rs_first_std_deviation_start, rs_first_std_deviation_end = rs_mean - rs_std_deviation, rs_mean + rs_std_deviation
rs_second_std_deviation_start,rs_second_std_deviation_end = rs_mean - (2 * rs_std_deviation), rs_mean + (2 * rs_std_deviation)
rs_third_std_deviation_start, rs_third_std_deviation_end = rs_mean - (3 * rs_std_deviation), rs_mean + (3 * rs_std_deviation)

rs_list_of_data_rithin_1_std_deviation = [result for result in readScore_list if result > rs_first_std_deviation_start and result < rs_first_std_deviation_end]
rs_list_of_data_rithin_2_std_deviation = [result for result in readScore_list if result > rs_second_std_deviation_start and result < rs_second_std_deviation_end]
rs_list_of_data_rithin_3_std_deviation = [result for result in readScore_list if result > rs_third_std_deviation_start and result < rs_third_std_deviation_end]

print("{}% of data for read marks lies rithin 1 standard deviations".format(len(rs_list_of_data_rithin_1_std_deviation)*100.0/len(readScore_list)))
print("{}% of data for read marks lies rithin 2 standard deviations".format(len(rs_list_of_data_rithin_2_std_deviation)*100.0/len(readScore_list)))
print("{}% of data for read marks lies rithin 3 standard deviations".format(len(rs_list_of_data_rithin_3_std_deviation)*100.0/len(readScore_list)))