def pre_build(output, conanfile, **kwargs):
    build_type = conanfile.settings.get_safe('build_type')
    runtime = conanfile.settings.get_safe('compiler.runtime')

    if build_type is None or runtime is None:
        return

    ok = runtime.endswith('d') and build_type == 'Debug' or not runtime.endswith('d') and build_type == 'Release'
    if not ok:
        output.error(f'build_type: {build_type}')
        output.error(f'runtime: {runtime}')
        raise Exception("Build-type mismatch between 'compiler.runtime' and 'build_type!")
