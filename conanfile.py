from conans import ConanFile, CMake


class Armadillo(ConanFile):
    name = "libarmadillo"
    version = "7.800.0"
    settings = "os", "compiler", "build_type", "arch"
    url = "http://arma.sourceforge.net/"
    license = "Apache-2.0"
    description = "High quality linear algebra library (matrix maths) for the C++ language, aiming towards a good " \
                  "balance between speed and ease of use "

    def source(self):
        self.run("wget http://sourceforge.net/projects/arma/files/armadillo-7.800.0.tar.xz")
        self.run("tar -xvf armadillo-7.800.0.tar.xz")

    def build(self):
        cmake = CMake(self.settings)
        self.run("cmake %s/armadillo-7.800.0 %s" % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build .")

    def package(self):
        self.copy("armadillo", dst="include", src="armadillo-7.800.0/include")
        self.copy("*.hpp", dst="include/armadillo_bits", src="armadillo-7.800.0/include/armadillo_bits")
        self.copy("*.so", dst="lib", src="")

    def package_info(self):
        self.cpp_info.libs = ["armadillo"]
