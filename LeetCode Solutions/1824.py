class Solution:
    def minSideJumps(self, obstacles):
        inf_value = int(1e6)
        lane_jumps = [inf_value, 1, 0, 1]
        for current_obstacle in obstacles:
            if current_obstacle > 0:
                lane_jumps[current_obstacle] = inf_value
            for current_lane in range(1, 4):
                if current_lane != current_obstacle:
                    for previous_lane in range(1, 4):
                        lane_jumps[current_lane] = min(
                            lane_jumps[current_lane],
                            lane_jumps[previous_lane] + (0 if current_lane == previous_lane else 1))
        return min(lane_jumps[1:])