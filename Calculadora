import streamlit as st

def calculadora_streamlit():
    st.title("🧮 Calculadora Simple")
    st.write("¡Pon a prueba lo que has aprendido!")

    num1 = st.number_input("Introduce el primer número", value=0.0, format="%.2f")
    num2 = st.number_input("Introduce el segundo número", value=0.0, format="%.2f")

    operacion = st.selectbox(
        "Selecciona una operación:",
        ("Sumar (+)", "Restar (-)", "Multiplicar (*)", "Dividir (/)")
    )

    resultado = None

    if st.button("Calcular"):
        try:
            if operacion == "Sumar (+)":
                resultado = num1 + num2
            elif operacion == "Restar (-)":
                resultado = num1 - num2
            elif operacion == "Multiplicar (*)":
                resultado = num1 * num2
            elif operacion == "Dividir (/)":
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    st.error("Error: No se puede dividir por cero.")
            else:
                st.warning("Operación no reconocida.")
        except ValueError:
            st.error("Por favor, introduce números válidos.")
        except Exception as e:
            st.error(f"Ocurrió un error inesperado: {e}")

    if resultado is not None:
        st.success(f"El resultado es: {resultado}")

if __name__ == "__main__":
    calculadora_streamlit()
