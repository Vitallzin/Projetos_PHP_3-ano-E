<?php
include"config.php";
if (!$conn){
    die ("Falha na conexão {mysqli_connect_error()}");}

//Recebe os dados

$nome = '';
$dtnasc = '';
$celular = '';
$email = '';
$RA = '';
$endereco = '';
$num_end = '';
$bairro = '';
$cidade = '';

//cria variaveis para inserir o registro
$sql = "";


?>