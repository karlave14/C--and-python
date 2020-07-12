
## Unit 4 
#### Members: 
* [Jason](https://github.com/JasonPinelo95/Programming_2/edit/master/UNIT_4)
* [Andrew]()
* [Karla](https://github.com/karlave14/C--and-python/blob/master/arraysfiles3.md)

## Arrays 

An arrays is a collection of items stored at contiguous memory 
locations and elements con be accssed randomly using indices of 
an array, they are used to store similar type of elemts as in
the data type ,must be the same for all elemts. 
They can be used to store collection of promitive data types 
such as int, float,double,char, to add to it, an array in c can
estore derived data tyoes such as the structure, pointers etc. 

We need do arrays, well if we want to store a large number of
intances, it becomesdificult to manage them with normal variables, 
the idea of an arrat is to repesent many instances in one varible

#### integer array: 

 * int a[10];

### character:
 
 * char b[10];

## Classification 

### One dimensional array
Where elements are stored one aster another. 

	arr[][][]
	----------
   an array of 3 elements
 *Systax:* datatype array_name[size];
 *datatype:* It denotes the type of the elements in the array
 *array_name:* Name of the array, It muct je a valid identifier. 
 *size:* Number of elements an arrays can hold. 
Example: 

	int num[100];
	float temp[20];
	char ch[30];  
 *Accsessing elements of an array*
 The elements can be accessed by specifying array name followed 
by subscript or index inside square brackets like [].Well index 
start at 0. If the size of an array is 4 the first element always 
is 0 and last element is at index 3. 

	int my_arr[3];
 
 First element – my_arr[0]
 Second element – my_arr[1]
 Third element – my_arr[2]

### Multi dimensinal array   

 The multi-dimensional Arrays is an array more than one dimension, 
 it is an array of arrays, as you will see in the code. A 2D array 
 is also called a matrix, or a table of rows and columns.
 Declaring a multi-dimensional array is similar to 
 the one-dimensinal arrays. 
 *Form of declaration:*
  type name[size1][size2]..[sizeN];
       
	int array[2][2]

## Files in C 



### Declaration and Description 

A file represents a sequence of bytes on the disk where a group of related data is stored. File is created for permanent 
 storage of data. It is a ready made structure.

Declaration: FILE *Fopen(const char *filename, const char * mode)
fopen()- is a function when used to open a dile to perform 
 operations such as reading, writing etc. 
*We declare a dile pointer and use fopen() as below, creates 
 a new file if the mentioned file nada does not exit.*
	
  *Operations of files*
 * “r” – Searches file. If the file is opened successfully fopen( ) loads 
  it into memory and sets up a pointer which points to the first character in it. 
  If the file cannot be opened fopen( ) returns NULL.
 * “w” – Searches file. If the file exists, its contents are overwritten. If the file doesn’t exist, 
 a new file is created. Returns NULL, if unable to open file.
 * “a” – Searches file. If the file is opened successfully fopen( ) loads it into memory and sets up 
  a pointer that points to the last character in it. 
  If the file doesn’t exist, a new file is created. Returns NULL, if unable to open file.
 * “r+” – Searches file. If is opened successfully fopen( ) loads it into memory and sets up a pointer 
  which points to the first character in it. 
  Returns NULL, if unable to open the file.
 * “w+” – Searches file. If the file exists, its contents are overwritten. If the file doesn’t exist a 
  new file is created. Returns NULL, if unable to open file.
 * “a+” – Searches file. If the file is opened successfully fopen( ) loads it into memory and sets up a 
  pointer which points to the last character in it. 
  If the file doesn’t exist, a new file is created. Returns NULL, if unable to open file.
	FILE *fp;
	fp=fopen("filename","mode");
 mode: refers to the operatin that will be performed on the file
 such: r - read, w - write, r+ - read and add,w+ - write and add.

 *Fuctions*
 * fopen() create a new file or open a existing file
 * fclose() function closes the file that is being pointed by file 
 * pointer fp. *Finally you need closed the file.*
 * getc() reads a character from a file
 * putc() writes a character to a file
 * fscanf() reads a set of data from a file
 * fprintf() writes a set of data to a file
 * getw() reads a integer from a file
 * putw() writes a integer to a file
 * fseek() set the position to desire point
 * ftell() gives current position in the file
 * rewind() set the position to the begining point
