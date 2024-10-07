from flask import Flask, jsonify
from control.TerrenoController import TerrenoController

app = Flask("API Terreno")

# Função auxiliar para lidar com validações
def handle_validation_error(e):
    return jsonify({"erro": str(e)}), 400

# Endpoint GET: /terreno/dimensoes/<float:largura>/<float:comprimento>
@app.route('/terreno/dimensoes/<float:largura>/<float:comprimento>', methods=['GET'])
def get_dimensoes_terreno(largura, comprimento):
    try:
        terrenoController = TerrenoController()
        terrenoController.terreno_converter.largura = largura
        terrenoController.terreno_converter.comprimento = comprimento

        area = terrenoController.calcular_area()
        perimetro = terrenoController.calcular_perimetro()

        jsonResposta = {
            "largura": largura,
            "comprimento": comprimento,
            "area": area,
            "perimetro": perimetro
        }
        return jsonify(jsonResposta), 200
    except ValueError as e:
        return handle_validation_error(e)

# Inicia o servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
