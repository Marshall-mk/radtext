"""
Usage:
    parse [options] -i FILE -o FILE

Options:
    --overwrite
    --bllip_model <str>     Bllip parser model path [default: ]
    -o FILE
    -i FILE
"""
import bioc
import docopt
import tqdm
from cmd_utils import process_options
from radtext.parse_bllip import BioCParserBllip


if __name__ == '__main__':
    argv = docopt.docopt(__doc__)
    process_options(argv)

    processor = BioCParserBllip(model_dir=argv['--model'])

    with open(argv['-i']) as fp:
        collection = bioc.load(fp)

    for doc in tqdm.tqdm(collection.documents):
        processor.process_document(doc)

    with open(argv['-o'], 'w') as fp:
        bioc.dump(collection, fp)
