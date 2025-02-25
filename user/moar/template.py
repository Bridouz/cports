pkgname = "moar"
pkgver = "1.31.2"
pkgrel = 2
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal pager program"
maintainer = "Biswapriyo Nath <nathbappai@gmail.com>"
license = "BSD-2-Clause"
url = "https://github.com/walles/moar"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f88f244c18ee1a8ba1428bc195f9140d53a551124cc8b54c0c7942ba6433e2d7"


def install(self):
    self.install_bin("build/moar")
    self.install_license("LICENSE")
    self.install_man("moar.1")
