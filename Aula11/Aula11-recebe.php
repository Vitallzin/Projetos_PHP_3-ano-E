<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $P = $_POST["P"];
    $A = $_POST["A"];
    $imc =$P/ $A * $A;
    echo "O IMC é: " ,$imc;
     if ( $imc <= 18.4 );
      echo "<h2>Você está abaixo do peso</h2>";
    elseif ($imc >= 24.9 );
     echo "<h2>Você está no peso ideal</h2>";
    


    header("Location: Aula11.php?imc=$imc&P=$P&A=&A&classificacao=$classificacao");
    ?>
    
</body>
</html>