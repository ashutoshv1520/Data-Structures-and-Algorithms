# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/course-schedule/

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        a=[]
        for i in prerequisites:
            a.append(i[0])
            a.append(i[1])
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
        
        if len(a)==len(ans):
            return True
        else:
            return False
        
        
        
        