import cadquery as cq

# Parámetros del tubo de llegada
radio_exterior = 15  
altura = 40 
espesor_pared = 2 
extension_espesor = 3


cilindro_hueco = (
    cq.Workplane("XY")
    .circle(radio_exterior)
    .circle(radio_exterior - espesor_pared)
    .extrude(altura)
)