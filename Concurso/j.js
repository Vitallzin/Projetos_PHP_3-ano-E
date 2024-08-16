 // Função para buscar dados do CEP e preencher os campos
 async function buscarEndereco() {
    // Obtém o valor do campo CEP
    const cep = document.getElementById('cep').value.replace(/\D/g, '');

    // Verifica se o CEP é válido (somente números e com 8 dígitos)
    if (cep.length !== 8) {
        alert('CEP inválido');
        return;
    }

    try {
        // Substitua a URL abaixo pela URL da API que você está usando
        const resposta = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
        const dados = await resposta.json();

        // Verifica se a API retornou um erro
        if (dados.erro) {
            alert('CEP não encontrado');
            return;
        }

        // Preenche os campos com os dados retornados pela API
        document.getElementById('logradouro').value = dados.logradouro;
        document.getElementById('bairro').value = dados.bairro;
        document.getElementById('cidade').value = dados.localidade;
        document.getElementById('estado').value = dados.uf;
        // Limpa o campo número e complemento
        document.getElementById('numero').value = '';
        document.getElementById('complemento').value = '';
        
    } catch (error) {
        alert('Erro ao buscar o CEP. Tente novamente.');
        console.error(error);
    }
}