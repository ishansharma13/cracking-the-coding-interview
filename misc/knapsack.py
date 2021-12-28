# User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        s = [[0]*(W+1)]*(N+1)

        for i in range(N+1):
            for w in range(W+1):
                not_taking_item = s[i-1][w]
                taking_item = 0

                if wt[i-1] <= w:
                    taking_item = val[i-1]+s[i-1][w-wt[i-1]]
                s[i][w] = max(taking_item, not_taking_item)

        print(s)

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    #     N, W = [int(x) for x in input().split()]
    #     val = input().split()
    #     for itr in range(N):
    #         val[itr] = int(val[itr])
    #     wt = input().split()
    #     for it in range(N):
    #         wt[it] = int(wt[it])

    ob = Solution()
    print(ob.knapSack(2, 3, [1, 1], [2, 1]))
# } Driver Code Ends
