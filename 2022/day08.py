import numpy as np

def get_input():
    rows = []
    with open("2022/input08.txt") as f:
        for l in f:
            rows.append(l.replace("\n",""))
    return rows


def p1(heights):

    is_visible = np.zeros([len(heights), len(heights[0])])
    max_heights = np.zeros([len(heights), len(heights[0])])

    #top to bottom visible
    #left to right visible

    for i in range(heights.shape[0]):
        for j in range(heights.shape[1]):
            if (i== 0) | (j == 0) | (i == heights.shape[0]-1) | (j == heights.shape[1]-1):  #edges
                is_visible[i,j] = 1
            else: #interior
                if heights[i,j] > max(heights[:i, j]):
                    is_visible[i,j] = 1

                elif heights [i,j] > max(heights[i,:j]):
                    is_visible[i,j] = 1

    for i in reversed(range(heights.shape[0]-1)):
        for j in reversed(range(heights.shape[1]-1)):
            if (i== 0) | (j == 0) | (i == heights.shape[0]-1) | (j == heights.shape[1]-1):  #edges
                is_visible[i,j] = 1
            else: #interior
                if (heights[i, j] > max(heights[i + 1:, j])):
                    is_visible[i, j] = 1

                elif heights[i, j] > max(heights[i, j + 1:]):
                    is_visible[i, j] = 1
    return is_visible


trees = get_input()
heights = []

#615 not right
for t in trees:
    heights.append(list(t))
heights = np.array(heights)
results = p1(heights.copy())
num_vis = sum(sum(results))




def visible_trees(heights):
    scores = np.zeros([heights.shape[0], heights.shape[1]])
    def calc_score(r,c):
        # r=1
        # c=1
        score = [0,0,0,0]
        idx=1
        while (r+idx != heights.shape[0]) and (heights[r,c] > heights[r+idx,c]):
            # print("DOWN", r,c,idx,heights[r,c], heights[r+idx,c])
            score[0] += 1
            idx += 1
        if (r+idx != heights.shape[0]):
            score[0]+=1

        idx=1
        while (r-idx != -1) and (heights[r,c] > heights[r-idx,c]):
            # print("UP",r,c,idx,heights[r,c], heights[r-idx,c])

            score[1] += 1
            idx += 1
        if (r-idx != -1):
            score[1]+=1


        idx=1
        while (c+idx != heights.shape[1]) and (heights[r,c] > heights[r,c+idx]):
            score[2] += 1
            idx += 1
        if (c+idx != heights.shape[1]):
            score[2]+=1

        idx=1
        while (c-idx != -1) and (heights[r,c] > heights[r,c-idx]):
            score[3] += 1
            idx += 1
        if (c-idx != -1):
            score[3]+=1


        for idx in range(4):
            if score[idx] == 0:
                score[idx] = 1
        print(f"i,j = {i},{j} and", score)



        return score[0]*score[1]*score[2]*score[3]


    #Loop through the trees
    for i in range(1,heights.shape[0]-1):
        for j in range(1,heights.shape[1]-1):
            scores[i,j] = calc_score(i,j)
    return scores

#
# heights = np.array([[3,0,3,7,3]
#                     ,[2,5,5,1,2]
#                     ,[6,5,3,3,2]
#                     ,[3,3,5,4,9]
#                     ,[3,5,3,9,0]])


#151008 not right
#154440
#238464 too high
scores = visible_trees(heights)
print(np.max(np.max(scores)))