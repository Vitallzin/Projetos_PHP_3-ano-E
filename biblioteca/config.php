<?php
//Configuração do banco de dados
$db_host = "localhost"; //hostname do servidor de banco de dados
$db_user = "root"; // Nome do usuário para conectar ao banco de dados
$db_pass = ""; // Senha para se conectar ao banxo de dados (vazio é sem senha)
$db_name = "db_biblioteca"; //Nome do banco de dados

// Conectar ao banco de daodos, para conectar vai ter usar o $con
$conn = new mysqli ($db_host, $db_user, $db_pass, $db_name);

//Verificação deu certo
if ($conn->connect_error){
//Se houver um erro, exibir a mensagem de erro e encerrar a execução do script
//a seta -> é usada para acessar propriedades e métodos de objetos em PHP, tornando o código mais legivel e fácil de manter
 die("Conexão falhou: " . $conn->connect_error);
}



1


?>