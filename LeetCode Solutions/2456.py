class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator_stats = {}
        max_popularity = 0

        for i in range(len(creators)):
            creator = creators[i]
            video_id = ids[i]
            view_count = views[i]

            if creator not in creator_stats:
                creator_stats[creator] = {
                    'total_views': 0,
                    'max_views': -1,
                    'min_lex_id': video_id
                }

            stats = creator_stats[creator]
            stats['total_views'] += view_count

            if view_count > stats['max_views'] or (view_count == stats['max_views'] and video_id < stats['min_lex_id']):
                stats['max_views'] = view_count
                stats['min_lex_id'] = video_id

            max_popularity = max(max_popularity, stats['total_views'])

        result = []
        for creator, stats in creator_stats.items():
            if stats['total_views'] == max_popularity:
                result.append([creator, stats['min_lex_id']])

        return result