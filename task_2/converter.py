import logging
from create_serializer import create_serializer_file

logging.basicConfig(
    level=logging.WARNING, filename="warning.log", format="%(levelname)s: %(message)s"
)

read = "r"
bread = "br"
write = "w"
bwrite = "bw"


def string_converter(_str, in_lang, out_lang):
    if in_lang == out_lang:
        return _str
    loader = create_serializer_file(in_lang)
    dumper = create_serializer_file(out_lang)
    return dumper.dumps(loader.loads(_str))


def file_converter(input_path, output_path, in_lang="json", out_lang="json"):
    try:
        in_ext = input_path.split(".")[-1]
        out_ext = output_path.split(".")[-1]
        loader = create_serializer_file(in_lang, input_path)
        if in_ext == "pickle":
            read_m = bread
        else:
            read_m = read
        if out_ext == "pickle":
            write_m = bwrite
        else:
            write_m = write
        dumper = create_serializer_file(out_lang, output_path)
        if loader is dumper:
            logging.info("Don't need to convert")
            return
        with open(input_path, read_m) as fp:
            loaded_data = loader.load(fp)

        with open(output_path, write_m) as fp:
            dumper.dump(loaded_data, fp)

    except TypeError as e:
        logging.warning(f"Warning: {e}")
