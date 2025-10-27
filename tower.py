import cadquery as cq

radio_exterior = 15
espesor_pared = 2
altura = 40
extension_espesor = 8
radio_anillo_ext = 20
radio_interior = radio_exterior - espesor_pared

# Parámetros de la base
radio_base = 25
altura_base = 5

# Base ancha
base = (
    cq.Workplane("XY")
    .circle(radio_base)
    .extrude(altura_base)
)

# Cilindro hueco
cilindro_hueco = (
    cq.Workplane("XY")
    .workplane(offset=altura_base)
    .circle(radio_exterior)
    .circle(radio_interior)
    .extrude(altura)
)

# Anillo de extensión
anillo_extension = (
    cq.Workplane("XY")
    .workplane(offset=altura_base + altura)
    .circle(radio_anillo_ext)
    .circle(radio_interior)
    .extrude(extension_espesor)
)

# Tapa superior
tapa = (
    cq.Workplane("XY")
    .workplane(offset=altura_base + altura + extension_espesor)
    .circle(radio_anillo_ext)
    .circle(radio_interior)
    .extrude(2)
)

# Almenas o muescas de la torre
altura_almenas = 8
ancho_almena = 4
num_almenas = 8


almenas = (
    cq.Workplane("XY")
    .workplane(offset=altura_base + altura + extension_espesor + 2)
    .polarArray(radio_anillo_ext - ancho_almena/2, 0, 360, num_almenas)
    .rect(ancho_almena, espesor_pared * 2)
    .extrude(altura_almenas)
)

#union del modelado de las muescas, la base, el cuerpo y el anillo externo
pieza_final = base.union(cilindro_hueco).union(anillo_extension).union(tapa).union(almenas)

show_object(pieza_final)

#Cod:160004613-160004725