from collections import deque
from json.tool import main
from posixpath import dirname
import queue
from turtle import left, right
import sys

from sklearn.exceptions import NonBLASDotWarning


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    def number_of_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.number_of_nodes(root.left) + self.number_of_nodes(root.right)

    def number_of_leaf_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.number_of_leaf_nodes(root.left) + self.number_of_leaf_nodes(root.right)

    def number_of_non_leaf_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return self.number_of_non_leaf_nodes(root.left) + self.number_of_non_leaf_nodes(root.right) + 1

    def number_of_full_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return self.number_of_full_nodes(root.left) + self.number_of_full_nodes(root.right) + (1 if (root.left is not None) and (root.right is not None) else 0)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def level_order_traversal(self, root):
        output_list = []
        if root is None:
            return output_list
        queue = deque([])
        queue.append(self.root)
        while len(queue) != 0:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                current_node = queue.popleft()
                current_level.append(current_node.data)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            output_list.append(current_level)
        return output_list

    def zig_zag_traversal(self, root):
        output_list = []
        if root is None:
            return output_list
        queue = deque([])
        queue.append(self.root)
        left_to_right = True
        while len(queue) != 0:
            level_size = len(queue)
            current_level = deque()
            for i in range(level_size):
                current_node = queue.popleft()
                if left_to_right:
                    current_level.append(current_node.data)
                else:
                    current_level.appendleft(current_node.data)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            output_list.append(current_level)
            left_to_right = not left_to_right
        return output_list

    # for loop iss liye hataya hai kyunki alag levels mein store karne ki need nahi thi
    # .data use karna is compulsary because data is stored as queue node object 
    def level_order_successor(self, root, key):
        if root is None:
            return None
        queue = deque([])
        queue.append(self.root)
        while len(queue) != 0:
            current_node = queue.popleft()
            
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
            if current_node.data == key:
                break
        return queue.popleft().data

    def minimum_depth(self,root):
        if root is None:
            return None
        queue = deque([])
        queue.append(self.root)
        depth=0
        while len(queue) != 0:
            depth+=1
            level_size=len(queue)
            for i in range(level_size):
                current_node = queue.popleft()
                if current_node.left is None and current_node.right is None:
                    return depth
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
        return depth

    def right_view(self, root):
        ans = []
        if root is None:
            return None
        queue = deque([])
        queue.append(self.root)
        while len(queue) != 0:
            level_size = len(queue)
            for i in range(level_size):
                current_node = queue.popleft()
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
                if i==level_size-1:
                    ans.append(current_node.data)
        return ans

    def left_view(self, root):
        ans = []
        if root is None:
            return None
        queue = deque([])
        queue.append(self.root)
        while len(queue) != 0:
            level_size = len(queue)
            for i in range(level_size):
                current_node = queue.popleft()
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
                if i==0:
                    ans.append(current_node.data)
        return ans

