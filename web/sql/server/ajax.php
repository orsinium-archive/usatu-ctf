<?php
if (isset($_POST['auth']))
{
  $link = mysqli_connect("localhost", "root", "963741") or die(mysqli_error($link));
  mysqli_select_db($link, "usatuctf") or die(mysqli_error($link));

  libxml_use_internal_errors(true);
  libxml_disable_entity_loader(false);   
  $auth = @simplexml_load_string($_POST['auth'], "SimpleXMLElement", LIBXML_NOENT);
  foreach (libxml_get_errors() as $error) {
    printf("Error %d %d %s\n", $error->line, $error->level, $error->message);
  }
  libxml_clear_errors();
  $user = $auth->user;


  $pass = $auth->pass;
  $res = mysqli_query($link, "SELECT balance FROM logins WHERE user='{$user}' AND pass='{$pass}'") or die(mysqli_error($link));
  while($row = mysqli_fetch_assoc($res)) 
    printf("<p>Your balance: <b>{$row['balance']}</b></p>");
  
}

?>

