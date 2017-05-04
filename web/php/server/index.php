<!DOCTYPE html> 
<html>
<head>
	<title>Admin page.</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="author" content="Gram - master_fess@mail.ru">
	<link rel="stylesheet" type="text/css" href="bootstrap.css">
</head>
<body>
<!--

//Пусть и тут будет, чтобы не забыть
$a = @$_GET['magic'];
if(isset($a)) {
	if(strpos($a,"answer") !== false && strlen($a) < 2) {
		echo $flag;
	} else {
		echo "You don't know the power of the dark side";
	}
}

-->
<?php
$flag = 'flag{1_am_y0ur_fath3r}';
$a = @$_GET['magic'];
if(isset($a)) {
	if(@strpos($a, "answer") !== false && @strlen($a) < 2)
		echo $flag;
	else
		echo "You don't know the power of the dark side";
	}
else
	echo '<p>Nothing interesting</p>';
?>
</body>
</html>
