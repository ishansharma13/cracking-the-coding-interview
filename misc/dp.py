class Solution:
    def countNumberswith4(self, N):
        # code here
        self.c = [0]*(N+1)

        def count4(i):
            if i <= 4:
                self.c[4] += 1
                return 
            else:
                for j in range(i, i+1):
                    if j % 10 == 4:
                        self.c[j] +=1
                return count4(i-1)
        count4(N)
        return self.c.count(1)


if __name__ == '__main__':
    

    ob = Solution()
    print(ob.countNumberswith4(34))
