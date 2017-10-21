# JavaScript Cheat Sheet
In html, js code must be inside <script> tags
	-can be placed in <body> or <head> section
	-or linked to externally via <script src="path_to_script.js"></script>


### Display				example:
Window		window.alert()		window.alert("hello world!");
HTML Output		document.write()
HTML element	innerHTML		document.getElementByID("someID").innerHTML = 'something';
browser console	console.log()


### Syntax
Case-Sensitive!
statements end with ;
comments: single line //, multiple lines /* */
```if (condition) {
 block of code to be executed if the condition is true
} else if (condition2) {
 block of code to be executed if the condition1 is false and condition2 is true
} else {
 block of code to be executed if the condition1 is false and condition2 is false
}
```
```
switch(expression) {
 case n:
	 code block
	 break;
 case n:
 	code block
	 break;
 default:
	 code block
} 
```
```
for (statement 1; statement 2; statement 3) {
 code block to be executed
}
```
```
while (condition) {
	 code block to be executed
}
```

### Variables
var x;	x = 6;	var x = 6;
declared with var, not type specific

#### Arrays
var array_name = [item1, item2, ...];
array.toString()			returns array as list of comma separated values
array.join(“delimiter”)		like toString but can specify delimiter
array.sort()
many more
pop() and push()

### Strings
denoted by ' or ", concatenate with + or with string1.concat(“ “, string2, etc);
\ - escape char
can be a primitive:	var x = “string”;
or an object:		var x = new String(“string);

#### Methods
string.length				returns int of length
string.indexOf(“string2”)		returns index of first occurrence of string2
string.lastIndexOf(“string2”)		returns index of last occurrence of string2
string.indexOf(“string2”, int)	int specifies the starting position of search for index of string2
string.search(“string2”)		like indexOf, but no int parameter & accepts regular expressions
string.slice(int, int)			returns string between the int positions (accepts negative indexes)
string.substring(int)		
string.replace
string.toUpperCase or .toLowerCase
string.charAt(
string.split(“delimiter”)		returns string as array. Delimiter =”” for just single chars


### Operators
+, -, *, /, %, ++, --

+=, -=, etc,


### Functions
```function functionName(params, etc) {
	code;
}```
-Functions are invoked when it is called from js code, an event occurs, or self-invoked
-functions can be used as variables


### Objects
var pokemon = {name:"ditto", type:"normal", lv: 34}
pokemon.lv = 35;

Objects are containers for named values, or name:value pairs called properties
They are accessed via:
	objectName.propertyName 	or
	objectName["propertyName"]

object methods are invoked via
	objectName.methodName()


### Events
ie 
```<button onclick='displayDate()'>The time is ?</button>
<some-HTML-element some-event='some JavaScript'>```

Event 		Description
onchange 	An HTML element has been changed
onclick 	The user clicks an HTML element
onmouseover 	The user moves the mouse over an HTML element
onmouseout 	The user moves the mouse away from an HTML element
onkeydown 	The user pushes a keyboard key
onload 		The browser has finished loading the page


### Type Conversion
typeof variable 	returns type of variable

# JS Datatypes:
string
number 
boolean 
object 
function 
Objects:
Object 
Date 
Array 
data types that cannot contain values:
null 
undefined 
