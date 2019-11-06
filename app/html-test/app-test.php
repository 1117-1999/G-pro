<?php

function fileopen($p){

    $filepass = fopen($p,"r");
    $size = filesize($p);
    $data = fread($filepass, $size);
    fclose($filepass);

    return $data;
}

$id = $_POST['id'];
$pass = $_POST['pass'];

$text = fileopen("app-test.html");
echo "<br /><h1>".$id."</h1><h2>".$pass."</h2>";
?>