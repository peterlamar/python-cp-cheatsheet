class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # start from back and move rocks down
        for r in box:
            last = len(box[0])-1
            for i in range(len(r)-1, -1, -1):
                if r[i] == '#':
                    r[i], r[last] = r[last], r[i]
                    last -= 1
                elif r[i] == '*':
                    last = i - 1
        return zip(*box[::-1])