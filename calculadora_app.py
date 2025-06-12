import streamlit as st

def calculadora_streamlit_avanzada():
    st.title("🧮 Calculadora Versátil")
    st.write("¡Elige cómo quieres operar tus números!")

    tipo_numero = st.radio(
        "¿Qué tipo de números quieres usar?",
        ("Números decimales (ej. 3.14)", "Números enteros (ej. 5, 10)")
    )

    num1_conv = 0.0
    num2_conv = 0.0
    error_input = False


    st.subheader("Introduce tus números:")
    num1_str = st.text_input("Primer número", value="0", key="num1")
    num2_str = st.text_input("Segundo número", value="0", key="num2")

    try:
        if tipo_numero == "Números enteros (ej. 5, 10)":
            num1_conv = int(float(num1_str)) 
            num2_conv = int(float(num2_str))
        else:
            num1_conv = float(num1_str)
            num2_conv = float(num2_str)
    except ValueError:
        st.error("Por favor, introduce solo números válidos.")
        error_input = True
    except Exception as e:
        st.error(f"Ocurrió un error inesperado al procesar los números: {e}")
        error_input = True


    st.subheader("Selecciona una operación:")
    operacion = st.selectbox(
        "Operación:",
        ("Sumar (+)", "Restar (-)", "Multiplicar (*)", "Dividir (/)")
    )

    resultado = None


    if st.button("Calcular", disabled=error_input): 
        if not error_input:
            try:
                if operacion == "Sumar (+)":
                    resultado = num1_conv + num2_conv
                elif operacion == "Restar (-)":
                    resultado = num1_conv - num2_conv
                elif operacion == "Multiplicar (*)":
                    resultado = num1_conv * num2_conv
                elif operacion == "Dividir (/)":
                    if num2_conv != 0:
                        resultado = num1_conv / num2_conv
                    else:
                        st.error("Error: No se puede dividir por cero.")
                        resultado = None
                
              
                if resultado is not None:
                    if tipo_numero == "Números enteros (ej. 5, 10)":
                   
                        if resultado == int(resultado):
                            st.success(f"El resultado es: {int(resultado)}")
                        else:
                       
                            st.warning(f"El resultado es decimal, aunque operaste con enteros: {resultado:.2f}")
                    else: 
                        st.success(f"El resultado es: {resultado}")

            except Exception as e:
                st.error(f"Ocurrió un error durante el cálculo: {e}")

if __name__ == "__main__":
    calculadora_streamlit_avanzada()
