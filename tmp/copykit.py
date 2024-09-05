import copykitten
from generate_penguin_logo import draw_penguin_logo


copykitten.copy("The kitten says meow")
copykitten.copy_image(draw_penguin_logo(100,100).tobytes(),100,100)



