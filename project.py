import statistics as st
import pandas as pd

file1 = pd.read_csv("StudentsPerformance.csv")
math_list = file1["math score"].to_list()
reading_list = file1["reading score"].to_list()
writing_list = file1["writing score"].to_list()

math_mean = st.mean(math_list)
reading_mean = st.mean(reading_list)
writing_mean = st.mean(writing_list)

math_median = st.median(math_list)
reading_median = st.median(reading_list)
writing_median = st.median(writing_list)

math_mode = st.mode(math_list)
reading_mode = st.mode(reading_list)
writing_mode = st.mode(writing_list)

math_stdev = st.stdev(math_list)
reading_stdev = st.stdev(reading_list)
writing_stdev = st.stdev(writing_list)

math_first_stdev_start, math_first_stdev_end = math_mean-math_stdev, math_mean+math_stdev
math_second_stdev_start, math_second_stdev_end = math_mean-(2*math_stdev), math_mean+(2*math_stdev)
math_third_stdev_start, math_third_stdev_end = math_mean-(3*math_stdev), math_mean+(3*math_stdev)

reading_first_stdev_start, reading_first_stdev_end = reading_mean-reading_stdev, reading_mean+reading_stdev
reading_second_stdev_start, reading_second_stdev_end = reading_mean-(2*reading_stdev), reading_mean+(2*reading_stdev)
reading_third_stdev_start, reading_third_stdev_end = reading_mean-(3*reading_stdev), reading_mean+(3*reading_stdev)

writing_first_stdev_start, writing_first_stdev_end = writing_mean-writing_stdev, writing_mean+writing_stdev
writing_second_stdev_start, writing_second_stdev_end = writing_mean-(2*writing_stdev), writing_mean+(2*writing_stdev)
writing_third_stdev_start, writing_third_stdev_end = writing_mean-(3*writing_stdev), writing_mean+(3*writing_stdev)

math_list_of_data_within_1_stdev = [result for result in math_list if result > math_first_stdev_start and result < math_first_stdev_end]
math_list_of_data_within_2_stdev = [result for result in math_list if result > math_second_stdev_start and result < math_second_stdev_end]
math_list_of_data_within_3_stdev = [result for result in math_list if result > math_third_stdev_start and result < math_third_stdev_end]

reading_list_of_data_within_1_stdev = [result for result in reading_list if result > reading_first_stdev_start and result < reading_first_stdev_end]
reading_list_of_data_within_2_stdev = [result for result in reading_list if result > reading_second_stdev_start and result < reading_second_stdev_end]
reading_list_of_data_within_3_stdev = [result for result in reading_list if result > reading_third_stdev_start and result < reading_third_stdev_end]

writing_list_of_data_within_1_stdev = [result for result in writing_list if result > writing_first_stdev_start and result < writing_first_stdev_end]
writing_list_of_data_within_2_stdev = [result for result in writing_list if result > writing_second_stdev_start and result < writing_second_stdev_end]
writing_list_of_data_within_3_stdev = [result for result in writing_list if result > writing_third_stdev_start and result < writing_third_stdev_end]

print("{}% of data for height lies within 1 standard deviation".format(len(math_list_of_data_within_1_stdev)*100.0/len(math_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(math_list_of_data_within_2_stdev)*100.0/len(math_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(math_list_of_data_within_3_stdev)*100.0/len(math_list)))

print("{}% of data for height lies within 1 standard deviation".format(len(reading_list_of_data_within_1_stdev)*100.0/len(reading_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(reading_list_of_data_within_2_stdev)*100.0/len(reading_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(reading_list_of_data_within_3_stdev)*100.0/len(reading_list)))

print("{}% of data for height lies within 1 standard deviation".format(len(writing_list_of_data_within_1_stdev)*100.0/len(writing_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(writing_list_of_data_within_2_stdev)*100.0/len(writing_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(writing_list_of_data_within_3_stdev)*100.0/len(writing_list)))