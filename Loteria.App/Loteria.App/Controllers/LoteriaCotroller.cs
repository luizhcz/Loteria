using Microsoft.AspNetCore.Mvc;

namespace Loteria.App.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class LoteriaCotroller : ControllerBase 
    {
        public LoteriaCotroller() { }

        [HttpPost("GeraLoteria")]
        public Saida GeraLoteria([FromBody] Entrada entrada) 
        {
            List<int> numerosAleatorios = GerarNumerosAleatorios(entrada.MinimoAleatorio, entrada.MaximoAleatorio, entrada.QuantidadeAleatorio);

            List<int[]> combinacoes = GerarCombinacoes(numerosAleatorios.ToArray(), entrada.TamanhoCombinacao);

            return new Saida { 
                Combinacoes = combinacoes, 
                totalCombinacoes = combinacoes.Count,
                NumeroGerados = numerosAleatorios.ToArray()
            };
        }

        private static List<int> GerarNumerosAleatorios(int minimo, int maximo, int quantidade)
        {
            List<int> numeros = new List<int>();
            Random random = new Random();

            for (int i = 0; i < quantidade; i++)
            {
                numeros.Add(random.Next(minimo, maximo + 1));
            }

            return numeros;
        }

        private static List<int[]> GerarCombinacoes(int[] numeros, int tamanhoComb)
        {
            List<int[]> combinacoes = new List<int[]>();
            int[] combinacao = new int[tamanhoComb];
            int[] indices = new int[tamanhoComb];

            for (int i = 0; i < tamanhoComb; i++)
            {
                indices[i] = i;
            }

            bool finalizado = false;
            while (!finalizado)
            {
                for (int i = 0; i < tamanhoComb; i++)
                {
                    combinacao[i] = numeros[indices[i]];
                }

                combinacoes.Add((int[])combinacao.Clone());

                int indiceAtualizado = tamanhoComb - 1;
                while (indiceAtualizado >= 0 && indices[indiceAtualizado] == numeros.Length - tamanhoComb + indiceAtualizado)
                {
                    indiceAtualizado--;
                }

                if (indiceAtualizado < 0)
                {
                    finalizado = true;
                }
                else
                {
                    indices[indiceAtualizado]++;
                    for (int i = indiceAtualizado + 1; i < tamanhoComb; i++)
                    {
                        indices[i] = indices[i - 1] + 1;
                    }
                }
            }

            return combinacoes;
        }
    }
}