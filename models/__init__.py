from .wildrefer import WildRefer

def create_model(args):
    return WildRefer(
        args=args,
        num_class=args.max_lang_num,
        input_feature_dim=3,
        num_queries=args.num_queries,
        num_decoder_layers=args.num_decoder_layers,
        self_position_embedding='loc_learned',
        contrastive_align_loss=True,
        d_model=288,
        pointnet_ckpt=None,
        resnet_ckpt=None,
        self_attend=True,
        frame_num=args.frame_num,
        butd=args.butd
    )
