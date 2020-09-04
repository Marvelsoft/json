from conans import ConanFile, tools

def get_version():
    try:
        return tools.load("version.txt").strip()
    except Exception:
        return None

class JsonConan(ConanFile):
    name = "json"
    version = get_version()
    license = "MIT"
    url = "https://gitlab.tz.marvelsoft.net/opensource/json"
    description = "JSON for Modern C++"

    # -------------------
    # ---   SOURCES   ---
    # -------------------
    exports_sources = "single_include/*"
    no_copy_source = True

    def package(self):
        self.copy("*.hpp", dst="include", src="single_include")

    def package_id(self):
        self.info.header_only()
