def selectionSort(arr):
	n=len(arr)
	for i in range(n):
		min=i
		for j in range(i+1,n):
			if arr[j]<arr[min]:
				min=j
		arr[i],arr[min]=arr[min],arr[i]
	return arr
	
def main():
	arr=[]
	n=int(input("ENTER NUMBER OF ELEMENTS IN ARRAY: "))
	for i in range(n):
		ele=int(input(f"ENTER ELEMENT {i}: "))
		arr.append(ele)
	while True:
		print("\n\n\t**************MENU***************")
		print("\n\t1.SELECTION SORT\n\t2.EXIT")
		choice=int(input("\n\tENTER YOUR CHOICE: "))
		if choice==1:
			selectionSort(arr)
			print(f"\n\tArray: {arr}")
		elif choice==2:
			print("\n\tExiting....")
			break
		else: 
			print("\n\tInvalid Choice!!!")
main()
