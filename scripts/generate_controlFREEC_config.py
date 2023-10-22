import argparse
import sys

def run(argv):
    """
    Generate a config file for controlFREEC given a set of parameters
    """

    parser = argparse.ArgumentParser(
        prog="generate_controlFREEC_config", description="Generate a config file for controlFREEC given a set of parameters"
    )

    parser.add_argument("--sample_name", help="sample_name", required=True)

    parser.add_argument("--BedGraphOutput", help="general:BedGraphOutput", required=True)
    parser.add_argument("--chrLenFile",help="general:chrLenFile",required=True)
    parser.add_argument("--contaminationAdjustment", help="general:contaminationAdjustment", required=True)
    parser.add_argument("--maxThreads", help="general:maxThreads", required=True)
    parser.add_argument("--window", help="general:window", required=True)
    parser.add_argument("--chrFiles", help="general:chrFiles", required=True)
    parser.add_argument("--degree", help="general:degree", required=True)
    parser.add_argument("--forceGCcontentNormalization", help="general:forceGCcontentNormalization", required=False)
    parser.add_argument("--sex", help="general:sex", required=False)
    parser.add_argument("--ploidy", help="general:ploidy", required=False)

    parser.add_argument("--sample_mateFile", help="sample:mateFile", required=True )
    parser.add_argument("--sample_mateCopyNumberFile", help="sample:mateCopyNumberFile", required=True )
    parser.add_argument("--sample_miniPileupFile", help="sample:miniPileup", required=True )
    parser.add_argument("--sample_inputFormat", help="sample:inputFormat", required=True )
    parser.add_argument("--sample_mateOrientation", help="sample:mateOrientation", required=True)

    parser.add_argument("--control_mateFile", help="control:mateFile", required=True)
    parser.add_argument("--control_mateCopyNumberFile", help="control:mateCopyNumberFile", required=True )
    parser.add_argument("--control_miniPileupFile", help="control:miniPileup", required=True )
    parser.add_argument("--control_inputFormat", help="control:inputFormat", required=True)
    parser.add_argument("--control_mateOrientation", help="control:mateOrientation", required=True)

    parser.add_argument("--baf_makePileup", help="baf:makePileup", required=False)
    parser.add_argument("--baf_fastaFile", help="baf:fastaFile", required=True)
    parser.add_argument("--baf_SNPfile", help="baf:SNPfile", required=True)

    args = parser.parse_args(argv[1:])

    config_text=''
    ### general section ###
    config_text = '\n'.join([config_text,'', '[general]'])
    str = 'BedGraphOutput=' + args.BedGraphOutput
    config_text = '\n'.join([config_text, str])
    str = 'chrLenFile='+ args.chrLenFile
    config_text = '\n'.join([config_text, str])
    str = 'contaminationAdjustment=' + args.contaminationAdjustment
    config_text = '\n'.join([config_text, str])
    str = 'maxThreads=' + args.maxThreads
    config_text = '\n'.join([config_text, str])
    str = 'window=' + args.window
    config_text = '\n'.join([config_text, str])
    str = 'chrFiles=' + args.chrFiles
    config_text = '\n'.join([config_text, str])
    str = 'degree=' + args.degree
    config_text = '\n'.join([config_text, str])
    if args.forceGCcontentNormalization:
        str = 'forceGCcontentNormalization=' + args.forceGCcontentNormalization
        config_text = '\n'.join([config_text, str])
    if args.sex:
        str = 'sex=' + args.sex
        config_text = '\n'.join([config_text, str])
    if args.ploidy:
        str = 'ploidy=' + args.ploidy
        config_text = '\n'.join([config_text, str])

    ### sample section ###
    config_text = '\n'.join([config_text,'' ,'[sample]'])
    str = 'mateFile=' + args.sample_mateFile
    config_text = '\n'.join([config_text, str])
    str = 'mateCopyNumberFile=' + args.sample_mateCopyNumberFile
    config_text = '\n'.join([config_text, str])
    str = 'miniPileup=' + args.sample_miniPileupFile
    config_text = '\n'.join([config_text, str])
    str = 'inputFormat=' + args.sample_inputFormat
    config_text = '\n'.join([config_text, str])
    str = 'mateOrientation=' + args.sample_mateOrientation
    config_text = '\n'.join([config_text, str])

    ### control section ###
    config_text = '\n'.join([config_text,'', '[control]'])
    str = 'mateFile=' + args.control_mateFile
    config_text = '\n'.join([config_text, str])
    str = 'mateCopyNumberFile=' + args.control_mateCopyNumberFile
    config_text = '\n'.join([config_text, str])
    str = 'miniPileup=' + args.control_miniPileupFile
    config_text = '\n'.join([config_text, str])
    str = 'inputFormat=' + args.control_inputFormat
    config_text = '\n'.join([config_text, str])
    str = 'mateOrientation=' + args.control_mateOrientation
    config_text = '\n'.join([config_text, str])

    ### BAF section ###
    config_text = '\n'.join([config_text,'', '[BAF]'])
    # str = 'makePileup=' + args.baf_makePileup
    # config_text = '\n'.join([config_text, str])
    str = 'fastaFile=' + args.baf_fastaFile
    config_text = '\n'.join([config_text, str])
    str = 'SNPfile=' + args.baf_SNPfile
    config_text = '\n'.join([config_text, str])
    if args.baf_makePileup:
        str = 'makePileup=' + args.baf_makePileup
        config_text = '\n'.join([config_text, str])

    with open(args.sample_name + ".config.txt", "w") as text_file:
        text_file.write(config_text)


if __name__ == "__main__":
    run(sys.argv)
