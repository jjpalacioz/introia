# Gemma 4 – Vision Token Budget

## 1. Nombre del Space

- **Nombre:** Gemma 4 – Vision Token Budget
- **Enlace:** https://huggingface.co/spaces/google/gemma4_vision_token_budget

## 2. ¿Qué hace el agente?

Es una herramienta que toma una imagen (subida por el usuario o una de muestra, como la palmera) y genera varias versiones redimensionadas de esa imagen, cada una ajustada a un presupuesto distinto de tokens visuales.

Sirve para visualizar cuánto detalle "ve" un modelo como Gemma dependiendo de cuántos tokens se le permiten para procesar una imagen.

## 3. Análisis PEAS

| Elemento | Respuesta |
|---|---|
| **Performance** | Que las imágenes generadas mantengan la proporción original correctamente, que el cálculo de tokens sea preciso, y que la reducción de calidad sea coherente con el presupuesto establecido. |
| **Environment** | La imagen que el usuario sube o selecciona, y la interfaz web donde se muestran los resultados. |
| **Actuators** | Generar y mostrar las versiones redimensionadas de la imagen, mostrar las nuevas dimensiones (ancho x alto) y el conteo de tokens correspondiente a cada versión. |
| **Sensors** | La imagen cargada por el usuario (o seleccionada de las muestras) y su resolución original. |

## 4. Clasificación del entorno

| Propiedad | Clasificación | Justificación |
|---|---|---|
| **Observable** | Total | El agente tiene acceso completo a toda la información que necesita (la imagen completa) para hacer su tarea; no hay información oculta. |
| **Determinista** | Sí | Dado el mismo input (misma imagen, mismo presupuesto de tokens), el resultado (dimensiones y calidad de salida) siempre será el mismo. |
| **Episódico** | Sí | Cada imagen se procesa de forma independiente; el resultado de un episodio (una imagen) no depende de imágenes anteriores. |
| **Estático** | Sí | La imagen no cambia mientras el agente la está procesando; no hay elementos dinámicos externos actuando durante el cálculo. |
| **Discreto** | Sí | Los presupuestos de tokens son valores fijos y discretos (70, 140, 280, 560, 1120), no un rango continuo. |
| **Conocido** | Sí | Las reglas de cómo se calculan los tokens a partir del tamaño de imagen son conocidas y fijas (es un algoritmo definido, no algo que el agente deba aprender o descubrir). |

## 5. ¿Qué tipo de programa de agente es?

**Agente de reflejo simple.**

**Justificación:** el sistema no mantiene un estado interno del mundo, no persigue objetivos complejos ni evalúa utilidades; simplemente aplica una función/regla fija: recibe una imagen y un presupuesto de tokens, y devuelve la versión redimensionada correspondiente.

## 6. Reto adicional

### 6.1 Totalmente observable, determinista y episódico

- **Space propuesto:** Gemma 4 – Vision Token Budget  
  https://huggingface.co/spaces/google/gemma4_vision_token_budget

**Justificación:**

- **Totalmente observable:** el agente ve toda la imagen completa de una vez; no hay nada oculto que necesite inferir.
- **Determinista:** la misma imagen con el mismo presupuesto de tokens siempre da exactamente el mismo resultado (mismas dimensiones, mismo cálculo).
- **Episódico:** cada imagen que subes es un episodio independiente. El resultado de procesar la palmera no depende de si antes procesaste otra imagen.

> Este análisis reutiliza directamente lo ya desarrollado en la ficha anterior.

### 6.2 Parcialmente observable, estocástico y secuencial

- **Space propuesto:** Tic Tac Toe Arena (LLMs juegan y comentan Tic-Tac-Toe)  
  https://huggingface.co/spaces/srk-dot-ai/Tic-Tac-Toe
- **Alternativa:** Space de Tic-Tac-Toe contra computadora (akhaliq)  
  https://huggingface.co/akhaliq/spaces  
  *(buscar: "Play Tic Tac Toe against a friend or the computer")*

**Justificación:**

- **Parcialmente observable:** aunque el tablero es visible, el agente (la IA que juega) no conoce con certeza qué estrategia o próxima jugada tiene en mente su oponente humano; solo observa el estado actual del tablero, no las intenciones futuras del otro jugador.
- **Estocástico:** si el oponente es humano, sus movimientos no son perfectamente predecibles desde la perspectiva del agente; dos partidas con el mismo inicio pueden terminar distinto según decisiones humanas.  
  *(Si el oponente fuera un algoritmo determinista fijo, entonces habría que aclarar que lo estocástico proviene de la variabilidad del jugador humano.)*
- **Secuencial:** cada jugada afecta las jugadas futuras y el resultado final de la partida; una decisión en el turno 2 condiciona las opciones disponibles en el turno 5.
