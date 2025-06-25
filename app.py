from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página inicial (onde o formulário aparece)
@app.route('/')
def home():
    return render_template('index.html')

# Rota para calcular o IMC (quando o botão é clicado)
@app.route('/calcular', methods=['POST'])
def calcular_imc():
    # --- Pega os dados do formulário HTML ---
    # O request.form pega o que veio do formulário web.
    # O .get() é seguro porque se o campo não existir, ele não dá erro.
    peso_texto = request.form.get('peso')
    altura_texto = request.form.get('altura')

    # --- Tenta converter para números e faz o cálculo ---
    try:
        peso = float(peso_texto)
        altura = float(altura_texto)

        # Evita divisão por zero ou altura inválida
        if altura <= 0:
            imc = 0.0 # Define um valor padrão ou você pode retornar uma mensagem de erro
            classificacao = "Altura inválida!"
        else:
            imc = peso / (altura * altura) # Sua fórmula de IMC!

            # --- Classificação do IMC (seu código Python de antes!) ---
            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif imc >= 18.5 and imc < 24.9:
                classificacao = "Peso normal"
            elif imc >= 25 and imc < 29.9:
                classificacao = "Sobrepeso"
            elif imc >= 30 and imc < 34.9:
                classificacao = "Obesidade Grau I"
            elif imc >= 35 and imc < 39.9:
                classificacao = "Obesidade Grau II"
            else:
                classificacao = "Obesidade Grau III ou Mórbida"

    except (ValueError, TypeError):
        # Caso o usuário não digite números válidos
        imc = None # Ou 0.0, para indicar que não foi possível calcular
        classificacao = "Por favor, digite números válidos para peso e altura."

    # --- Devolve o resultado para o HTML ---
    # render_template envia de volta a mesma página HTML,
    # mas agora com as variáveis 'imc' e 'classificacao' preenchidas.
    return render_template('index.html', imc=imc, classificacao=classificacao)

# Inicia o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True) # debug=True é bom para desenvolvimento, mostra erros no navegador