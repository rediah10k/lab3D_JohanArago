import cadquery as cq

# Parámetros arbitrarios
radio_exterior = 15    # radio exterior del cilindro hueco
espesor_pared = 2      # grosor de la pared del cilindro
altura = 40            # altura del cilindro hueco

# Parámetros del anillo de extensión
extension_espesor = 8      # altura del anillo exterior
radio_anillo_ext = 20      # radio exterior del anillo de extensión (mayor al radio_exterior)
# Radio interior siempre es radio_exterior - espesor_pared
radio_interior = radio_exterior - espesor_pared

# Cilindro hueco
cilindro_hueco = (
    cq.Workplane("XY")
    .circle(radio_exterior)
    .circle(radio_interior)
    .extrude(altura)
)

# Anillo de extensión
anillo_extension = (
    cq.Workplane("XY")
    .circle(radio_anillo_ext)
    .circle(radio_interior)
    .extrude(extension_espesor)
    .translate((0, 0, altura))
)

# Unir ambas piezas
pieza_final = cilindro_hueco.union(anillo_extension)

show_object(pieza_final)  # Solo necesario en CQ-editor o Jupyter