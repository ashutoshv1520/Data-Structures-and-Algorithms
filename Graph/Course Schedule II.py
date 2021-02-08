# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/course-schedule-ii/

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        a=[]
        
        for i in range(numCourses):
            a.append(i)
        
        a=list(set(a))
        
        indegree={}
        for i in a:
            indegree[i]=0
        
        d={}
        for i in indegree:
            d[i]=[]
        
        for edge in prerequisites:
            d[edge[1]].append(edge[0])
            indegree[edge[0]]=indegree[edge[0]]+1
            
        q=[]
        for i in indegree:
            if indegree[i]==0:
                q.append(i)
        
        ans=[]
        while len(q)!=0:
            v=q.pop()
            ans.append(v)
            for i in d[v]:
                indegree[i]=indegree[i]-1
                if indegree[i]==0:
                    q.append(i)
        if len(ans)!=len(a):
            return []
        elif ans==[]:
            return [0]
        else:
            return(ans)
    
        
        
        