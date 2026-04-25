from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        max_side_length = side
        num_points = len(points)
        point_positions = [0] * num_points
        perimeter = 4 * max_side_length
        extended_positions = [0] * (2 * num_points)

        for i in range(num_points):
            x, y = points[i]
            if y == 0:
                position = x
            elif x == max_side_length:
                position = max_side_length + y
            elif y == max_side_length:
                position = 3 * max_side_length - x
            else:  # x == 0
                position = 4 * max_side_length - y
            point_positions[i] = position

        point_positions.sort()

        for i in range(num_points):
            extended_positions[i] = point_positions[i]
            extended_positions[i + num_points] = point_positions[i] + perimeter

        def is_feasible(distance: int) -> bool:
            for i in range(num_points):
                count = 1
                last_position = extended_positions[i]
                current_index = i
                end_index = i + num_points
                while count < k:
                    target_position = last_position + distance
                    idx = bisect_left(extended_positions, target_position, current_index + 1, end_index)
                    if idx == end_index:
                        break
                    current_index = idx
                    last_position = extended_positions[current_index]
                    count += 1

                if count == k and (extended_positions[i] + perimeter - last_position) >= distance:
                    return True
            return False

        low, high = 0, 2 * max_side_length
        result = 0
        while low <= high:
            mid = (low + high + 1) // 2
            if is_feasible(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
