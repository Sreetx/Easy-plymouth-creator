pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'plymouth_creator_by_sreetx'

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('pkgdatadir', pkgdatadir)
configure_file(
            input: 'plymouth-creator-by_sreetx.in',
           output: 'plymouth-creator-by_sreetx',
    configuration: conf,
          install: true,
      install_dir: get_option('bindir'),
     install_mode: 'r-xr-xr-x'
)

plymouth_creator_by_sreetx_sources = [
    '__init__.py',
    'main.py'
]

install_data(plymouth_creator_by_sreetx_sources, install_dir: moduledir)
