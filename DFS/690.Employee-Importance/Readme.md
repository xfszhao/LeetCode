1. My DFS C++ Soution
```
/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/
class Solution {
private:
    unordered_map<int, Employee*> _id2emp;
public:
    int getImportance(Employee* emp) {
        int sumImpt = emp->importance;
        for (auto sub : emp->subordinates)   
            sumImpt += getImportance(_id2emp[sub]);
        return sumImpt;
    }
    
    int getImportance(vector<Employee*> employees, int id) {
        for (auto emp : employees)
        {
            _id2emp[emp->id] = emp;
        }
        return getImportance(_id2emp[id]);        
    }
};
```

2. My BFS Python Solution

```
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        map = {}
        for e in employees:
            map[e.id] = e
        from collections import deque
        dq = deque()
        dq.append(map[id])
        visited = set()
        sumImp = 0
        while dq:
            e = dq.popleft()
            if e in visited:
                continue
            visited.add(e)
            sumImp += e.importance
            for sub in e.subordinates:
                dq.append(map[sub])
        return sumImp
```
