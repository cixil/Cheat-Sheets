# JQuery Cheat Sheet

JQuery is just javascript library to make life "easier"
The entire file can be viewed or referenced here: https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js

JQuery functions are used to select html elements and perform actions on them. The JQuery object is represented with $.

## Syntax
$(*selector*).*action*()

#### Document Ready Event
Put Jquery methods within the doc ready function to ensure they do not start before the page loads.
```
$(document).ready(function(){

   // jQuery methods go here...

}); 
```
This shorthand also works:
```
$(function(){

   // jQuery methods go here...

}); 
```

## Selectors
# Syntax		Description

$("*")
Selects all elements

$(this)
Selects the current HTML element

$("p.intro")
Selects all <p> elements with class="intro"

$("p:first")
Selects the first <p> element

$("ul li:first")
Selects the first <li> element of the first <ul>

$("ul li:first-child")
Selects the first <li> element of every <ul>

$("[href]")
Selects all elements with an href attribute

$("a[target='_blank']")
Selects all <a> elements with a target attribute value equal to "_blank"

$("a[target!='_blank']")
Selects all <a> elements with a target attribute value NOT equal to "_blank"

$(":button")
Selects all <button> elements and <input> elements of type="button"

$("tr:even")
Selects all even <tr> elements

$("tr:odd")
Selects all odd <tr> elements



## Events / Actions
Example Syntax:
```
$("p").dblclick(function(){
	 $(this).hide();
}); 
```

Mouse Events
Keyboard Events
Form Events
Document/Window Events
click
keypress
submit
load
dblclick
keydown
change
resize
mouseenter
keyup
focus
scroll
mouseleave
 
blur
unload


## DOM Manipulation

### GET
text		$(*selector*).text()
html		$(*selector*).html()
value		$(*selector*).val()
attribute	$(*selector*).attr(*attribute*) ~ ie “href” to get a link from an attribute

### SET
text		$(*selector*).text(*some text and stuff*)
works for html, val, attr
Example:
```
$("#btn1").click(function(){
    $("#test1").text("Hello world!");
});
```

### CSS
You can also edit css
```
$(*selector*).css("propertyname","value");

```
Set multiple properties
```
$(*selector*).css({"propertyname":"value","propertyname":"value",...});

```
Get an existing css value
```
$(*selector*).css("propertyname");
```

This is not a full Jquery reference.
I took notes while perusing https://www.w3schools.com/jquery
