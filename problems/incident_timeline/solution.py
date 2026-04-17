# ============================================================
# Problem: Consolidate Incident Timelines
# ============================================================
# You receive incident reports as a list of plain-text strings.
# Each string has the format:
#
#   "incident=<ID>, start=<int>, end=<int>"
#
# Example input:
#   [
#       "incident=A, start=10, end=15",
#       "incident=A, start=12, end=18",
#       "incident=A, start=20, end=25",
#       "incident=A, start=17, end=19",
#   ]
#
# Requirements:
#   1. Parse each input string to extract the incident ID,
#      start time, and end time.
#   2. Group intervals by incident ID.
#   3. Merge overlapping or adjacent intervals within each
#      group. Two intervals overlap if the first's end >= the
#      second's start. They are adjacent if the first's
#      end + 1 == the second's start. In both cases, merge
#      them into a single interval spanning the combined range.
#   4. Return a dict mapping each incident ID to a list of
#      merged (start, end) tuples, sorted by start time.
#      The dict keys should be in alphabetical order.
#
# Formally, intervals [a, b] and [c, d] (where a <= c after
# sorting) should be merged when b + 1 >= c.
#
# Return type: dict[str, list[tuple[int, int]]]
#
# Example output for the input above:
#   {"A": [(10, 25)]}
#
# Explanation:
#   Sorted intervals for A: [10,15], [12,18], [17,19], [20,25]
#   [10,15] + [12,18] -> [10,18]  (overlap: 15 >= 12)
#   [10,18] + [17,19] -> [10,19]  (overlap: 18 >= 17)
#   [10,19] + [20,25] -> [10,25]  (adjacent: 19+1 == 20)
# ============================================================
from collections import defaultdict


def consolidate_timelines(reports: list[str]) -> dict[str, list[tuple[int, int]]]:

    incident_dict = defaultdict(list)

    for report in reports:
        report_parts = report.split(",")
        incident_id = report_parts[0].split("=")[1]
        start_time = report_parts[1].split("=")[1]
        end_time = report_parts[2].split("=")[1]
        incident_dict[incident_id].append((int(start_time), int(end_time)))

    result_dict = defaultdict(list)
    for inc_id, intervals in incident_dict.items():
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        result_dict[inc_id].append(sorted_intervals[0])
        for i, interval in enumerate(sorted_intervals):
            if i == 0:
                continue
            # merge scenario
            last_interval_inserted = result_dict[inc_id][-1]
            if last_interval_inserted[1] + 1 >= interval[0]:
                last_interval_inserted = (last_interval_inserted[0], max(last_interval_inserted[1], interval[1]))
                result_dict[inc_id][-1] = last_interval_inserted
            # add this interval as-is to the result list
            else:
                result_dict[inc_id].append(interval)

    sorted_result_dict = dict(sorted(result_dict.items(), key=lambda item: item[0]))
    return sorted_result_dict