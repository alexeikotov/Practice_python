### 1 ###

def helloWorld(n):
	for i in range(n):
		if i%3 == 0 and i%5 == 0:
			print('helloworld')
		elif i%3 == 0:
			print('hello')
		elif i%5 == 0:
			print('world')
		else:
			print(str(i))

### 2 ###

def ones(lst):
	k=0; maxk = 0
	for i in lst:
		if i ==1:
			k+=1
		else:
			if maxk < k:
				maxk = k
			k=0
	print(maxk)

### 3 ###

def sumRanges(nums):
    ans = []
    
    if len(nums)==1:
        return([str(nums[0])])
    else:
        start = nums[0]
        end = None
        for i in range(1,len(nums)):
            delta = nums[i]-nums[i-1]
            if delta == 1 and i!=len(nums)-1:
                end = nums[i]
            elif delta!=1 and i!=len(nums)-1:
                if end == None:
                    ans.append(str(start))
                else:
                    ans.append(f"{start}->{end}")
                    end = None
                start = nums[i]
            elif delta == 1 and i==len(nums)-1:
                end = nums[i]
                ans.append(f"{start}->{end}")
            elif delta != 1 and i==len(nums)-1:
                if end == None:
                    ans.append(str(start))
                else:
                    ans.append(f"{start}->{end}")
                ans.append(str(nums[i]))              
        return ans
                
            

        
