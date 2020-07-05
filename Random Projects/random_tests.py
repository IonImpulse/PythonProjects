class Solution:
    def maxPoints(self, points) -> int:
        def get_slope(p1, p2) :            
            if p1[0] == p2[0] :
                return "s"
            
            elif p1[1] == p2[1] :
                return "u"

            else :
                return (p2[1]-p1[1])/(p2[0]-p1[0])

        highest_path = 0
        current_path = 1

        for index_1, point in enumerate(points) :
            for index_2, second_point in enumerate(points) :
                if index_1 != index_2 :
                    current_path = 0
                    slope = get_slope(point, second_point)
                    
                    if slope != "s" and slope != "u" :
                        intercept = point[1] - (point[0] * slope)
                
                        for index_3, nth_point in enumerate(points) :
                            if nth_point[1] == (nth_point[0]) * slope + intercept or point == nth_point:
                                current_path += 1
                    else :
                        for nth_point in points :
                            if get_slope(point, nth_point) == slope or point == nth_point:
                                current_path += 1
            
            if current_path > highest_path : highest_path = current_path

        return highest_path

s = Solution()

inp = [[15,12],[9,10],[-16,3],[-15,15],[11,-10],[-5,20],[-3,-15],[-11,-8],[-8,-3],[3,6],[15,-14],[-16,-18],[-6,-8],[14,9],[-1,-7],[-1,-2],[3,11],[6,20],[10,-7],[0,14],[19,-18],[-10,-15],[-17,-1],[8,7],[20,-18],[-4,-9],[-9,16],[10,14],[-14,-15],[-2,-10],[-18,9],[7,-5],[-12,11],[-17,-6],[5,-17],[-2,-20],[15,-2],[-5,-16],[1,-20],[19,-12],[-14,-1],[18,10],[1,-20],[-15,19],[-18,13],[13,-3],[-16,-17],[1,0],[20,-18],[7,19],[1,-6],[-7,-11],[7,1],[-15,12],[-1,7],[-3,-13],[-11,2],[-17,-5],[-12,-14],[15,-3],[15,-11],[7,3],[19,7],[-15,19],[10,-14],[-14,5],[0,-1],[-12,-4],[4,18],[7,-3],[-5,-3],[1,-11],[1,-1],[2,16],[6,-6],[-17,9],[14,3],[-13,8],[-9,14],[-5,-1],[-18,-17],[9,-10],[19,19],[16,7],[3,7],[-18,-12],[-11,12],[-15,20],[-3,4],[-18,1],[13,17],[-16,-15],[-9,-9],[15,8],[19,-9],[9,-17]]
ad = [[1,1],[2,2],[3,3]]
print(s.maxPoints(inp))