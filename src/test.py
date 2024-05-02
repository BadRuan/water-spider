from util.datetool import get_target_year_date_range_list

if __name__ == "__main__":
    
    date_list = get_target_year_date_range_list(2023)
    for i in date_list:
        print(i)