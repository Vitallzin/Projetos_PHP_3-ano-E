<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
    $name = $_POST["name"];
    $pass = $_POST["pass"];

    if ($name == "Maria" and $pass == 12345)
    {
        echo"<h2>Seja bem-vindo, agora veja esse belo homem</h2>";
        echo"<img src='5.jpg'>";
    }
    
    else
    {
        echo"<h2>Senha ou nome incorreta. Você não tem permissão de vissualizar essa página</h2>";
    }

    
?>
    
</body>
</html>