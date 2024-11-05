<?php
include "config.php";

// Consulta para obter todos os leitores
$sql_leitores = "SELECT CodLeitor, Nome FROM leitores ORDER BY Nome";
$result_leitores = mysqli_query($conn, $sql_leitores);

// Consulta para obter todos os livros
$sql_livros = "SELECT CodLivro, Titulo FROM livros ORDER BY Titulo";
$result_livros = mysqli_query($conn, $sql_livros);
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Empréstimos</title>
    <link rel="stylesheet" href="style2.css">
</head>
<body>
    <header>
        <h1 class="text-center">CADASTRO DE EMPRÉSTIMOS</h3>
        <hr>
    </header>
    <div class="container">
        <div class="box">
            <form action="cadastra-emprestimo.php" method="post">
                <div>
                    <label for="codleitor"></label>
                    <select id="codleitor" name="codleitor" aria-placeholder="Leitor" required>
                        <option value="">Selecione um leitor</option>
                        <?php
                        while ($row = mysqli_fetch_assoc($result_leitores)) {
                            echo "<option value='" . $row['CodLeitor'] . "'>" . $row['CodLeitor'] . " - " . $row['Nome'] . "</option>";
                        }
                        ?>
                    </select>
                </div>
                <div>
                    <label for="codlivro"></label>
                    <select id="codlivro" name="codlivro" aria-placeholder="Livro" required>
                        <option value="">Selecione um livro</option>
                        <?php
                        while ($row = mysqli_fetch_assoc($result_livros)) {
                            echo "<option value='" . $row['CodLivro'] . "'>" . $row['CodLivro'] . " - " . $row['Titulo'] . "</option>";
                        }
                        ?>
                    </select>
                </div>
                <div>
                    <label for="data_emprestimo">Data do Empréstimo:</label>
                    <input type="date" id="data_emprestimo" name="data_emprestimo" required />
                </div>
                <div>
                    <label for="data_devolucao">Data de Devolução:</label>
                    <input type="date" id="data_devolucao" name="data_devolucao" required />
                </div>
                <div>
                    <button type="submit">Cadastrar Empréstimo</button>
                    <a href="index.html"><button title="Voltar ao início">Voltar</button></a>
                </div>
            </form>
        </div>
    </div>
</body>
</html>

<?php
mysqli_close($conn);
?>