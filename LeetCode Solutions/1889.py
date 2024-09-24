class Solution:
    def minWastedSpace(self, parcel_weights, shipping_boxes):
        total_weight_of_parcels = sum(parcel_weights)
        least_space_wasted = 10**12
        parcel_weights.sort()
        for box in shipping_boxes:
            box.sort()
            if box[-1] < parcel_weights[-1]:
                continue
            total_space_used = 0
            current_index = 0
            for box_capacity in box:
                next_index = self.findFirstIndexGreaterThanOrEqual(parcel_weights, box_capacity + 1)
                total_space_used += box_capacity * (next_index - current_index)
                current_index = next_index
            least_space_wasted = min(least_space_wasted, total_space_used)
        return -1 if least_space_wasted == 10**12 else (least_space_wasted - total_weight_of_parcels) % (10**9+7)
    def findFirstIndexGreaterThanOrEqual(self, weight_array, threshold):
        low, high = 0, len(weight_array)
        while low < high:
            mid = (low + high) // 2
            if weight_array[mid] >= threshold:
                high = mid
            else:
                low = mid + 1
        return low
