from .strefer_plus_dynamic import STReferPlusDynamicDataset
from .strefer_dynamic import STReferDynamicDataset

def create_dataset(args, split):
    if args.dataset == 'wildrefer':
        return STReferPlusDynamicDataset(args, split)
    elif args.dataset == 'strefer':
        return STReferDynamicDataset(args, split)