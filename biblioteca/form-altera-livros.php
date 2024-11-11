<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alterar Cadastro de Livros</title>
    <link rel="stylesheet" href="style-altera.css">
</head>
<body>
  <header>
    
      
        <h1 class="text-center">Cadastro Dos Livros</h1>
        <h3>Alterar/Excluir</h3>
    
  </header>
  <div class="container">
    

    <?php
    include "config.php";

    $codlivro = isset($_POST['codlivro']) ? (int)$_POST['codlivro'] : null;

    if ($codlivro > 0) {
        $sql = "SELECT * FROM livros WHERE CodLivro = $codlivro";
        $resultado = mysqli_query($conn, $sql) or die("Não foi possível realizar a consulta");

        $linha = mysqli_fetch_array($resultado);

        if (!$linha) {
            echo "<p style='color: red;'>Registro não encontrado.</p>";
        }
    }
    ?>

    <form action="altera-livro.php" method="post">
        <div>
            <label for="codlivro">Código:</label></br>
            <input type="text" id="codlivro" name="codlivro" readonly value="<?php echo isset($linha['CodLivro']) ? htmlspecialchars($linha['CodLivro']) : ''; ?>" required />
        </div>
        <div>
            <label for="titulo">Título:</label></br>
            <input type="text" id="titulo" name="titulo" value="<?php echo isset($linha['Titulo']) ? htmlspecialchars($linha['Titulo']) : ''; ?>" required />
        </div>
        <div>
            <label for="autor">Autor:</label></br>
            <input type="text" id="autor" name="autor" value="<?php echo isset($linha['Autor']) ? htmlspecialchars($linha['Autor']) : ''; ?>" required />
        </div>
        <div>
            <label for="editora">Editora:</label></br>
            <input type="text" id="editora" name="editora" value="<?php echo isset($linha['Editora']) ? htmlspecialchars($linha['Editora']) : ''; ?>" required />
        </div>
        <div>
            <label for="sinopse">Sinopse:</label></br>
            <textarea id="sinopse" name="sinopse" required><?php echo isset($linha['Sinopse']) ? htmlspecialchars($linha['Sinopse']) : ''; ?></textarea>
        </div>
        <div>
            <label for="ano_pub">Ano de Publicação:</label></br>
            <input type="number" id="ano_pub" name="ano_pub" min="1000" max="2100" value="<?php echo isset($linha['AnoPublicacao']) ? htmlspecialchars($linha['AnoPublicacao']) : ''; ?>" required />
        </div>
        <div>
            <label for="genero">Gênero:</label></br>
            <input type="text" id="genero" name="genero" value="<?php echo isset($linha['Genero']) ? htmlspecialchars($linha['Genero']) : ''; ?>" required />
        </div>
        <div>
            <label for="paginas">Número de Páginas:</label></br>
            <input type="number" id="paginas" name="paginas" value="<?php echo isset($linha['Paginas']) ? htmlspecialchars($linha['Paginas']) : ''; ?>" required />
        </div>
        <div>
            <button type="submit">Atualizar</button>
            <button type="button" onclick="excluirLivro()">Excluir</button>
        </div>
        
    </form>
  </div>
  <a href="listar-livros.php"><button title="Voltar ao início">Voltar</button></a>

  <script>
    function excluirLivro() {
      if (confirm('Tem certeza que deseja excluir este livro?')) {
        // Redireciona para a página de exclusão
        window.location.href = 'exclui-livro.php?codlivro=' + document.getElementById('codlivro').value;
      }
    }
    </script>
</body>
</html>