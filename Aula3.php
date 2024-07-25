<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1{
            color: blueviolet;
        }
        table{
            border-collapse: collapse;
            font-size: 150%;
        }
        td{
            border: 1px solid black;
            font-size: 150%;
        }

    </style>
</head>
<body>
    <?php
    echo"<h1> Contando de 1 a 10</h1>";
    echo"<table><td>";

    for ($x = 1; $x <= 10; $x++ ){
        echo "<td>$x</td>";
    }
    echo"</td></table>";


    echo "<h1>Tabela de 1 a 10 em PHP</h1>";


    ?>

    
</body>
</html>