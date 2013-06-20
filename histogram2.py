heights = [7, 2, 1, 4, 5, 1, 3, 3]

l_bound = [i for i in range(len(heights))]
r_bound = [i for i in range(len(heights))]

max_area = -2 ** 32
left = -1
right = -1
height = -1

for i in range(len(heights)):
    while l_bound[i] > 0 and heights[l_bound[i] - 1] >= heights[i]:
        l_bound[i] = l_bound[l_bound[i] - 1]
    while r_bound[i] < len(heights) - 1 and heights[r_bound[i] + 1] >= heights[i]:
        r_bound[i] = r_bound[r_bound[i] + 1]
    
    area = (r_bound[i] - l_bound[i] + 1) * heights[i]
    if area > max_area:
        max_area = area
        left = l_bound[i]
        right = r_bound[i]
        height = heights[i]

print max_area, left, right, height
