import slugify


def generate_path(instance, filename):
    result = f"{slugify.slugify(str(instance.album.name))}/{filename}"
    if result.find("portfolio") != -1:
        result = "portfolio/" + result
    print(result)
    return result
