def generate__position_coord():
    position_image_coords = []
    for i in range(ord('A'),ord('I')):
        for j in range(1,13):
            coord = str(chr(i))+str(j) + ' Position1_ch00'
            position_image_coords.append(coord)
            # print(coord)
    return position_image_coords
position_image_coords = generate__position_coord()
print(position_image_coords)