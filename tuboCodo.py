import cadquery as cq

radio_exterior = 15
espesor_pared = 2
altura = 40
extension_espesor = 8
radio_anillo_ext = 20
radio_interior = radio_exterior - espesor_pared

# Base: cilindro hueco con anillo
cilindro_hueco = (
    cq.Workplane("XY")
    .circle(radio_exterior)
    .circle(radio_interior)
    .extrude(altura)
)

anillo_extension = (
    cq.Workplane("XY")
    .circle(radio_anillo_ext)
    .circle(radio_interior)
    .extrude(extension_espesor)
    .translate((0, 0, altura))
)

# Tapa superior
tapa = (
    cq.Workplane("XY")
    .workplane(offset=altura + extension_espesor)
    .circle(radio_anillo_ext)
    .circle(radio_interior)
    .extrude(2)
)


altura_almenas = 8
ancho_almena = 6
num_almenas = 10

#Muescas de la torre con sus parametros
almenas = (
    cq.Workplane("XY")
    .workplane(offset=altura + extension_espesor + 2)  # encima de la tapa
    .polarArray(radio_anillo_ext - ancho_almena/2, 0, 360, num_almenas)
    .rect(ancho_almena, espesor_pared * 2)
    .extrude(altura_almenas)
)

pieza_final = cilindro_hueco.union(anillo_extension).union(tapa).union(almenas)

show_object(pieza_final)