import React, { useState } from 'react';

function App() {

  const [temperatura, setTemperatura] = useState({ valor: 25, tipo: 'Celsius' });

  const converterCelsiusParaFahrenheit = () => {
    if(temperatura.tipo === 'Celsius'){
      const novaTemperatura = (temperatura.valor * 1.8) + 32;
      setTemperatura((information) => ({ ...information, valor: novaTemperatura, tipo: 'Fahrenheit' }))
    }
  }

  const converterFahrenheitParaCelsius = () => {
    if(temperatura.tipo === 'Fahrenheit'){
      const novaTemperatura = (temperatura.valor - 32) / 1.8;
      setTemperatura((information) => ({ ...information, valor: novaTemperatura, tipo: 'Celsius' }))
    }
  }

  return (
    <div>
      <h1>Conversor de Temperatura</h1>

      <button onClick={converterFahrenheitParaCelsius}>Celsius</button>
      <button onClick={converterCelsiusParaFahrenheit}>Fahrenheit</button>

      <h1>A temperatura do tipo {temperatura.tipo} é de {temperatura.valor} graus!</h1>

    </div>
  );
}

export default App;
