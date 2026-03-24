import pandas
def load_tilemap(text_tilemap, object_map):
    object_tilemap = []
    for x_cord, row in text_tilemap.iterrows():
        object_row = []
        for y_cord, tile in enumerate(row):
            for hash_, object_ in object_map.items():
                if tile == hash_:
                    object_row.append(object_(x_cord,y_cord))
        object_tilemap.append(object_row)
    return pandas.DataFrame(object_tilemap)


def save_tilemap(tilemap, object_map):
    
    text_tilemap = []
    for x_cord, row in tilemap.iterrows():
        text_row = []
        for y_cord, tile in enumerate(row):
            for hash_, object_ in object_map.items():
                if isinstance(tile, object_):
                    text_row.append(hash_)
        text_tilemap.append(text_row)
    return text_tilemap