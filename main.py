import tkinter as tk

# Cara en emojis (cada emoji es un cuadrado de color)
CARA = """
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜⬜
⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜
⬜⬜🟨🟨⬛🟨🟨🟨🟨⬛🟨🟨🟨⬜⬜
⬜⬜🟨🟨⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨⬜
⬜⬜🟨🟨⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨⬜
⬜⬜🟨🟨⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨⬜
⬜⬜🟨🟨⬛🟨🟨🟨🟨⬛🟨🟨🟧🟧⬜
⬜⬜🟧🟨🟨🟨🟨🟨🟨🟨🟨🟨🟧🟧⬜
⬜⬜🟧🟨⬛🟨🟨🟨🟨⬛🟨🟧🟧🟧⬜
⬜⬜🟧🟧⬛🟨🟨🟨🟨⬛🟧🟧🟧⬜⬜
⬜⬜⬜🟧⬛⬛⬛⬛⬛⬛🟧🟧🟧⬜⬜
⬜⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
"""

# Colores parecidos a los emojis de Twemoji
COLORES = {
    "⬜": "#FFFFFF",
    "🟨": "#FFCC4D",
    "⬛": "#292F33",
    "🟧": "#F4900C",
}

TAMANO_CELDA = 22


def leer_cara(texto):
    """Convierte el texto de emojis en una matriz de caracteres."""
    filas = []
    for linea in texto.strip().splitlines():
        fila = [c for c in linea if c in COLORES]
        if fila:
            filas.append(fila)
    return filas


def comprobar_respuesta(pregunta):
    """Misma lógica que el programa original."""
    if pregunta == "paris":
        return "oh oui oui oui it is paris!"
    return "nope, it is paris,,,"


def main():
    root = tk.Tk()
    root.title("Quiz: capital de Francia")
    root.resizable(False, False)

    # Dibujar la cara
    filas = leer_cara(CARA)
    ancho = len(filas[0]) * TAMANO_CELDA
    alto = len(filas) * TAMANO_CELDA
    lienzo = tk.Canvas(root, width=ancho, height=alto,
                       highlightthickness=0, bg="white")
    lienzo.pack(padx=10, pady=10)

    for y, fila in enumerate(filas):
        for x, emoji in enumerate(fila):
            lienzo.create_rectangle(
                x * TAMANO_CELDA, y * TAMANO_CELDA,
                (x + 1) * TAMANO_CELDA, (y + 1) * TAMANO_CELDA,
                fill=COLORES[emoji], outline="",
            )

    # Pregunta
    tk.Label(root, text="What is the capital of France?",
             font=("Arial", 14)).pack()

    entrada = tk.Entry(root, font=("Arial", 14), justify="center")
    entrada.pack(pady=5)
    entrada.focus()

    resultado = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
    resultado.pack(pady=5)

    def al_responder(event=None):
        resultado.config(text=comprobar_respuesta(entrada.get()))

    tk.Button(root, text="Responder", command=al_responder).pack(pady=5)
    entrada.bind("<Return>", al_responder)

    root.mainloop()


if __name__ == "__main__":
    main()