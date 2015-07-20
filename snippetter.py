
import os
import pprint

rootpath = '/home/mmyalipu/.emacs.d/elpa/yasnippet-20150415.244/snippets'

def list_files(rootpath=rootpath):
    for dir, sub_dir, flist in os.walk(rootpath):
        if dir.endswith('python-mode'):
            for fl in flist:
                yield fl


output = dict()
for fl in list_files():
    with open('/'.join([rootpath,'python-mode', fl]),'r') as f:
        snippet_line = f.readline()
        if snippet_line.strip() == '# -*- mode: snippet -*-':
            name_line = f.readline()
            key_line = f.readline()
            output[key_line.replace('# key: ', '').replace('\n','')] = name_line.replace('# name: ','').replace('\n','')

pprint.pprint(output)

'''
Output : 
=========
{'.': 'self',
 'a': 'all',
 'ae': 'assertEqual',
 'af': 'assertFalse',
 'ai': 'assertIn',
 'an': 'assetNotIn',
 'ane': 'assertNotEqual',
 'ar': 'assertRaises',
 'arg': 'arg_positional',
 'ass': 'assert',
 'at': 'assertTrue',
 'cdb': 'celery pdb',
 'cls': 'cls',
 'cm': 'classmethod',
 'cont': '__contains__',
 'd': 'doc',
 'dec': 'dec',
 'doc': 'doctest',
 'dt': 'deftest',
 'ent': '__enter__',
 'eq': '__eq__',
 'ex': '__exit__',
 'f': 'function',
 'fd': 'function_docstring',
 'from': 'from',
 'fw': 'with_statement',
 'getit': '__getitem__',
 'id': 'init_docstring',
 'if': 'if',
 'ife': 'ife',
 'ifm': 'ifmain',
 'imp': 'import',
 'init': 'init',
 'int': 'interact',
 'iter': '__iter__',
 'lam': 'lambda',
 'len': '__len__',
 'li': 'list',
 'ln': 'logger_name',
 'log': 'logging',
 'm': 'method',
 'main': 'main',
 'md': 'method_docstring',
 'mt': 'metaclass',
 'new': '__new__',
 'not_impl': 'not_impl',
 'np': 'np',
 'p': 'print',
 'pargs': 'parse_args',
 'pars': 'parser',
 'ps': 'pass',
 'r': 'return',
 'reg': 'reg',
 'repr': '__repr__',
 's': 'self_without_dot',
 'script': 'script',
 'setdef': 'setdef',
 'setit': '__setitem__',
 'setup': 'setup',
 'size': 'size',
 'sm': 'static',
 'sn': 'selfassign',
 'str': '__str__',
 'super': 'super',
 'tcs': 'test_class',
 'tf': 'test_file',
 'tr': 'trace',
 'try': 'try',
 'un': '__unicode__',
 'utf8': 'utf-8 encoding',
 'wh': 'while',
 'with': 'with'}
'''
    
