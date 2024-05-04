module.exports = (req, res) => {
    const { minimo = 1, maximo = 50, quantidade = 5, comb_size = 3 } = req.query;

    // Gerar número aleatório entre min e max
    const gerarNumeroAleatorio = (min, max) => {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min;
    };

    // Gerar números aleatórios
    const gerarNumerosAleatorios = (min, max, quant) => {
        let resultados = [];
        for (let i = 0; i < quant; i++) {
            resultados.push(gerarNumeroAleatorio(min, max));
        }
        return resultados;
    };

    // Gerar combinações
    const combinar = (arr, combSize) => {
        const combinations = [];
        const combine = (temp, left, right) => {
            if (combSize === temp.length) {
                combinations.push(temp.slice());
                return;
            }
            for (let i = left; i <= right; i++) {
                temp.push(arr[i]);
                combine(temp, i + 1, right);
                temp.pop();
            }
        };
        combine([], 0, arr.length - 1);
        return combinations;
    };

    // Processar dados
    const numeros = gerarNumerosAleatorios(parseInt(minimo), parseInt(maximo), parseInt(quantidade));
    const combinacoes = combinar(numeros, parseInt(comb_size));

    // Enviar resposta
    res.status(200).json({ numeros, combinacoes });
};
