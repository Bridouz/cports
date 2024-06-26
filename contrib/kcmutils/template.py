pkgname = "kcmutils"
pkgver = "6.2.0"
pkgrel = 1
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Utilities for KDE System Settings modules"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcmutils/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcmutils-{pkgver}.tar.xz"
sha256 = "8cef140ca9eabf29e88a08489c799078e85247907fd6f74165aeafd4ed40c0bb"
# FIXME: cfi crashes systemsettings (when entering almost any page) in libkcmutilsqmlplugin.so
hardening = ["vis", "!cfi"]


@subpackage("kcmutils-devel")
def _devel(self):
    self.depends += [
        "kconfigwidgets-devel",
        "kcoreaddons-devel",
        "qt6-qtdeclarative-devel",
    ]

    return self.default_devel()
