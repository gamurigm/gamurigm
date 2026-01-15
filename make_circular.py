from PIL import Image, ImageDraw

# Abrir imagen original
img = Image.open('assets/me.png').convert('RGBA')

# Crear máscara circular
size = min(img.size)
mask = Image.new('L', (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size, size), fill=255)

# Recortar imagen al centro si no es cuadrada
if img.size[0] != img.size[1]:
    left = (img.size[0] - size) // 2
    top = (img.size[1] - size) // 2
    img = img.crop((left, top, left + size, top + size))

# Aplicar máscara circular
output = Image.new('RGBA', (size, size), (0, 0, 0, 0))
output.paste(img, (0, 0))
output.putalpha(mask)

# Guardar
output.save('assets/me-circular.png', 'PNG')
print(f'✅ Imagen circular guardada: assets/me-circular.png ({size}x{size}px)')
