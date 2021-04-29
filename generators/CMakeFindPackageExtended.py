import textwrap

from conans.client.generators import CMakeFindPackageGenerator
from jinja2 import Template


class CMakeFindPackageExtended(CMakeFindPackageGenerator):
    # name = 'cmake_find_package_extended'

    @property
    def content(self):
        content = super(CMakeFindPackageExtended, self).content
        for pkg_name, cpp_info in self.deps_build_info.dependencies:
            if cpp_info.get_property('INTERFACE_LINK_OPTIONS'):
                print(f"{cpp_info.name} PROPERTY 'INTERFACE_LINK_OPTIONS': {cpp_info.get_property('INTERFACE_LINK_OPTIONS')}")
                
                fm_name = cpp_info.names[CMakeFindPackageExtended.name]
                for file in content.keys():
                    if fm_name in file:
                        content[file] += textwrap.dedent("""
set_target_properties(GTest::GMockMain
    PROPERTIES
        INTERFACE_LINK_OPTIONS "/SUBSYSTEM:WINDOWSCE;/ENTRY:mainACRTStartup"
)
                        """)

        return content
