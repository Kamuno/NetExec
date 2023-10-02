# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(
    ['./nxc/netexec.py'],
     pathex=['./nxc'],
     binaries=[],
     datas=[
        ('./nxc/protocols', 'nxc/protocols'),
        ('./nxc/data', 'nxc/data'),
        ('./nxc/modules', 'nxc/modules')
     ],
     hiddenimports=[
        'impacket.examples.secretsdump',
        'impacket.dcerpc.v5.lsat',
        'impacket.dcerpc.v5.transport',
        'impacket.dcerpc.v5.lsad',
        'impacket.dcerpc.v5.gkdi',
        'impacket.dcerpc.v5.rprn',
        'impacket.dpapi_ng',
        'impacket.tds',
        'impacket.version',
        'impacket.ldap.ldap',
        'nxc.connection',
        'nxc.servers.smb',
        'nxc.protocols.smb.wmiexec',
        'nxc.protocols.smb.atexec',
        'nxc.protocols.smb.smbexec',
        'nxc.protocols.smb.mmcexec',
        'nxc.protocols.smb.smbspider',
        'nxc.protocols.smb.passpol',
        'nxc.protocols.mssql.mssqlexec',
        'nxc.helpers.bash',
        'nxc.helpers.bloodhound',
        'nxc.helpers.msada_guids',
        'paramiko',
        'pypsrp.client',
        'pywerview.cli.helpers',
        'pylnk3',
        'pypykatz',
        'masky',
        'msldap',
        'msldap.connection',
        'lsassy',
        'lsassy.dumper',
        'lsassy.parser',
        'lsassy.session',
        'lsassy.impacketfile',
        'dns',
        'dns.name',
        'dns.resolver',
        'dploot',
        'dploot.triage',
        'dploot.triage.rdg',
        'dploot.triage.vaults',
        'dploot.triage.browser',
        'dploot.triage.credentials',
        'dploot.triage.masterkeys',
        'dploot.triage.backupkey',
        'dploot.triage.wifi',
        'dploot.lib.target',
        'dploot.lib.smb',
        'pyasn1_modules.rfc5652',
        'unicrypto.backends.pycryptodomex',
     ],
     hookspath=['./nxc/.hooks'],
     runtime_hooks=[],
     excludes=[],
     win_no_prefer_redirects=False,
     win_private_assemblies=False,
     cipher=block_cipher,
     noarchive=False
 )
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='nxc',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    icon='./nxc/data/nxc.ico'
)
