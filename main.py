from PIL import Image

def resize_image(input_path,output_path,size):
    with Image.open (input_path) as img:
        img=img.resize(size,Image.LANCZOS)
        img.save(output_path)
        print(f"Image resized and saved as {output_path}")

input_image="nature.jpg"
output_image="nature_resize1.jpg"
new_size=(800,600)
resize_image(input_image,output_image,new_size)