import glob
import os

from conans.client.generators import CMakeFindPackageGenerator


class CMakeFindPackageMigration(CMakeFindPackageGenerator):

    @property
    def content(self):
        content = super(CMakeFindPackageMigration, self).content

        for pkg_name, cpp_info in self.deps_build_info.dependencies:
            cmake_file_found = False
            for f in glob.glob(f'{cpp_info.rootpath}/**/*.cmake', recursive=True):
                if pkg_name.lower() in os.path.basename(f).lower():
                    cmake_file_found = True
                    break

            if cmake_file_found:
                print(f'Deleting autogenerated Find{pkg_name}.cmake for package {pkg_name}, root_path: {cpp_info.rootpath}')
                del content[f'Find{pkg_name}.cmake']

        return content
