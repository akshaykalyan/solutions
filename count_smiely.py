def count_smileys(arr):
    x=0
    for x in range (len(arr)):
        if ")" in arr[x]:
        	print(arr[x])
			x+=1
		elif "D" in arr[x]:
        	print(arr[x])
			x+=1        
    return x
print(count_smileys([':)',':(',':D',':O',':;']))