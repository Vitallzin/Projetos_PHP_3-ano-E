<?php
include"config.php";
if (!$conn){
    die ("Falha na conexão: " . mysqli_connect_error());}

//Recebe os dados
$titulo = $_POST[`Titulo`];
$autor = $_POST['Autor'];
$editora = $_POST['Editora'];
$sinopse = $_POST['Sinopse'];
$anopub = $_POST['Anopub'];
$genero = $_POST['Genero'];
$pags = $_POST['Pags'];

//cria variaveis para inserir o registro
$sql = "INSERT INTO `livros`
(`Titulo`, `Autor`, `Editora`, `Sinopse`, `AnoPublicacao`, `Genero`, `Paginas`) VALUES 
('$titulo','$autor','$editora','$sinopse','$anopub','$genero','$pags')";


//executa a consulta sql. Se falhar, exibe erro do banco de dados;
$query = mysqli_query (mysql: $conn,query : $sql) or
die(mysqli_error(mysql: $conn));

if ($query){
    echo"<center>";
    echo "<h1>Registro inserido com sucesso!</h1></br>";
    echo "<a href='index.html'><button tittle = 'Home Page'>Voltar</button></a>";
    echo "</center>" ;
} 
else {
    echo"<center>";
    echo "<h1>Erro ao inserir registro!</h1></br>";
    echo "<a href='index.php'><button tittle = 'Home Page'>Voltar</button></a>";
    echo "</center>";
}



?>