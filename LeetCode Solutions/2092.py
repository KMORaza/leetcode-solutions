from collections import deque, defaultdict
class Solution:
    def findAllPeople(self, total_count: int, gatherings: list[list[int]], starter: int) -> list[int]:
        known_status = [False] * total_count
        known_status[0] = True
        known_status[starter] = True
        gatherings.sort(key=lambda event: event[2])
        current_index = 0
        while current_index < len(gatherings):
            final_index = current_index
            while final_index + 1 < len(gatherings) and gatherings[final_index + 1][2] == gatherings[current_index][2]:
                final_index += 1
            meeting_graph = defaultdict(list)
            attendees = set()
            for meeting in range(current_index, final_index + 1):
                participant_A, participant_B = gatherings[meeting][0], gatherings[meeting][1]
                meeting_graph[participant_A].append(participant_B)
                meeting_graph[participant_B].append(participant_A)
                attendees.add(participant_A)
                attendees.add(participant_B)
            bfs_queue = deque()
            for person in attendees:
                if known_status[person]:
                    bfs_queue.append(person)
            while bfs_queue:
                current_person = bfs_queue.popleft()
                for adjacent in meeting_graph[current_person]:
                    if not known_status[adjacent]:
                        known_status[adjacent] = True
                        bfs_queue.append(adjacent)
            current_index = final_index + 1
        known_individuals = [idx for idx in range(total_count) if known_status[idx]]
        return known_individuals
