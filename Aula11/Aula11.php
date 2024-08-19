<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    


<form action="Aula11-recebe.php" method="post">
    <label for="P">Peso:</label>
    <input type="text" name="P" required placeholder="O seu Peso"> <br>
    <label for="A">Altura:</label>
    <input type="text" name="A" required placeholder="A sua Altura"> <br>
    <button type="submit">Enviar</button>
    <input type="submit" value="somar"> <br>
    Resultado: <input type="text" width="5" value="<?php echo (isset($_GET["imc"])?$_GET["imc"]:"");?>"><br>


</body>
</html>