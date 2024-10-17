<?php
include"config.php";
if (!$conn){
    die ("Falha na conexão: " . mysqli_connect_error());}

//Recebe os dados
$nome = $_POST['nome'];
$dtnasc = $_POST['Dtnasc'];
$celular = $_POST['Celular'];
$email = $_POST['Email'];
$RA = $_POST['RA'];
$endereco = $_POST['Endereco'];
$num_end = $_POST['NumEnd'];
$bairro = $_POST['Bairro'];
$cidade = $_POST['CidadeUF'];

//cria variaveis para inserir o registro
$sql = "INSERT INTO `leitores`
(`Nome`, `DtNasc`, `Celular`, `Email`, `RA`, `Endereco`, `NumEnd`, `Bairro`, `CidadeUF`) VALUES 
('$nome','$dtnasc','$celular','$email','$RA','$endereco','$num_end','$bairro','$cidade')";


//executa a consulta sql. Se falhar, exibe erro do banco de dados;
$query = mysqli_query (mysql: $conn,query : $sql) or
die(mysqli_error(mysql: $conn));

if ($query){
    echo"<center>";
    echo "<h1>Registro inserido com sucesso!</h1></br>";
    echo "<a href='index.php'><button tittle = 'Home Page'>Voltar</button></a>";
    echo "</center>" ;
} 
else {
    echo"<center>";
    echo "<h1>Erro ao inserir registro!</h1></br>";
    echo "<a href='index.php'><button tittle = 'Home Page'>Voltar</button></a>";
    echo "</center>";
}



?>