from conans import ConanFile, Meson
import os

class JsonTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "pkg_config"

    def build(self):
        meson = Meson(self)
        meson.configure()
        meson.build()

    def test(self):
        self.run(".%stest_package" % os.sep)
