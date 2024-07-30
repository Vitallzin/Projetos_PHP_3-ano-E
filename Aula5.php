<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        table{
            border-collapse: collapse;
            font-size: 200%;
        }
        td{
            border: 1px solid black;
        }
        .blueviolet{
            background-color: blueviolet;

        }
    </style>
</head>
<body>
    <?php
    echo"<h1>Tabelinha com as cores</h1>";
    echo"<table>";
    for( $i = 1; $i <= 10; $i++){
        if($i%2 == 0){
              echo"<tr><td class='blueviolet'>  $i</tr></td>";
            }
        else {
           echo"<tr><td>$i</tr></td>";
        }
    }
    echo"</table>";


    ?>
    
</body>
</html>