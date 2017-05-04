<!DOCTYPE html> 
<html>
<head>
	<title>Admin page.</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="author" content="Gram - master_fess@mail.ru">
	<link rel="stylesheet" type="text/css" href="bootstrap.css">
</head>
<body>
<?php 
	$flag = 'flag{brute_without_dict_so_boring}';
	if(@$_COOKIE['token'] == $flag):
		echo 'Flag is near :)';
	else:

	if(@$_POST['password']) {
		if($_POST['password']=='qq') {
			SetCookie('token', $flag); 
			echo '<script>location.href=""</script>';
			}
		else
			echo '<p>Данные введены неверно!</p>';
		}
?>
<form method="POST">
	<input type="text" name="password" placeholder="Введите пароль" />
	<input type="submit" value="Войти" />
</form>
<?php endif; ?>
<p><i class="off">&copy; Gram <a href="mailto:master_fess@mail.ru">master_fess@mail.ru</a></i></p>
</body>
</html>
