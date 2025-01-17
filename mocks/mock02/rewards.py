class Solution:
    # Complexity
    # Time: O(nlogn) - sorting result array
    # Space: O(n) - dictionary
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        # converting the both positive_feedback and negative_feedback for fast accessing.
        pos= set(positive_feedback) # O(1) search, O(m) space
        neg= set(negative_feedback) # O(1) search, O(m) space
        d={}   #dictionary to store every student points

        # for eacho report
        for i in range(len(report)):
            pts=0 # points
            lst=report[i].split() # split by space
            for j in lst: # for each word in report
                if j in pos:    # if positive feedback
                    pts+=3
                if j in neg:    # if negative feedback
                    pts-=1
            d[student_id[i]]=pts  #storing the final points

        #sorting the dictionary accoring to max points
        final_lst=list(sorted(d.items(),key=lambda x : (x[-1],-x[0]),reverse=True))
        ans=[]  #to store final answer
        for i in range(k): # getting k highest scores
            ans.append(final_lst[i][0])
        return ans

s = Solution()
positive_feedback = ["smart","brilliant","studious"]
negative_feedback = ["not"]
report = ["this student is studious","the student is smart"]
student_id = [1,2] # student IDs
k = 2 # top k students to return from result
r = s.topStudents(positive_feedback, negative_feedback, report, student_id, k)
print(r)

# Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
# Output: [1,2]
# Explanation:
# Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.