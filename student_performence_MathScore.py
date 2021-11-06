import statistics
import pandas as pd
import csv

df = pd.read_csv('C:/Users/Meet Ankoliya/Python/project-13/StudentsPerformance.csv')

mathScore_list = df["math score"].to_list()

ms_mean = statistics.mean(mathScore_list)
ms_median = statistics.median(mathScore_list)
ms_mode = statistics.mode(mathScore_list)

print("Mean, Median and Mode of Math Score is {}, {} and {} respectively".format(ms_mean, ms_median, ms_mode))

ms_std_deviation = statistics.stdev(mathScore_list)

ms_first_std_deviation_start, ms_first_std_deviation_end = ms_mean - ms_std_deviation, ms_mean + ms_std_deviation
ms_second_std_deviation_start,ms_second_std_deviation_end = ms_mean - (2 * ms_std_deviation), ms_mean + (2 * ms_std_deviation)
ms_third_std_deviation_start, ms_third_std_deviation_end = ms_mean - (3 * ms_std_deviation), ms_mean + (3 * ms_std_deviation)

ms_list_of_data_within_1_std_deviation = [result for result in mathScore_list if result > ms_first_std_deviation_start and result < ms_first_std_deviation_end]
ms_list_of_data_within_2_std_deviation = [result for result in mathScore_list if result > ms_second_std_deviation_start and result < ms_second_std_deviation_end]
ms_list_of_data_within_3_std_deviation = [result for result in mathScore_list if result > ms_third_std_deviation_start and result < ms_third_std_deviation_end]

print("{}% of data for Math marks lies within 1 standard deviations".format(len(ms_list_of_data_within_1_std_deviation)*100.0/len(mathScore_list)))
print("{}% of data for Math marks lies within 2 standard deviations".format(len(ms_list_of_data_within_2_std_deviation)*100.0/len(mathScore_list)))
print("{}% of data for Math marks lies within 3 standard deviations".format(len(ms_list_of_data_within_3_std_deviation)*100.0/len(mathScore_list)))