#--------------------------------------------------------------------------------------------------------------------------------------------------

    # Does binary tree path equal to given sum exist?    
    def haspath(self, root, sum):
        if root is None :
            return False
        
        if root.data == sum and root.left is None and root.right is None:
            return True
        
        return self.haspath(root.left, sum - root.data) or self.haspath(root.right, sum - root.data)   
    
    # Sum root to leaf numbers is
    def find_path_sum(self, root, pathsum):
        if root is None:
            return 0

        pathsum = pathsum * 10 + root.data

        if root.left is None and root.right is None:
            return pathsum
        
        return self.find_path_sum(root.left,pathsum) + self.find_path_sum(root.right,pathsum)
        

    def find_sum_path_numbers(self, root):
        return self.find_path_sum(root,0)

    # Given Sequence present in binary tree?
    def findSequence(self, root, sequence, index):
        if root is None:
            return False
        
        if index >= len(sequence) or root.data != sequence[index]:
            return False

        if root.left is None and root.right is None and root.data == sequence[index]:
            return True
        
        return self.findSequence(root.left, sequence, index + 1) or self.findSequence(root.right, sequence, index + 1)

    def haspath1(self,root,sequence):
        if root is None:
            return len(sequence)==0
        
        return self.findSequence(root,sequence,0)

    # Diameter of binary tree
    diameter = 0

    def findHeight1(self, root):
        if root is None:
            return 0

        leftHeight = self.findHeight1(root.left)
        rightHeight = self.findHeight1(root.right)

        currentDiameter = leftHeight + rightHeight + 1

        self.diameter = max(currentDiameter, self.diameter)

        return max(leftHeight, rightHeight) + 1
    
    def findDiameter(self, root):
        self.findHeight1(root)
        return self.diameter

    # Binary tree maximum path sum
    maxSum = -sys.maxsize

    def findMaxSumRecursive(self, root):
        if root is None:
            return 0
        
        leftSum = self.findMaxSumRecursive(root.left)
        rightSum = self.findMaxSumRecursive(root.right)

        # need explaination for this
        leftSum = max(leftSum, 0)
        rightSum = max(rightSum, 0)

        currentSum =leftSum + rightSum + root.data

        self.maxSum = max(currentSum, self.maxSum)

        return max(leftSum, rightSum) + root.data

    def findMaxSum(self, root):
        self.findMaxSumRecursive(root)
        return self.maxSum

    def lowestCommomAncestor(self,root,p,q):
        if root is None:
            return None
        
        if root.data == p.data or root.data == q.data:
            return root
        
        left = self.lowestCommomAncestor(root.left, p, q)
        right = self.lowestCommomAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        
        return left if left is not None else right


    

           

if __name__ == '__main__':
    tree = Tree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(4)

    print("Preorder traversal of binary tree is")
    tree.preorder(tree.root)
    print("\nInorder traversal of binary tree is")
    tree.inorder(tree.root)
    print("\nPostorder traversal of binary tree is")
    tree.postorder(tree.root)

    print("\nNumber of nodes in tree is", tree.number_of_nodes(tree.root))

    print("\nNumber of leaf nodes in tree is",
          tree.number_of_leaf_nodes(tree.root))

    print("\nNumber of non-leaf nodes in tree is",
          tree.number_of_non_leaf_nodes(tree.root))

    print("\nNumber of full nodes in tree is",
          tree.number_of_full_nodes(tree.root))

    print("\n----------------------------------------------------------------------------")

    print("\nLevel order traversal of tree is")
    print(tree.level_order_traversal(tree.root))

    print("\nZig-Zag traversal of tree is")
    print(tree.zig_zag_traversal(tree.root))

    #key=int(input("Enter value of which you want to level order traversal:\n"))
    #print("\nLevel order successor of "+str(key)+" is")
    #print(tree.level_order_successor(tree.root,key))

    print("\nMinimum Depth of binary tree is")
    print(tree.minimum_depth(tree.root))

    print("\nRight View of binary tree is")
    print(tree.right_view(tree.root))

    print("\nLeft view of binary tree is")
    print(tree.left_view(tree.root))

    print("\n----------------------------------------------------------------------------")

    #sum=int(input("\nEnter value of sum:\n"))
    #print("\nDoes binary tree path equal to given sum exist?")
    #print(tree.haspath(tree.root,sum))

    print("\nSum root to leaf numbers is")
    print(tree.find_sum_path_numbers(tree.root))

    #sequence = list(map(int,input("\nEnter sequence to be searched:\n").split(" ")))
    #print("\nGiven Sequence present in binary tree?")
    #print(tree.haspath1(tree.root, sequence))

    print("\nDiameter of binary tree is")
    print(tree.findDiameter(tree.root))

    print("\nBinary tree maximum path sum is")
    print(tree.findMaxSum(tree.root))

    p = tree.root.left.left
    q = tree.root.left.right
    print("\nLowest Common Ancestor of p and q is")
    lca=tree.lowestCommomAncestor(tree.root,p,q)
    print(lca.data)


