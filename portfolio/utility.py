import slugify


def generate_path_dir(album_name, filename):
    result = f"{slugify.slugify(str(album_name))}"
    if result.find("portfolio") != -1:
        result = "portfolio/" + result

    return result


def generate_path(instance, filename):
    return generate_path_dir(instance.album.name, filename) + "/" + str(filename)
