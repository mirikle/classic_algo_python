import sys
from math import sqrt

class Node: pass
 
def distance_sq(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 
 
def kdtree(point_list, depth=0):
    if not point_list:
        return None
 
    # Select axis based on depth so that axis cycles through all valid values
    k = len(point_list[0]) # assumes all points have the same dimension
    axis = depth % k
 
    # Sort point list and choose median as pivot element
    point_list.sort(key=lambda point: point[axis])
    median = len(point_list) // 2 # choose median
 
    # Create node and construct subtrees
    node = Node()
    node.location = point_list[median]
    node.left = kdtree(point_list[:median], depth + 1)
    node.right = kdtree(point_list[median + 1:], depth + 1)
    return node

cur_np = None
cur_nd = sys.maxint
def query_nearest(subroot, point, depth=0):
    global cur_nd, cur_np
    
    cur_dist = distance_sq(subroot.location, point)
    if cur_dist < cur_nd:
        cur_nd = cur_dist
        cur_np = subroot.location 
    
    if not subroot.left and not subroot.right: return

    left_dist = sys.maxint
    right_dist = sys.maxint
    if subroot.left:
        left_dist = distance_sq(subroot.left.location, point)
    if subroot.right:
        right_dist = distance_sq(subroot.right.location, point)
    if left_dist < right_dist:
        query_nearest(subroot.left, point, depth + 1)
    else:
        query_nearest(subroot.right, point, depth + 1)

    if subroot.left and subroot.right:
        axis = depth % len(point)
        if left_dist < right_dist and point[axis] + sqrt(cur_nd) > subroot.location[axis]:
            if subroot.right: query_nearest(subroot.right, point)
        if left_dist >= right_dist and point[axis] - sqrt(cur_nd) < subroot.location[axis]:
            if subroot.left: query_nearest(subroot.left, point)
        

point_list = [(0.0, 0.0), (10.1, -10.1), (-12.2, 12.2), (38.3, 38.3), (79.99, 179.99)]
tree = kdtree(point_list)

query_nearest(tree, (10, -9))
print cur_np

