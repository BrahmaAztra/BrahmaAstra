<?php 
 
$localhost 	= "localhost"; 
$username 	= "root"; 
$password 	= "hunter"; 
$dbname 	= "studentdb"; 
 
$con = new mysqli($localhost, $username, $password, $dbname); 

if($con->connect_error) {
    die("connection failed : " . $con->connect_error);
} 
 
?>