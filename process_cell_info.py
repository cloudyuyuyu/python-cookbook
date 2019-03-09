import os
import numpy as np
import pandas as pd
import json
import re

if __name__ == "__main__":
    # source_dir = "C:/Software/cmder/AIDataFiles/User_Hand_2019_03_09_15_41/Cells_User_Hand_2019_03_09_15_41"
    # lte_pattern = re.compile(r"LTE;-?\d+;-?\d+;-?\d+;-?\d+;-?\d+;-?\d+;-?\d+;-?\d+;-?\d+")
    # target_data_frame = pd.DataFrame(columns=["time", "count", "details"])
    #
    # for file in os.listdir(source_dir):
    #     with open(os.path.join(source_dir, file),
    #               encoding="utf-8") as f:
    #         for line in f:
    #             if len(line) == 0:
    #                 continue
    #
    #             current_dict = dict(time=0, count=0, details=None)
    #             current_dict["time"] = line.split(";")[0]
    #             cell_info_dict = dict.fromkeys(["is_register", "station_id", "mobile_country_code",
    #                                             "mobile_network_code", "physical_cell_id", "tracking_area_code",
    #                                             "asu_level", "reference_signal_received_power", "signal_level"])
    #             details_dict = dict()
    #             for matcher in lte_pattern.findall(line):
    #                 matcher_list = matcher.split(";")
    #                 is_register = matcher_list[1]
    #                 station_id = matcher_list[2]
    #                 mobile_country_code = matcher_list[3]
    #                 mobile_network_code = matcher_list[4]
    #                 physical_cell_id = matcher_list[5]
    #                 tracking_area_code = matcher_list[6]
    #                 asu_level = matcher_list[7]
    #                 reference_signal_received_power = matcher_list[8]
    #                 signal_level = matcher_list[9]
    #
    #                 if physical_cell_id != "2147483647":
    #                     cell_info_dict["is_register"] = is_register
    #                     cell_info_dict["station_id"] = station_id
    #                     cell_info_dict["mobile_country_code"] = mobile_country_code
    #                     cell_info_dict["mobile_network_code"] = mobile_network_code
    #                     cell_info_dict["physical_cell_id"] = physical_cell_id
    #                     cell_info_dict["tracking_area_code"] = tracking_area_code
    #                     cell_info_dict["asu_level"] = asu_level
    #                     cell_info_dict["reference_signal_received_power"] = reference_signal_received_power
    #                     cell_info_dict["signal_level"] = signal_level
    #
    #                     details_dict[str(current_dict["count"])] = cell_info_dict.copy()
    #                     current_dict["count"] += 1
    #
    #             current_dict["details"] = json.dumps(details_dict)
    #             target_data_frame = pd.concat([target_data_frame, pd.DataFrame(current_dict,
    #                                                                            index=[0])],
    #                                           axis=0,
    #                                           ignore_index=True)
    # target_data_frame = target_data_frame.sort_values(by="time")
    # target_data_frame.to_csv("cell_info.csv",
    #                          index=False)

    """
    Parse Csv File
    """
    source_data_frame = pd.read_csv("cell_info.csv")
    start_current = source_data_frame["time"].min()
    end_time = source_data_frame["time"].max()

    count_per_min = np.array([])
    asu_level_per_min = np.array([])
    signal_strength_per_min = np.array([])

    while True:
        end_current = start_current + 1000 * 60
        if end_current > end_time:
            break

        else:
            current_range = np.arange(start_current, end_current)
            start_current = end_current

        current_data_frame = source_data_frame[source_data_frame["time"].isin(current_range)]

        count_of_one_min = np.array([])
        asu_level_of_one_min = np.array([])
        signal_strength_of_one_min = np.array([])

        for index, row in current_data_frame.iterrows():
            print(index)
            count_of_one_min = np.append(count_of_one_min, int(row["count"]))
            details_dict = json.loads(row["details"])
            if len(details_dict) == 0:
                continue
            for _, cell_info in details_dict.items():
                asu_level_of_one_min = np.append(asu_level_of_one_min, int(cell_info["asu_level"]))
                signal_strength_of_one_min = np.append(signal_strength_of_one_min, int(cell_info["signal_level"]))

        count_per_min = np.append(count_per_min, np.mean(count_of_one_min))
        asu_level_per_min = np.append(asu_level_per_min, np.mean(asu_level_of_one_min))
        signal_strength_per_min = np.append(signal_strength_per_min, np.mean(signal_strength_of_one_min))

    print(count_per_min)
    print(asu_level_per_min)
    print(signal_strength_per_min)
