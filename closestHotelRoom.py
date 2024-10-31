from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms: list[list[int]], queries: list[list[int]]) -> list[int]:
        rooms.sort(key=lambda room: room[1], reverse=True) 
        r = 0 

        avail = SortedList() # list of ids
        ans = [-1]*len(queries)
        qidxs = list(range(len(queries)))
        qidxs.sort(key=lambda i: queries[i][1], reverse=True)

        for qidx in qidxs:
            
            pref, minsize = queries[qidx]
            while r < len(rooms) and rooms[r][1] >= minsize:
                avail.add(rooms[r][0])
                r += 1

            if not avail: continue # leave answer as -1

            i = avail.bisect_left(pref)
            if i == len(avail):
                ans[qidx] = avail[-1]
            else:
                id = avail[i] 
                if i:
                   
                    lower = avail[i-1]
                    if pref-lower <= id-pref:
            
                        id = lower

                ans[qidx] = id

        return ans


