# PHP Cheat Sheet
PHP is server scripting language. 
PHP files 
  - can contain text, HTML, CSS, JS and PHP code
  - are executed on the server and returned to the browser as HTML


## Syntax
A PHP script can be placed anywhere in the document.              Not case sensitive.
```
<?php
  // PHP code here
?>
```
**Comments**  Single-line: // or #. Multiline or within line: /*  */
Statements end with ;


## Variables
Start with a $, followed by var name                       Case sensitive!
Variables cannot be declared without assignment.
```
$txt = "hello worldi"; // example
```
PHP supports the following data types:

    String    ~ denoted with either " or '
    Integer
    Float (floating point numbers - also called double)
    Boolean
    Array     ~ $cars = array("Volvo","BMW","Toyota"); //example
    Object
    NULL
    Resource  ~ not actual datatype. Stores references to external functions and resources



## Print / Echo
Only difference is that echo has no return value and print returns 1. Echo can take multiple parameters and is marginally faster.
```
echo "<h1>" . $txt . "</h1>";
echo "printing contents of some var: $txt";
echo "This ", "string ", "was ", "made ", "with multiple parameters.";
```


## PHP Cookies
**Syntax**
```
 setcookie(name, value, expire, path, domain, secure, httponly);
 ```
 To modify a cookie, just use setcookie again
 To delete a cookie, use setcookie with an expiration date in the past
 
 ## PHP Sessions
 This must be the first thing in the document, before any html:
 ```
 <?php
session_start();
?>

<!DOCTYPE html>
<html>
...
```
Session variables start with the php global variable $\_session
```
$_SESSION["variable_name"] = value;
 ```

To end a php session:
```
<?php
session_unset();  // remove all session variables
session_destroy();  // destroy the session
?>
```
