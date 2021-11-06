import re


def parse_hpgl_string(arg):
    '''The function takes a string `arg` of HPGL commands, parses them
    (separates them) and returns them in a list.
    '''
    if not isinstance(arg, str):
        raise TypeError('`arg` must be of type string.')

    # find label terminator first (DT)
    try:
        terminator = re.search('DT(.*?)(,[01])?;', arg).group(1)
    except:
        terminator = '\x03'  # EOT

    string_commands = ['LB', 'BL']
    numeric_commands = ['AA', 'AF', 'AH', 'AP', 'AR', 'AS',
                        'BF',
                        'CA', 'CC', 'CI', 'CM', 'CP', 'CS', 'CT', 'CV',
                        'DC', 'DF', 'DI', 'DP', 'DR', 'DS', 'DV',  # DL
                        'EA', 'EC', 'EP', 'ER', 'ES', 'EW',
                        'FP', 'FR', 'FS', 'FT',
                        'GC',  # GM GP
                        'IM', 'IN', 'IP', 'IV', 'IW',
                        'KY',
                        'LO', 'LT',
                        'NR',
                        'OA', 'OC', 'OD', 'OE', 'OF', 'OG', 'OH', 'OI', 'OK', 'OL', 'OO', 'OP', 'OS', 'OT', 'OW',
                        'PA', 'PB', 'PD', 'PG', 'PM', 'PR', 'PS', 'PT', 'PU',
                        'RA', 'RO', 'RR',
                        'SA', 'SC', 'SI', 'SL', 'SM', 'SP', 'SR', 'SS',  # SG
                        'TL',
                        # 'UC', UF
                        'VS',
                        'WD', 'WG',
                        'XT',
                        'YT']
    ## TODO: Add all the supported escape (DCI) commands.
    dci_commands = ['\x1b\.\(', '\x1b\.Y']

    # NOTE: added '-' to hpgl_patter because we were barfing on strings like
    # 'PA1.99,-5.00;' -- the ,- construction wasn't being parsed correctly.
    # Don't understand why normal negative integers were being parsed
    # correctly though...
    # NOTE: some files have whitespace as separator,
    # even though that's not the official grammar
    numeric_pattern = '|'.join([c + '[-0-9., ]*' for c in numeric_commands])
    dci_pattern = '|'.join([c + '[0-9.;]*' for c in dci_commands])
    string_pattern = '|'.join([c + '.*?[%s]' % terminator for c in string_commands])
    pattern = '|'.join([numeric_pattern, string_pattern, dci_pattern])
    ## this assumes that the re will find each and every hpgl command
    ## with the pattern. Any command not matched will effectively be
    ## removed... we don't want that.
    result = re.findall(pattern, arg)
    return ['DT' + terminator] + result
