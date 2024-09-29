class Solution:
    def maximumInvitations(self, favorites):
        return max(self._calculateMaxCycle(favorites), self._executeTopologicalSort(favorites))
    def _calculateMaxCycle(self, preferences):
        count = len(preferences)
        visited_set = [False] * count
        longest_cycle = 0
        for starting_point in range(count):
            if visited_set[starting_point]:
                continue
            current_cycle = []
            current_node = starting_point
            while not visited_set[current_node]:
                current_cycle.append(current_node)
                visited_set[current_node] = True
                current_node = preferences[current_node]
            for index in range(len(current_cycle)):
                if current_cycle[index] == current_node:
                    longest_cycle = max(longest_cycle, len(current_cycle) - index)
                    break
        return longest_cycle
    def _executeTopologicalSort(self, preferences):
        count = len(preferences)
        incoming_edges = [0] * count
        max_steps = [1] * count
        for choice in preferences:
            incoming_edges[choice] += 1
        processing_queue = []
        for i in range(count):
            if incoming_edges[i] == 0:
                processing_queue.append(i)
        while processing_queue:
            current_node = processing_queue.pop(0)
            next_node = preferences[current_node]
            max_steps[next_node] = max(max_steps[next_node], max_steps[current_node] + 1)
            incoming_edges[next_node] -= 1
            if incoming_edges[next_node] == 0:
                processing_queue.append(next_node)
        total_invites = 0
        for i in range(count):
            if i == preferences[preferences[i]]:
                total_invites += max_steps[i]
        return total_invites