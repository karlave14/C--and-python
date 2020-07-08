# C language programing
### What it is?
 C is a procedural programming language, it was initially developed
 as a sytem programming language to write an operating system,
 it include low-level access to memory, a simple set of keywords
 and clean style.
### Structure of a C program

 *Header:* Here need to put libraries that need for example
  
	- #include<stdio.h> --> Input / output
	- #include<stdlib.h> --> Stardard library
	- #include<string.h> --> use by strings
	- #include<time.h> --> use by ramdom or data and time
	- #include<manth.h> --> use by found 
 *Main():* When you being write your code

	int main(){
	}
 *Variable declaration:* You declared all of variable that you will use 

	int a = 2;
 *Body:* write what is to do the program. 

	prinf("%d",a);
 *Return:* write what is the variable tat returns.

## Variable and keywords 

A varible in simple is terms is a storage place which has some memory
 allocated to it. Basically, a varible used to store some form of data. 
Different types of varibles require different amounts which can be applied on 
them.Can be num, a,b, etc.

  ###Type data of variable

Each data type requires different amounts of memory and has some specific 
operations which can be performed over it

    int // integet  
    char // character 
    short // is a short integer 
    long // longer 
    float // a number with decimals
    double // type varible is a 64-bit floatng

Declaration:

	type varible_name;
	type varible1, varible2;
 
###Keywords
 *Keywords* are reserved words has a specific feature associated with it. 
Almost all of the words wich help us use functionality.There are 32 keywords. 

	auto       break    case     char     const     continue
	default    do       double   else     enum      extern
	float      for      goto     if       int       long
	register   return   short    signed   sizeof    static
	struct     switch   typedef  union    unsigned  void
        volatile   while  

 * const: can be used to declared constant variables when initialized, can’t 
   change their value.
 * static: used to declare static varibles, wich are populary used while writhing
 programs. 
 * void: is an empty data type, has it has nothing or it holds no value. 
 * tydef: is used to give a new name to an already existing or even a custom data type. 

## Operators 

We can define operators as symbols that help us to perform specific mathematical 
and logical computations on operands.

### Arithmetic Operators
Used to perform arithmetic/mathematical operations on operands
* Unary Operators: ++ - 
* Binary Operators: +,-,*,/
### Relational Operators: 
Used by comparison of the values like ==.<,>,=<,=>;
###Logical
used to combine two or more conditions/constraints or to complement 
the evaluation of the original condition in consideration.
AND,&&
------Operators------

()	Parentheses 
[]	Brackets array	
.	Member selection via object name	
*	Member selection via pointer	
++/–	Postfix increment/decrement	
++/–	Prefix increment/decrement
+/-	Unary plus/minus
*	Dereference	
&	Address (of operand)	
sizeof	Determine size in bytes on this implementation	
||      or 
%       modulus
&&      And
=       assignment
,       expression separator
## Control Structurs

* if statements
* Schitch statment
* for (int i; i <10; i++){}
* while and do while 
## Special characters: 

* \n is a new line
* \t tab 
* \n null
* // coments
## Print formathing: 
* "%d";    // integer
* "%s";    // string
* "%f";    // float
* "%ld";   // long
* "%3.2f"; // minimum 3 digits left and 2 digits right decimal float
* "%c";    // char
## Files 

FILE is a pointer by to file. 
 *Fuctions*
 * fopen() create a new file or open a existing file
 * fclose() function closes the file that is being pointed by file
 * pointer fp. *Finally you need closed the file.*
 * getc() reads a character from a file
 * putc() writes a character to a file
 * fscanf() reads a set of data from a file                                                                                                                                                      * fprintf() writes a set of data to a file                                                                                                                                                      * getw() reads a integer from a file
 * putw() writes a integer to a file
 * fseek() set the position to desire point
 * ftell() gives current position in the file
 * rewind() set the position to the begining point

# Python language 
*Python* is a widely used general-prupose, high level programing language,
that lets you work quickly and integrate systems more efficiently.

##Primitive datatypes
* Numeric: Integers, Complex numbers, float.
* Dictionary.
* Boolean.
* Set.
* Secuence type: Strings, list,tuple. 
## Operators 
* + sum
* - subtraction.
* / division
* // integer positive
* % Modulo 
* ** Exponentation 
* ( ) parentheses by to separed 
* not true 
* not false
* and two true by true 
* or  one or two
* == comparison 
* != false
* < 
* >

### List 
*List* are ordered and have a definite count
	list []
*Diccionary* is an unordered collection of data values, used 
to store data values like a map.
	Dict={1:'karla' }
## Control Structurs

* if statements
* Schitch statment
* for 
* while and do while
