#################### C code of the program based on the Prefix Sum algorithm #################
# int n;
# printf("Please enter numer of array elements (maximum 20 element) \n");
# scanf("%d",&n);
# int arr[n];
# printf("Please enter the array elemnts \n");
# for (int i = 0;i<n;i++){
#	scanf("%d",arr[i]);
# }
# pre(sum,arr){
# sum[0] = arr[0]
# for(i=0;i<n;i++){
#  sum[i] = sum[i-1] + arr[i]
# }
# printf("The result :");
# for (int i=0;i<n;i++){
# printf("%d\t",sum[i]);
# }

##################### MIPS assembly code #########################

# intialize some strings and allocate space for the arrays

.data
	.align 2      # to read multi-byte values from memory at an address that's a multiple of the data size.
	arr: .space 80
	sum: .word 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0	
	msg1: .asciiz "Please enter number of array elements (maximum 20 element) \n"
	msg2: .asciiz "Please enter the array elemnts \n"
	msg3: .asciiz "The result :"
	msg4: .asciiz "can't get a sum of zero or negative array numbers.\n"
	tab: .asciiz "\t"
	
	
	
.text

getSize:
	# print msg1 -> Please enter numer of array elements (maximum 20 element)
	li $v0,4
	la $a0,msg1
	syscall 

	#take the number of the array element from the user the stores it in $s0
	li $v0, 5
	syscall 
	add $s0,$v0,$0

checkZero:
	bne $s0,$0,getElements
	li $v0,4
	la $a0,msg4
	syscall 
	j getSize
	
getElements:
	# print msg2 -> Please enter the array elemnts 
	li $v0,4  			# system call to print string
	la $a0,msg2
	syscall

	# take a copy of the number of array elemnts to use in other calculations
	move $s7,$s0
	sll $s7,$s7,2  		# multiply the num of array elements by 4 to be used directly in any comparisons later
	addi $t0,$0,0 		# intialize counter $t0 to 0 -used later-
	j input 

# main function
main: 
la $a0, arr 		# intialize $a0 with the address of the arr array
la $a1, sum 		# intialize $a1 with the address of the sum array


# main function to calculate prefix sum
pre:
	# assign the first element in the arr to the sum array
	lw $t0, 0($a0) 		# $t0 = arr[0]
	sw $t0, 0($a1)		# sum[0] = $t0 -> sum[0] = arr[0]	
	addi $s1,$0,1 		# intialize counter i=1 to iterate through the arrays

	
# iterating through the two arrays to caculate the other values to the sum array         
loop:
	sll $t1, $s1, 2  	# $t1 = i*4 
	add $t1,$t1,$a0  	# $t1 = arr[i]
	lw $t2, 0($t1)
	
	addi $t4,$s1,-1  	# $t4 = i-1 -> associated to sum[i-1]
	sll $t1, $t4, 2  	# $t1 = i*4 
	add $t1,$t1,$a1  	# $t1 = sum[i-1]
	lw $t3, 0($t1)
	
	sll $t1, $s1, 2 
	add $t1, $t1, $a1 
	
	add $t5, $t2,$t3 	# sum[i-1]+arr[i]
	
	sw $t5, 0($t1)		# sum[i] = sum[i-1]+arr[i]
	
# check for the i<n 
branch:
	addi $s1,$s1,1
	slt $t6, $s1, $s0
	bne $t6,$0,loop

# in case of finishing iterating through the arrays (our calculations are done) then jumps to sayGoodBye the print the result array
	j sayGoodBye 		


# input the array element 
input:
	beq $t0,$s7,exit	# checks if we reached the maimum number of the array element -> i<n
	
	li $v0,5  			# input the element
	syscall

	move $t9,$v0   		# copy it to $t0
	sw $t9, arr($t0)	# store the value to its place in the array
	
	addi $t0, $t0,4 	# increase the counter 
	j input

# return to the main after taking the array elements
exit:
	j main


# print the result -msg3 and call the output to print the sum array elements 
sayGoodBye: 
	li $v0, 4
	la $a0, msg3
	syscall
	addi $t0,$0,0  		# intialize counter i=0
	j output

# print the sum array elements
output:
	beq $t0,$s7,end
	lw $t9, sum($t0) 	# load the element from the memory to $t9
	
	li $v0,1 			# system call to print integers
	move $a0,$t9
    	syscall
    	
    	li $v0,4 
    	la $a0,tab		# print a tab between every element of the array 
    	syscall
    	
    	addi $t0,$t0,4
    	j output
		
		

end:
	
