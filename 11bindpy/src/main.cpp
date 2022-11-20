#include <pybind11/embed.h>
namespace py = pybind11;

//PYBIND11_EMBEDDED_MODULE(cpp_module, m) {
//    m.attr("a") = 1;
//}

int main() {
    printf("1\n");
    py::scoped_interpreter guard{};
    printf("2\n");
    auto py_module = py::module_::import("mod1");
    printf("3\n");
    py::object result = py_module.attr("add")(1, 2);
    int n = result.cast<int>();
    printf("n %d", n);
    assert(n == 3);
}